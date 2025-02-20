import xml.etree.ElementTree as ET


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract compounds
    compounds = set()
    for compound in root.findall(".//Compound"):
        name = compound.find("Name").text
        if name:
            compounds.add(name)

    # Extract simulation objects and link with graphic objects
    simulation_objects = {}
    connections = []
    objectTagMap = {}
    for sim_obj in root.findall(".//SimulationObject"):
        obj_name = sim_obj.find("Name").text if sim_obj.find("Name") is not None else "Unnamed"
        obj_name = obj_name.replace("-", "_")  # Remove -
        obj_type = sim_obj.find("Type").text if sim_obj.find("Type") is not None else "Unknown"

        # Extract only the last part of the type (e.g., MaterialStream)
        obj_type_short = obj_type.split(".")[-1]
        if obj_type_short in objectTagMap:
            objectTagMap[obj_type_short] += 1
        else:
            objectTagMap[obj_type_short] = 1
        code = obj_type_short + str(objectTagMap[obj_type_short])

        # Extract properties
        obj_pressure = obj_temperature = obj_massflow = None
        for phase in sim_obj.findall(".//Phase"):
            properties = phase.findall("Properties")[1]
            if properties is not None:
                obj_pressure = properties.find("pressure").text if properties.find("pressure") is not None else None
                obj_temperature = properties.find("temperature").text if properties.find(
                    "temperature") is not None else None
                obj_massflow = properties.find("massflow").text if properties.find("massflow") is not None else None
                break

        simulation_objects[obj_name] = {
            "type": obj_type_short,
            "code": code,
            "pressure": obj_pressure,
            "temperature": obj_temperature,
            "massflow": obj_massflow
        }

    # Extract graphic objects and link by name
    graphic_objects = {}
    for graphic_obj in root.findall(".//GraphicObject"):
        name = graphic_obj.find("Name").text
        name = name.replace("-", "_")
        if name:
            x = graphic_obj.find("X").text if graphic_obj.find("X") is not None else "100"
            y = graphic_obj.find("Y").text if graphic_obj.find("Y") is not None else "100"
            tag = graphic_obj.find("Tag").text if graphic_obj.find("Tag") is not None else "Tag"
            objectType = graphic_obj.find("ObjectType").text if graphic_obj.find("ObjectType") is not None else ""
            graphic_objects[name] = {"x": x, "y": y, "tag": tag, "objectType": objectType}

        # Process connections inside the loop
        for conn in graphic_obj.findall(".//InputConnectors/Connector"):
            from_id = conn.get("AttachedFromObjID")
            if from_id:
                connections.append((from_id.replace("-", "_"), name))

        for conn in graphic_obj.findall(".//OutputConnectors/Connector"):
            to_id = conn.get("AttachedToObjID")
            if to_id:
                connections.append((name, to_id.replace("-", "_")))

    unique_connections = set(tuple(link) for link in connections)

    # Convert back to a list if needed
    unique_connections = list(unique_connections)

    return compounds, simulation_objects, graphic_objects, unique_connections


