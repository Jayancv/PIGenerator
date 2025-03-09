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
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding EnergyStream: EN_0b5f43af_e071_4741_ae3e_0b21a67e19b2
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 968, 267, "turbine energy")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_140efd4f_49b4_461a_a6a9_81e98adc17f1
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1079, 307, "spent steam")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(373.130065998883)  # Temperature in K
MaterialStream1.SetPressure(101345.854189936)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.251995806789775)  # Mass Flow in kg/s

# Adding CompressorExpander: TURB_b3b73be8_807f_4643_b26d_a865d67e8dbd
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1013, 303, "turbine")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_9ed21c9d_534c_4426_89c5_912c2f5e4f28
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 950, 302, "sheater outlet")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(560.928540306803)  # Temperature in K
MaterialStream2.SetPressure(1723658.45743874)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.251995806789775)  # Mass Flow in kg/s

# Adding EnergyStream: EN_6c892b7e_5a2a_4d6b_9f70_ccf5907e18c4
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 854, 268, "sheater energy")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding HeaterCooler: AQ_90233220_bf8f_4c6c_8f40_5d137e9df402
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 879, 307, "super heater ")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_3ba2e596_92fb_4124_bc67_adea90afa8ee
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 734, 271, "boiler energy ")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_afd64065_a2e7_4f28_897a_80f95e87041b
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 818, 308, "boiler outlet ")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(478.139642409703)  # Temperature in K
MaterialStream3.SetPressure(1723658.45743874)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.251995806789775)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_cdaf68ee_1f73_462d_b3ef_88fe7adb49b8
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 772, 315, "boiler")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding EnergyStream: EN_c5d895df_e0d1_40cd_8615_14c55ee3d160
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 608, 267, "pump energy ")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_554c7279_0c6e_4a07_b4e8_fdd6acaea531
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 725, 307, "pump outlet ")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(291.634557413948)  # Temperature in K
MaterialStream4.SetPressure(1723658.45743874)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.251995806789775)  # Mass Flow in kg/s

# Adding Pump: BB_f4047bb1_9c95_460d_936d_243d9933f87a
Pump1 = sim.AddObject(ObjectType.Pump, 662, 305, "PUMP")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_4972be49_2e76_4de9_9170_1b526714bfc9
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 606, 309, "feed water")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(291.483333333333)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.251995806789775)  # Mass Flow in kg/s

sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream2
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Pump1 to MaterialStream4
sim.ConnectObjects(MaterialStream3.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream3 to HeaterCooler1
sim.ConnectObjects(MaterialStream2.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream2 to AdiabaticExpanderCompressor1
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to EnergyStream1
sim.ConnectObjects(MaterialStream5.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream5 to Pump1
sim.ConnectObjects(EnergyStream3.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream3 to HeaterCooler2
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream1
sim.ConnectObjects(EnergyStream4.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream4 to Pump1
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream3
sim.ConnectObjects(MaterialStream4.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream4 to HeaterCooler2
sim.ConnectObjects(EnergyStream2.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # EnergyStream2 to HeaterCooler1
#sim.AutoLayout()
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_13.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_13.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

