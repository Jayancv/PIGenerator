import os
import re
import xml.etree.ElementTree as ET

# Custom mapping for object names
object_name_mapping = {
    "CompressorExpander": "Compressor",
    "HeaterCooler": "Heater",
    # Add more mappings as needed
}
compound_mapping = {
    "Metano": "Methane",
    "Etano": "Ethane",
    "Propano": "Propane",
    "nButano": "N-butane",
    "iButano": "Isobutane",
    "nPentano": "N-pentane",
    "iPentano": "Isopentane",
    "nHexano": "N-hexane",
    "nHeptano": "N-heptane",
    "nOctano": "N-octane",
    "nNonano": "N-nonane",
    "nDecano": "N-decane",
    "Oxigenio": "Oxygen",
    "Nitrogenio": "Nitrogen",
    "Agua": "Water",
    "DioxidoDeCarbono": "Carbon dioxide",
    "SulfetoDeHidrogenio": "Hydrogen sulfide",
}


def rename(name):
    # Match one or more digits and/or underscores at the beginning, and capture the rest
    m = re.match(r'^([0-9_]+)(.+)$', name)
    if m:
        prefix, rest = m.groups()
        # If prefix has any digits, remove any trailing underscores (to avoid an extra underscore)
        if any(c.isdigit() for c in prefix):
            prefix = prefix.rstrip('_')
        # If the prefix itself starts with an underscore, simply append it
        if prefix and prefix[0] == '_':
            return rest + prefix
        # Otherwise, append with an underscore separator
        if prefix:
            return rest + "_" + prefix
    # Return unchanged if no match (i.e. no digits or underscores in front)
    return name


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract compounds
    compounds = set()
    for compound in root.findall(".//Compound"):
        name = compound.find("Name")
        if name is not None:
            compounds.add(name.text)

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
        streams = []
        if obj_type_short == "DistillationColumn":
            for sub_cmp in ['MaterialStream', 'EnergyStream']:
                # graphic_obj2 =
                # if graphic_obj2 is None:
                #     continue
                for stream in sim_obj.findall(f'.//{sub_cmp}'):
                    stream_type = stream.find('StreamType').text if stream.find('StreamType') is not None else None
                    stream_behavior = stream.find('StreamBehavior').text if stream.find(
                        'StreamBehavior') is not None else None
                    stream_id = stream.find('StreamID').text if stream.find('StreamID') is not None else None
                    streams.append({'StreamType': stream_type, 'StreamBehavior': stream_behavior,
                                    'StreamID': stream_id.replace("-", "_")})

            # for material in sim_obj.findall('.//MaterialStream'):
            #     stream_type = material.find('StreamType').text if material.find('StreamType') is not None else None
            #     stream_behavior = material.find('StreamBehavior').text if material.find(
            #         'StreamBehavior') is not None else None
            #     stream_id = energy.find('StreamID').text if energy.find('StreamID') is not None else None
            #     streams.append({'StreamType': stream_type, 'StreamBehavior': stream_behavior, 'StreamID': stream_id.replace("-", "_")})
            #
            # # Extract EnergyStreams
            # for energy in sim_obj.findall('.//EnergyStream'):
            #     stream_type = energy.find('StreamType').text if energy.find('StreamType') is not None else None
            #     stream_behavior = energy.find('StreamBehavior').text if energy.find(
            #         'StreamBehavior') is not None else None
            #     stream_id = energy.find('StreamID').text if energy.find('StreamID') is not None else None
            #     streams.append({'StreamType': stream_type, 'StreamBehavior': stream_behavior, 'StreamID': stream_id.replace("-", "_")})

        simulation_objects[obj_name] = {
            "type": obj_type_short,
            "code": code,
            "pressure": obj_pressure,
            "temperature": obj_temperature,
            "massflow": obj_massflow,
            "streams": streams
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
        for conn in graphic_obj.findall("./InputConnectors/Connector"):
            from_id = conn.get("AttachedFromObjID")
            if from_id:
                connections.append((from_id.replace("-", "_"), name))

        for conn in graphic_obj.findall("./OutputConnectors/Connector"):
            to_id = conn.get("AttachedToObjID")
            if to_id:
                connections.append((name, to_id.replace("-", "_")))

        for sub_cmp in ["ConnectedToMv", "ConnectedToRv", "ConnectedToCv"]:
            graphic_obj2 = graphic_obj.find(f"./{sub_cmp}")
            if graphic_obj2 is None:
                continue
            name = graphic_obj2.find("Name")
            if name is not None:
                name = graphic_obj2.find("Name").text
                name = name.replace("-", "_")
                # x = graphic_obj2.find("X").text if graphic_obj2.find("X") is not None else "100"
                # y = graphic_obj2.find("Y").text if graphic_obj2.find("Y") is not None else "100"
                # tag = graphic_obj2.find("Tag").text if graphic_obj2.find("Tag") is not None else "Tag"
                # objectType = graphic_obj2.find("ObjectType").text if graphic_obj2.find("ObjectType") is not None else ""
                # graphic_objects[name] = {"x": x, "y": y, "tag": tag, "objectType": objectType}

                # Process connections inside the connections loop
                for conn in graphic_obj2.findall("./InputConnectors/Connector"):
                    from_id = conn.get("AttachedFromObjID")
                    if from_id:
                        connections.append((from_id.replace("-", "_"), name))

                for conn in graphic_obj2.findall("./OutputConnectors/Connector"):
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
        compound_id = rename(compound.replace("-", "_").replace(" ", "_").replace(",", "_").lower())
        compound_name = compound_mapping.get(compound, compound)
        python_code += f"{compound_id} = sim.AvailableCompounds[\"{compound_name}\"]\n"
        python_code += f"sim.SelectedCompounds.Add({compound_id}.Name, {compound_id})\n"

    python_code += "\n# Adding Simulation Objects\n"

    for obj_name, obj in sim_objects.items():
        tag = graphic_objects.get(obj_name, {}).get("tag", "Dummy")
        obj_type = graphic_objects.get(obj_name, {}).get("objectType", "")
        if not obj_type:
            obj_type = obj["type"].split(".")[-1]  # Extract last part of type
        assigned_name = object_name_mapping.get(obj_type, obj_type)

        code = obj["code"].split(".")[-1]  # Extract last part of type
        x = graphic_objects.get(obj_name, {}).get("x", "100")  # Get X position
        y = graphic_objects.get(obj_name, {}).get("y", "100")  # Get Y position

        python_code += f"# Adding {obj_type}: {obj_name}\n"
        python_code += f"{code} = sim.AddObject(ObjectType.{assigned_name}, {int(float(x))}, {int(float(y))}, \"{tag}\")\n"
        python_code += f"{code} = {code}.GetAsObject()\n"

        if obj["temperature"]:
            python_code += f"{code}.SetTemperature({obj['temperature']})  # Temperature in K\n"
        if obj["pressure"]:
            python_code += f"{code}.SetPressure({obj['pressure']})  # Pressure in Pa\n"
        if obj["massflow"]:
            python_code += f"{code}.SetMassFlow({obj['massflow']})  # Mass Flow in kg/s\n"

        python_code += "\n"

    # Add connections immediately after defining the object

    for obj_name, obj in sim_objects.items():
        code = obj["code"].split(".")[-1]  # Extract last part of type

        if obj["streams"]:
            for stream in obj['streams']:
                connect_stream_id = stream['StreamID']
                connect_obj = sim_objects[connect_stream_id]['code']
                if stream['StreamType'] == "Material" and stream['StreamBehavior'] == "OverheadVapor":
                    python_code += f"{code}.ConnectVaporProduct({connect_obj}) # ConnectVaporProduct \n"
                    if (obj_name, connect_stream_id) in connections:
                        connections.remove((obj_name, connect_stream_id))
                if stream['StreamType'] == "Material" and stream['StreamBehavior'] == "Distillate":
                    python_code += f"{code}.ConnectDistillate({connect_obj})  # ConnectDistillate \n"
                    if (obj_name, connect_stream_id) in connections:
                        connections.remove((obj_name, connect_stream_id))
                if stream['StreamType'] == "Material" and stream['StreamBehavior'] == "BottomsLiquid":
                    python_code += f"{code}.ConnectBottoms({connect_obj})  # ConnectBottoms \n"
                    if (obj_name, connect_stream_id) in connections:
                        connections.remove((obj_name, connect_stream_id))
                if stream['StreamType'] == "Energy" and stream['StreamBehavior'] == "Distillate":
                    python_code += f"{code}.ConnectCondenserDuty({connect_obj})  # ConnectCondenserDuty \n"
                    if (obj_name, connect_stream_id) in connections:
                        connections.remove((obj_name, connect_stream_id))
                if stream['StreamType'] == "Energy" and stream['StreamBehavior'] == "BottomsLiquid":
                    python_code += f"{code}.ConnectReboilerDuty({connect_obj})  # ConnectReboilerDuty \n"
                    if (obj_name, connect_stream_id) in connections:
                        connections.remove((obj_name, connect_stream_id))

    for from_obj, to_obj in connections:
        from_tag = sim_objects.get(from_obj).get("code")
        to_tag = sim_objects.get(to_obj).get("code")
        python_code += f"sim.ConnectObjects({from_tag}.GraphicObject, {to_tag}.GraphicObject, -1, -1)  # {from_tag} to {to_tag}\n"

    python_code += (" # sim.AutoLayout()  \n"
                    " # Save the flowsheet \n")
    python_code += f"fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), \"gen_{file_name}.xml\")\n"

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
sim.GetSurface().AutoArrange()
PFDSurface = sim.GetSurface()
bmp = SKBitmap(2048, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
"""
    python_code += f"imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), \"img_{file_name}.png\")\n"

    python_code += """ 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

"""

    return python_code


def list_files_in_folder(folder_path):
    try:
        file_names = os.listdir(folder_path)  # Get all file and folder names
        file_names = [os.path.splitext(f)[0] for f in file_names if
                      os.path.isfile(os.path.join(folder_path, f))]  # Remove extensions
        return file_names
    except FileNotFoundError:
        print("Folder not found.")
        return []
    except PermissionError:
        print("Permission denied.")
        return []


# Example usage:
folder_path = "D:\\Masters\\Thesis\\PIGenerator\\src\\revers_engineering\\resources\\xml"
file_list = list_files_in_folder(folder_path)
# file_list = ["0"]
print(file_list)

for file in file_list:
    xml_path = folder_path + f"\\{file}.xml"
    compounds, simulation_objects, graphic_objects, connections = parse_xml(xml_path)
    python_script = generate_python_code(file, compounds, simulation_objects, graphic_objects, connections)

    # Save the generated Python script
    with open(f"{file}_generated_sim.py", "w") as f:
        f.write(python_script)

    print("Python script generated successfully.")

folder_path_dwxml = "D:\\Masters\\Thesis\\PIGenerator\\src\\revers_engineering\\resources\\dwxml"
dwxml_file_list = list_files_in_folder(folder_path_dwxml)
# file_list = ["0"]
print(dwxml_file_list)

for file in dwxml_file_list:
    xml_path = folder_path_dwxml + f"\\{file}.dwxml"
    compounds, simulation_objects, graphic_objects, connections = parse_xml(xml_path)
    python_script = generate_python_code(file, compounds, simulation_objects, graphic_objects, connections)

    # Save the generated Python script
    with open(f"{file}_generated_sim.py", "w") as f:
        f.write(python_script)

    print("Python script generated successfully.")
