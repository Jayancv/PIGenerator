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
dimethyl_sulfoxide = sim.AvailableCompounds["Dimethyl sulfoxide"]
sim.SelectedCompounds.Add(dimethyl_sulfoxide.Name, dimethyl_sulfoxide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
isopropanol = sim.AvailableCompounds["Isopropanol"]
sim.SelectedCompounds.Add(isopropanol.Name, isopropanol)

# Adding Simulation Objects
# Adding OT_Recycle: REC_d6650f28_e978_46a1_ad6d_548636522abe
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1444, 521, "REC-014")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_9acca7e7_468c_4b1c_8277_bf2a6f5a33ef
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1366, 425, "WATER")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(372.611867924684)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.258510349699887)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_664cde9f_9de7_45cc_8bd3_ec831559f69e
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1271, 471, "DISTI")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_11bbd441_a255_458c_867c_3c8f5d3f4bf1
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1367, 521, "DMSO")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(462.383060665187)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(2.21713992099181)  # Mass Flow in kg/s

# Adding EnergyStream: EN_11d0c45f_79a3_496d_88e5_6e7b9872f126
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 930, 558, "ESTR-007")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_4df33c49_33cb_4bda_b325_5fa8f3ce587f
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1021, 528, "ENTRAINER")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(345.15)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(2.22462659474074)  # Mass Flow in kg/s

# Adding Cooler: RESF_ca95ac59_b11b_4df8_99c6_d258b4f64430
Cooler1 = sim.AddObject(ObjectType.Cooler, 961, 499, "COOL-005")
Cooler1 = Cooler1.GetAsObject()

# Adding NodeIn: MIST_16c906e4_146b_407a_b582_641715a796d6
Mixer1 = sim.AddObject(ObjectType.NodeIn, 847, 502, "MIX-004")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_0601c838_c76d_4230_a87d_0a5ba5ac682c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 766, 623, "MAKE UP")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(469.76)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(3.5941364E-07)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6f7316df_a697_45c6_b09e_1fc01293190f
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1111, 605, "RECYCLE")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(469.76)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(2.2246262353271)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_52dd04fe_6260_4021_8846_80e48653131a
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 903, 502, "MIX OUT")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(469.76)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(2.22462659474074)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b127aa98_d9e6_44e7_a894_b5ad5743be61
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1019, 427, "FEED")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(352.2)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.084875)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_cbc5a723_6351_4185_834e_45f97a86a1a9
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1103, 458, "EXTRAC COLUMN")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_51052c3d_86ec_4814_a157_c3575fb8b7a4
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1252, 390, "PURE ISOPROPANOL")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(355.498468937006)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.833851324049013)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1e720209_f0b3_4a85_ac9c_d83aba316e7a
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1197, 506, "DMSO WATER MIX")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(415.636715298375)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.4756502706917)  # Mass Flow in kg/s

sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Mixer1 to MaterialStream6
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream5 to Mixer1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream9
sim.ConnectObjects(MaterialStream6.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream6 to Cooler1
sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO1
# sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO2
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream2 to Recycle1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle1 to MaterialStream5
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Cooler1 to MaterialStream3
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_36.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_36.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

