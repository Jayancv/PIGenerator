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
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_dab6b1b5_b92b_4f29_be0e_d24315e02e67
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1564, 411, "dehumidified air")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(293.15)  # Temperature in K
MaterialStream1.SetPressure(100000.026040658)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.995318298020669)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b0b3121f_16a8_481b_af4d_9a6d426994ab
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1354, 517, "heavy liquid")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(293.15)  # Temperature in K
MaterialStream2.SetPressure(274999.973523717)  # Pressure in Pa
MaterialStream2.SetMassFlow(0)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3de91d9f_7336_46e5_af0b_fbad1b3be8be
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1109, 505, "ESTR-010")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_46d048d4_755a_4fb7_98aa_d4b4c22af3eb
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1363, 463, "removed water")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(293.15)  # Temperature in K
MaterialStream3.SetPressure(274999.973523717)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.00468170198690697)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_59aee98e_86db_4c60_b2c2_5d462ce8958c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1362, 403, "gas stream")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(293.15)  # Temperature in K
MaterialStream4.SetPressure(274999.973523717)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.995318298020669)  # Mass Flow in kg/s

# Adding Vessel: SEP_9fc4dbf1_0fae_4767_9e62_2a46855a6604
Separator1 = sim.AddObject(ObjectType.Vessel, 1180, 423, "SEP-007")
Separator1 = Separator1.GetAsObject()

# Adding EnergyStream: EN_4c19c146_2472_4683_a9bf_9c36b14fe112
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1034, 491, "ESTR-006")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_199b68dd_42bf_40b7_9c4f_068753b12ee2
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 893, 445, "compressed humid air")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(355.154570004591)  # Temperature in K
MaterialStream5.SetPressure(274999.973523717)  # Pressure in Pa
MaterialStream5.SetMassFlow(1)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_b56262ab_52c8_45e2_8bd6_a98b7d39362c
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 767, 439, "compressor")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_9cce4842_de99_4d92_9cdb_6c37a91f10e0
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 631, 442, "Feed")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(293.15)  # Temperature in K
MaterialStream6.SetPressure(100000.026040658)  # Pressure in Pa
MaterialStream6.SetMassFlow(1)  # Mass Flow in kg/s

# Adding EnergyStream: EN_aeaf438a_8ecc_4608_9fe4_e50d2dbd8e04
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 709, 485, "ESTR-003")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding HeaterCooler: RESF_e74a87cd_e036_442f_bfba_e6c8fd6f22dd
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 979, 443, "cooler")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_eaa4b644_d703_4bcd_9871_65999ed88cfd
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1077, 446, "cooled air")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(293.15)  # Temperature in K
MaterialStream7.SetPressure(274999.973523717)  # Pressure in Pa
MaterialStream7.SetMassFlow(1)  # Mass Flow in kg/s

# Adding Valve: VALV_49ce35e1_cadd_4096_b355_b7c6420e2da6
Valve1 = sim.AddObject(ObjectType.Valve, 1475, 405, "VALV-013")
Valve1 = Valve1.GetAsObject()

sim.ConnectObjects(MaterialStream6.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream6 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler1
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Separator1 to MaterialStream2
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream5
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Separator1 to MaterialStream4
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Valve1 to MaterialStream1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Separator1 to MaterialStream3
sim.ConnectObjects(EnergyStream3.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream3 to AdiabaticExpanderCompressor1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream7
sim.ConnectObjects(MaterialStream7.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream7 to Separator1
sim.ConnectObjects(EnergyStream1.GraphicObject, Separator1.GraphicObject, -1, -1)  # EnergyStream1 to Separator1
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_18.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_18.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

