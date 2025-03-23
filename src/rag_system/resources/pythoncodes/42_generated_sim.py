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
glycerol = sim.AvailableCompounds["Glycerol"]
sim.SelectedCompounds.Add(glycerol.Name, glycerol)
ethanol = sim.AvailableCompounds["Ethanol"]
sim.SelectedCompounds.Add(ethanol.Name, ethanol)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_3b563062_06ca_4e32_ad08_dca65519852b
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 866, 438, "ENTRAINER")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(353.15)  # Temperature in K
MaterialStream1.SetPressure(2026.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.15009410816975)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dcbe5f01_e09d_4f8e_8255_aed388836fb4
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 949, 494, "GLY MAKEUP")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(353.15)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0011511725)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1bdef212_2558_454f_9f31_f7e20d5e53e8
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1057, 445, "GLYCEROL")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(353.15)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.15124528066975)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_59f9cdea_69a0_4782_a943_e2cf2b049493
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1050, 516, "AZEO FEED")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(351.537192999817)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.19397388888889)  # Mass Flow in kg/s

# Adding NodeIn: MIST_efac62a1_1a8a_4f76_b892_a2a097dffad2
Mixer1 = sim.AddObject(ObjectType.NodeIn, 988, 445, "MIX-004")
Mixer1 = Mixer1.GetAsObject()

# Adding CapeOpenUO: COUO_8157b6ab_08e5_45fb_89db_600c67c3bd81
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1130, 484, "ExDistiCol")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_973d6ec3_d1d6_4187_a29d_6ba4d6f6b2e6
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1233, 449, "PURE ETHANOL")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(351.584607350521)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.1719801354516)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_83e2f7df_c94a_4cf2_8884_caec95b320ab
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1213, 535, "ERC FEED")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(448.329460816125)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(1.17323903410641)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_40427f29_d6fc_41db_83f2_430d04ea62ac
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1310, 488, "ERC")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_2f30dff7_bb97_4e71_9c46_b5da4d1b434f
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1394, 429, "WATER")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(286.651351451472)  # Temperature in K
MaterialStream7.SetPressure(2026.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.0250916815660259)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0d6cbf54_d328_422c_8e63_fa08675f3810
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1397, 521, "ENTRAINER1")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(449.438701362679)  # Temperature in K
MaterialStream8.SetPressure(2026.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(1.14814735254011)  # Mass Flow in kg/s

# Adding Cooler: RESF_fb39816e_e50e_4161_b508_8dda98dfaa3f
Cooler1 = sim.AddObject(ObjectType.Cooler, 1469, 519, "COOL-011")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_c946d828_bdf4_4294_955d_44a4aa91ef02
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1443, 679, "ENTRAINER RECYCLE")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(353.15)  # Temperature in K
MaterialStream9.SetPressure(2026.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.14814735254011)  # Mass Flow in kg/s

# Adding EnergyStream: EN_1dc0fe79_328c_4ddf_a258_9e604237d19c
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1384, 583, "ESTR-013")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding OT_Recycle: REC_fb36368a_b730_49fd_bf37_88dba62c7af1
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 840, 627, "REC-014")
Recycle1 = Recycle1.GetAsObject()

sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Cooler1 to MaterialStream9
sim.ConnectObjects(MaterialStream9.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream9 to Recycle1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Mixer1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream6
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(MaterialStream8.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream8 to Cooler1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
# sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_42.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_42.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

