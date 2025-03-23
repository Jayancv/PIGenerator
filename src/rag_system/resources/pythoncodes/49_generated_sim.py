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
toluene = sim.AvailableCompounds["Toluene"]
sim.SelectedCompounds.Add(toluene.Name, toluene)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
p_xylene = sim.AvailableCompounds["P-xylene"]
sim.SelectedCompounds.Add(p_xylene.Name, p_xylene)

# Adding Simulation Objects
# Adding MaterialStream: MAT_0b5bb0db_8056_4cee_8bb8_407cb445d2b0
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1036, 641, "Feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(358)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(93.5433)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_336db84d_2837_4004_8416_7fd9b954e299
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1180, 636, "Prefrac Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_cf621297_b496_4931_8f1e_7dd79cce35a8
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1248, 524, "top")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(341.074910069715)  # Temperature in K
MaterialStream2.SetPressure(37490.3)  # Pressure in Pa
MaterialStream2.SetMassFlow(54.7518912466797)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b5a19afd_119c_4796_b58a_76caeb91c38a
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1235, 774, "bottom")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(357.627770530868)  # Temperature in K
MaterialStream3.SetPressure(37490.3)  # Pressure in Pa
MaterialStream3.SetMassFlow(127.537702382368)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_d5b9705d_f826_49a1_bd17_71d824a70657
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1344, 636, "MainFrac Column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_3407cf59_db54_416a_8247_5d6e59f496d9
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1480, 474, "MSTR-007")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(358.532445089898)  # Temperature in K
MaterialStream4.SetPressure(37490.3)  # Pressure in Pa
MaterialStream4.SetMassFlow(57.3179695672696)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_89e4f3e7_d07b_40ed_92b6_99c76cfb0503
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1699, 561, "toluene")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(351.236698816543)  # Temperature in K
MaterialStream5.SetPressure(37490.3)  # Pressure in Pa
MaterialStream5.SetMassFlow(27.2123738886542)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6baf5cb4_9e2e_4514_be3c_15fa1b7a900a
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1559, 649, "MSTR-009")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(345.85604663582)  # Temperature in K
MaterialStream6.SetPressure(37490.3)  # Pressure in Pa
MaterialStream6.SetMassFlow(31.5470160722587)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_396c2b33_eca5_41b3_b13e_95bcd1ff3cf7
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1702, 799, "p-xylene")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(377.642576016356)  # Temperature in K
MaterialStream7.SetPressure(37490.3)  # Pressure in Pa
MaterialStream7.SetMassFlow(42.8375555588561)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e3532cb7_4d8f_4021_b732_324a382ceb39
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1708, 888, "Benzene")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(323.255628389303)  # Temperature in K
MaterialStream8.SetPressure(37490.3)  # Pressure in Pa
MaterialStream8.SetMassFlow(23.374678542009)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_3b81ee0a_5e2f_48f5_a090_25c6e7e07325
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1611, 650, "REC-012")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_0aa92161_3772_402e_bf76_9036cef8bfcf
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1633, 413, "to stage 1")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(345.85604663582)  # Temperature in K
MaterialStream9.SetPressure(37490.3)  # Pressure in Pa
MaterialStream9.SetMassFlow(31.5470160722587)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_d1e0f3d8_360d_44b2_90c6_88015da45288
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1620, 472, "REC-014")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_85d15868_7ab8_4614_b627_3782f6397df1
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1617, 730, "to stage 23")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(358.532445089898)  # Temperature in K
MaterialStream10.SetPressure(37490.3)  # Pressure in Pa
MaterialStream10.SetMassFlow(57.3179695672696)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream10.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream10 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream6 to Recycle1
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Recycle2 to MaterialStream10
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
# sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Recycle1 to MaterialStream9
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO2
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream4 to Recycle2
# sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO2
# sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_49.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_49.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

