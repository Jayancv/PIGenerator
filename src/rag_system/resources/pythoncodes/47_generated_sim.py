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
tetrahydrofuran = sim.AvailableCompounds["Tetrahydrofuran"]
sim.SelectedCompounds.Add(tetrahydrofuran.Name, tetrahydrofuran)

# Adding Simulation Objects
# Adding EnergyStream: EN_b2c72d37_2932_419e_9df2_eebfe06e50a3
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1545, 660, "ESTR-023")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_f79c0e1c_7c25_4d5d_a4b4_e0dc1310a4c7
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1189, 838, "Feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(308.15)  # Temperature in K
MaterialStream1.SetPressure(110000)  # Pressure in Pa
MaterialStream1.SetMassFlow(11.8114)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_8e29d711_9ade_4d09_b486_7faab3debed4
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1964, 884, "REC-022")
Recycle1 = Recycle1.GetAsObject()

# Adding HeatExchanger: HE_a35d2b06_ad71_459f_b931_a0c9aae84cf3
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1296, 833, "HE-002")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_aa9a307d_4352_47ed_9ee7_97e5a75982e3
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1347, 708, "MSTR-003")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(346.375437173037)  # Temperature in K
MaterialStream2.SetPressure(110000)  # Pressure in Pa
MaterialStream2.SetMassFlow(11.8114)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_af2115e2_6c66_40c1_9b58_a4b130cb5ff0
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1397, 1003, "WATER")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(323.15)  # Temperature in K
MaterialStream3.SetPressure(110000)  # Pressure in Pa
MaterialStream3.SetMassFlow(9.41173433824789)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_480013d8_274c_4b63_ab69_a9c453effc90
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1859, 913, "MSTR-023")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(420.096605882176)  # Temperature in K
MaterialStream4.SetPressure(790000)  # Pressure in Pa
MaterialStream4.SetMassFlow(2.41193817315165)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_0966a6a0_b943_457a_b0a2_b1123768a9ef
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1386, 627, "COUO-006")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_2ed32f57_b434_47cf_a376_9fef3bd53b5c
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1456, 582, "MSTR-007")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(335.162473709511)  # Temperature in K
MaterialStream5.SetPressure(110000)  # Pressure in Pa
MaterialStream5.SetMassFlow(6.33208785563117)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7cf1c9de_9651_4d61_86d4_64205df72eea
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1474, 723, "MSTR-008")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(376.672015052139)  # Temperature in K
MaterialStream6.SetPressure(110000)  # Pressure in Pa
MaterialStream6.SetMassFlow(9.40914074777465)  # Mass Flow in kg/s

# Adding Pump: BB_62386509_14bd_4558_b7cf_e70c4eeab0e5
Pump1 = sim.AddObject(ObjectType.Pump, 1585, 606, "PUMP-022")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_e62728d2_73e2_452a_a6b9_fef819b52cb0
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1631, 807, "MSTR-010")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(335.267304463963)  # Temperature in K
MaterialStream7.SetPressure(790000)  # Pressure in Pa
MaterialStream7.SetMassFlow(6.33208785563117)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_86d38d72_3abc_4a23_91fe_7ddf78d9b596
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 1717, 802, "HE-012")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_5fe0fef9_85fe_4ebe_b7dc_99945b0eabaf
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1772, 687, "MSTR-013")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(361.803247997861)  # Temperature in K
MaterialStream8.SetPressure(790000)  # Pressure in Pa
MaterialStream8.SetMassFlow(6.33208785563117)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fd87c351_5fca_423b_90fd_92b3b7a87673
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1805, 1001, "THF")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(351.15)  # Temperature in K
MaterialStream9.SetPressure(790000)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.41763201167195)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_9fc22660_cd20_4a94_a293_a720f9aa24f1
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1835, 677, "COUO-015")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_80733362_ef47_4600_8b04_e4cd6dfb82a1
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1886, 552, "MSTR-016")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(407.132724859142)  # Temperature in K
MaterialStream10.SetPressure(790000)  # Pressure in Pa
MaterialStream10.SetMassFlow(3.92014982405005)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3f4e5425_4573_4970_a6fa_30290da3f29c
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1911, 784, "MSTR-017")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(420.096605882176)  # Temperature in K
MaterialStream11.SetPressure(790000)  # Pressure in Pa
MaterialStream11.SetMassFlow(2.41193817315165)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_29d29039_036a_437d_8351_a9f348782448
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1660, 509, "REC-018")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_08f2e4e6_c043_471b_b774_b6dd573ba1a5
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1637, 425, "MSTR-019")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(407.132724859142)  # Temperature in K
MaterialStream12.SetPressure(790000)  # Pressure in Pa
MaterialStream12.SetMassFlow(3.92014982405005)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_e4ff1847_5438_461a_b14b_a3c66987be74
Recycle3 = sim.AddObject(ObjectType.OT_Recycle, 1530, 811, "REC-020")
Recycle3 = Recycle3.GetAsObject()

# Adding MaterialStream: MAT_6feea41f_667e_4684_8e42_b515d928596a
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1454, 867, "MSTR-021")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(376.672015052139)  # Temperature in K
MaterialStream13.SetPressure(110000)  # Pressure in Pa
MaterialStream13.SetMassFlow(9.40914074777465)  # Mass Flow in kg/s

# Adding Valve: VALV_8613ca04_5c9f_45f7_b11a_55e6fb5ff76f
Valve1 = sim.AddObject(ObjectType.Valve, 1532, 425, "VALV-023")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_c7123ac9_df19_461f_83fd_b245e86dc963
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1299, 425, "MSTR-023")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(334.68647532809)  # Temperature in K
MaterialStream14.SetPressure(110000)  # Pressure in Pa
MaterialStream14.SetMassFlow(3.92982860485416)  # Mass Flow in kg/s

sim.ConnectObjects(Pump1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Pump1 to MaterialStream7
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle3.GraphicObject, -1, -1)  # MaterialStream6 to Recycle3
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream10
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Recycle1 to MaterialStream4
sim.ConnectObjects(MaterialStream11.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream11 to Recycle1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream6
sim.ConnectObjects(MaterialStream13.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream13 to HeatExchanger1
sim.ConnectObjects(MaterialStream5.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream5 to Pump1
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Recycle2 to MaterialStream12
sim.ConnectObjects(MaterialStream7.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream7 to HeatExchanger2
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO1
sim.ConnectObjects(MaterialStream10.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream10 to Recycle2
sim.ConnectObjects(MaterialStream12.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream12 to Valve1
# sim.ConnectObjects(MaterialStream14.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream14 to CapeOpenUO1
sim.ConnectObjects(Recycle3.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Recycle3 to MaterialStream13
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream2
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Valve1 to MaterialStream14
sim.ConnectObjects(MaterialStream1.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream1 to HeatExchanger1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream3
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream9
sim.ConnectObjects(MaterialStream4.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream4 to HeatExchanger2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream11
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream8
sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_47.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_47.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

