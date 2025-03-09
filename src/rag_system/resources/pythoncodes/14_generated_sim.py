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
# Adding MaterialStream: MAT_1e138567_3a22_4a5d_8187_a324eb2cd0ab
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1344, 406, "Steam recycle")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(333.182186272117)  # Temperature in K
MaterialStream1.SetPressure(20000)  # Pressure in Pa
MaterialStream1.SetMassFlow(8)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_ff88e793_c7e8_4463_9497_8cfa3327d94b
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1294, 431, "recycle")
Recycle1 = Recycle1.GetAsObject()

# Adding EnergyStream: EN_815845e6_134c_452b_93c5_062904b9d67b
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1099, 693, "Pump Energy input")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_965b4681_1613_49c2_8fb5_1c677fc7c174
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1111, 579, "Water to boiler")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(316.177975935023)  # Temperature in K
MaterialStream2.SetPressure(10000000)  # Pressure in Pa
MaterialStream2.SetMassFlow(8)  # Mass Flow in kg/s

# Adding Pump: BB_2bc9df57_62c1_4307_ad3d_250cad4f38e4
Pump1 = sim.AddObject(ObjectType.Pump, 1178, 650, "PUMP")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_410f6f82_35ae_4bb5_b344_862d584f5c3d
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1430, 620, "Water")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(313.149999770313)  # Temperature in K
MaterialStream3.SetPressure(20000)  # Pressure in Pa
MaterialStream3.SetMassFlow(8)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ed77ffd1_740a_473d_a7d6_5a8c65b91302
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1488, 540, "Cooler Energy out")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding HeaterCooler: RESF_005ab90f_5f27_44d0_9cfb_d50bc4e22768
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1394, 511, "cooler")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_eda34c35_6077_4b05_845b_22af37a6972e
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 989, 615, "Boiler Energry input")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_49de711e_35c2_48d6_8bb8_f4b8b97ce8c6
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1247, 533, "Work Output")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_7b9f5de3_ed9e_4a90_a847_6aae5bf4ef3b
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1223, 450, "Expanded Steam out")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(333.182186272117)  # Temperature in K
MaterialStream4.SetPressure(20000)  # Pressure in Pa
MaterialStream4.SetMassFlow(8)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c83c1701_9c88_4c5d_b0e1_d1c74d2f6fdd
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1031, 460, "Steam")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(773.150000000053)  # Temperature in K
MaterialStream5.SetPressure(10000000)  # Pressure in Pa
MaterialStream5.SetMassFlow(8)  # Mass Flow in kg/s

# Adding CompressorExpander: TURB_bff6004a_2d70_4392_ac47_b0d2db58a84d
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1143, 482, "adiabatic turbine")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding HeaterCooler: AQ_8e0427c7_e3ba_4f99_a73d_837dcc90337f
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 1045, 547, "Boiler")
HeaterCooler2 = HeaterCooler2.GetAsObject()

sim.ConnectObjects(EnergyStream3.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream3 to HeaterCooler2
sim.ConnectObjects(MaterialStream1.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream1 to HeaterCooler1
sim.ConnectObjects(MaterialStream2.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream2 to HeaterCooler2
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
# sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to EnergyStream4
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream5
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream4
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(MaterialStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream3 to Pump1
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Pump1 to MaterialStream2
sim.ConnectObjects(MaterialStream5.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream5 to AdiabaticExpanderCompressor1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream3
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_14.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_14.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

