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
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_7e6aedb2_dee7_415d_8d36_dddb68b30b9f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 898, 408, "compressor inlet")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(230.945239794662)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(1)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_1e6aa758_0559_4172_9425_8127e926bfb9
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 974, 406, "compressor")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_85d7e7e1_8f20_4d54_b8af_b181814c6f62
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1052, 406, "condenser inlet")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(305.133011228293)  # Temperature in K
MaterialStream2.SetPressure(960000)  # Pressure in Pa
MaterialStream2.SetMassFlow(1)  # Mass Flow in kg/s

# Adding EnergyStream: EN_64053e24_f267_4a41_be33_6647b65ae5fd
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 925, 345, "compressor energy")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_c29c0117_f08b_4b8b_bc4c_cdaf61c8dd59
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1486, 409, "evaporator outlet")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(230.945239770961)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(1)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_e2f6544f_8ea3_479f_87ac_f015577e23a3
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1130, 405, "condenser")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_73b37f6b_41af_4f8d_ad5d_b26ee334fce7
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1194, 409, "valve inlet")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.14922956536)  # Temperature in K
MaterialStream4.SetPressure(960000)  # Pressure in Pa
MaterialStream4.SetMassFlow(1)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4aee5837_5c07_4a7f_8df1_6c97b8fa6288
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1056, 349, "condenser energy")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding Valve: VALV_88668760_2570_4bfd_b20e_d301df35a129
Valve1 = sim.AddObject(ObjectType.Valve, 1262, 408, "valve")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_ef4b2ef4_2859_41c3_8a72_f29024788fb3
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1329, 409, "evaporator inlet ")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(230.945239794662)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_a4a49ff5_0c52_48f6_bfce_a04c33ff7a2d
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 1396, 408, "evaporator")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding EnergyStream: EN_abddaf55_af50_4929_8c38_1d4560f23da3
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1341, 353, "evaporator energy")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding OT_Recycle: REC_ee1c92f2_5ccc_4f8d_9f67_a30e06085673
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 990, 533, "REC-012")
Recycle1 = Recycle1.GetAsObject()

sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream4
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream3
sim.ConnectObjects(MaterialStream3.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream3 to Recycle1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Valve1 to MaterialStream5
sim.ConnectObjects(EnergyStream3.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream3 to HeaterCooler2
sim.ConnectObjects(MaterialStream2.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream2 to HeaterCooler1
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler2
sim.ConnectObjects(EnergyStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream2
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_16.xml")
 
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
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_16.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