def generate_python_code(file_name, compounds, sim_objects, graphic_objects, connections):
    python_code = """import clr

dwsimpath = "C:\\\\Users\\\\jcvid\\\\AppData\\\\Local\\\\DWSIM\\\\"
clr.AddReference("System")
clr.AddReference(dwsimpath + "CapeOpen.dll")
clr.AddReference(dwsimpath + "DWSIM.Automation.dll")
clr.AddReference(dwsimpath + "DWSIM.Interfaces.dll")
clr.AddReference(dwsimpath + "DWSIM.GlobalSettings.dll")
clr.AddReference(dwsimpath + "DWSIM.SharedClasses.dll")
clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.dll")
clr.AddReference(dwsimpath + "DWSIM.Thermodynamics.ThermoC.dll")
clr.AddReference(dwsimpath + "DWSIM.UnitOperations.dll")
clr.AddReference(dwsimpath + "DWSIM.Inspector.dll")
clr.AddReference(dwsimpath + "System.Buffers.dll")

from DWSIM.Interfaces.Enums.GraphicObjects import ObjectType
from DWSIM.Thermodynamics import Streams, PropertyPackages
from DWSIM.UnitOperations import UnitOperations
from DWSIM.Automation import Automation3
from DWSIM.GlobalSettings import Settings
from System.IO import Directory, Path, File
from System import String, Environment

# Set current directory to DWSIM path
Directory.SetCurrentDirectory(dwsimpath)

interf = Automation3()
sim = interf.CreateFlowsheet()

# Adding Compounds
"""

    for compound in compounds:
        python_code += f"{compound.replace("-", "_") .lower()} = sim.AvailableCompounds[\"{compound}\"]\n"
        python_code += f"sim.SelectedCompounds.Add({compound.replace("-", "_") .lower()}.Name, {compound.replace("-", "_") .lower()})\n"

    python_code += "\n# Adding Simulation Objects\n"

    for obj_name, obj in sim_objects.items():
        tag = graphic_objects.get(obj_name, {}).get("tag", "Dummy")
        obj_type = graphic_objects.get(obj_name, {}).get("objectType", "")
        if not obj_type:
            obj_type = obj["type"].split(".")[-1]  # Extract last part of type

        code = obj["code"].split(".")[-1]  # Extract last part of type
        x = graphic_objects.get(obj_name, {}).get("x", "100")  # Get X position
        y = graphic_objects.get(obj_name, {}).get("y", "100")  # Get Y position

        python_code += f"# Adding {obj_type}: {obj_name}\n"
        python_code += f"{code} = sim.AddObject(ObjectType.{obj_type}, {int(float(x))}, {int(float(y))}, \"{tag}\")\n"
        python_code += f"{code} = {code}.GetAsObject()\n"

        if obj["temperature"]:
            python_code += f"{code}.SetTemperature({obj['temperature']})  # Temperature in K\n"
        if obj["pressure"]:
            python_code += f"{code}.SetPressure({obj['pressure']})  # Pressure in Pa\n"
        if obj["massflow"]:
            python_code += f"{code}.SetMassFlow({obj['massflow']})  # Mass Flow in kg/s\n"

        python_code += "\n"

    # Add connections immediately after defining the object
    for from_obj, to_obj in connections:
        from_tag = sim_objects.get(from_obj).get("code")
        to_tag = sim_objects.get(to_obj).get("code")
        python_code += f"sim.ConnectObjects({from_tag}.GraphicObject, {to_tag}.GraphicObject, -1, -1)  # {from_tag} to {to_tag}\n"

    python_code += " # Save the flowsheet \n"
    python_code += f"fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), \"{file_name}.xml\")\n"

    python_code += """ 
interf.SaveFlowsheet(sim, fileNameToSave, False)



# Export PFD image
clr.AddReference(dwsimpath + "SkiaSharp.dll")
clr.AddReference("System.Drawing")

from SkiaSharp import SKBitmap, SKImage, SKCanvas, SKEncodedImageFormat
from System.IO import MemoryStream
from System.Drawing import Image
from System.Drawing.Imaging import ImageFormat

# Render PFD to image
PFDSurface = sim.GetSurface()
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
"""
    python_code += f"imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), \"{file_name}.png\")\n"


    python_code +=""" 

image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()


"""

    return python_code


# Example usage
xml_path = "D:\\Masters\\Thesis\\PIGenerator\\src\\revers_engineering\\resources\\b.xml"  # Replace with actual path
file_name = "b"
compounds, simulation_objects, graphic_objects, connections = parse_xml(xml_path)
python_script = generate_python_code(file_name, compounds, simulation_objects, graphic_objects, connections)

# Save the generated Python script
with open("generated_sim.py", "w") as f:
    f.write(python_script)

print("Python script generated successfully.")
