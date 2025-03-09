import clr

dwsimpath = "C:\\Users\\jcvid\\AppData\\Local\\DWSIM\\"
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
air = sim.AvailableCompounds["Air"]
sim.SelectedCompounds.Add(air.Name, air)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)

# Adding Simulation Objects
# Adding MaterialStream: MAT_3b61dd0c_4dd9_43e0_89ab_a0298fa4548a
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1257, 382, "valve outlet")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(299.15)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.955185671683994)  # Mass Flow in kg/s

# Adding Valve: VALV_df26e96c_76bf_4781_a9af_d6366b4ed395
Valve1 = sim.AddObject(ObjectType.Valve, 1185, 380, "VALV-011")
Valve1 = Valve1.GetAsObject()

# Adding EnergyStream: EN_81c01335_514d_4e08_b1cb_058ceee22197
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 983, 342, "flash energy")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_72b85346_c84f_4f01_b829_9923f33a9dc6
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1188, 469, "liquid benzene")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(299.15)  # Temperature in K
MaterialStream2.SetPressure(14489475)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0448143283111749)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4aa39093_653c_4e27_a8d2_7b8bde060aa7
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1126, 337, "purified air")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(299.15)  # Temperature in K
MaterialStream3.SetPressure(14489475)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.955185671683994)  # Mass Flow in kg/s

# Adding Vessel: SEP_443953ab_5634_4b6f_93ae_b110cd98182c
Separator1 = sim.AddObject(ObjectType.Vessel, 1057, 384, "SEP-007")
Separator1 = Separator1.GetAsObject()

# Adding HeaterCooler: RESF_866cd520_75ec_45e5_b3ea_a62b8e3958e1
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 943, 415, "COOL-004")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_0a35e700_5e2a_40bc_8f85_77696635f840
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 998, 481, "cooler outlet")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(299.15)  # Temperature in K
MaterialStream4.SetPressure(14489475)  # Pressure in Pa
MaterialStream4.SetMassFlow(1)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_b94d9cad_c70e_478a_b96e_52615f040364
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 801, 409, "COMP-002")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding EnergyStream: EN_ffb6e465_11bd_4eb5_9f35_9e1398a977c3
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 897, 346, "cooler energy")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding EnergyStream: EN_8d9b7d3c_3b4f_4e01_a0d4_10918dd7e0a8
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 778, 348, "compresser energy")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_e70ce5c2_9c7f_4a3f_b3f4_1d093e1914dc
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 875, 398, "compressed gas")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(645.812238381866)  # Temperature in K
MaterialStream5.SetPressure(14489475)  # Pressure in Pa
MaterialStream5.SetMassFlow(1)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c7f25921_1bd6_4d9c_9682_2aab93d6389b
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 747, 408, "feed")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(299.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(1)  # Mass Flow in kg/s

sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream4
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.ConnectObjects(MaterialStream4.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream4 to Separator1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Separator1 to MaterialStream2
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Separator1 to MaterialStream3
sim.ConnectObjects(EnergyStream3.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream3 to AdiabaticExpanderCompressor1
sim.ConnectObjects(EnergyStream1.GraphicObject, Separator1.GraphicObject, -1, -1)  # EnergyStream1 to Separator1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Valve1 to MaterialStream1
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler1
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream5
sim.ConnectObjects(MaterialStream3.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream3 to Valve1
sim.ConnectObjects(MaterialStream6.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream6 to AdiabaticExpanderCompressor1
# sim.AutoLayout()
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_11.xml")
 
interf.SaveFlowsheet(sim, fileNameToSave, False)



# Export PFD image
clr.AddReference(dwsimpath + "SkiaSharp.dll")
clr.AddReference("System.Drawing")

from SkiaSharp import SKBitmap, SKImage, SKCanvas, SKEncodedImageFormat
from System.IO import MemoryStream
from System.Drawing import Image
from System.Drawing.Imaging import ImageFormat

# Render PFD to image
# sim.GetSurface().AutoArrange()
PFDSurface = sim.GetSurface()
bmp = SKBitmap(2024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_11.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

