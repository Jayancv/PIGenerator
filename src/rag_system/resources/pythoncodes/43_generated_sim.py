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
ethylbenzene = sim.AvailableCompounds["Ethylbenzene"]
sim.SelectedCompounds.Add(ethylbenzene.Name, ethylbenzene)
p_diethylbenzene = sim.AvailableCompounds["P-diethylbenzene"]
sim.SelectedCompounds.Add(p_diethylbenzene.Name, p_diethylbenzene)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
ethylene = sim.AvailableCompounds["Ethylene"]
sim.SelectedCompounds.Add(ethylene.Name, ethylene)

# Adding Simulation Objects
# Adding MaterialStream: MAT_f999f7a9_a542_41fc_adf1_b26654d7d688
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1543, 914, "MSTR-032")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(381.465521088287)  # Temperature in K
MaterialStream1.SetPressure(2026500)  # Pressure in Pa
MaterialStream1.SetMassFlow(10.5061282787051)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_204d6bea_6e88_4b52_a30d_b7fbb76830e2
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1821, 693, "MSTR-022")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(313.37993449546)  # Temperature in K
MaterialStream2.SetPressure(30397.5)  # Pressure in Pa
MaterialStream2.SetMassFlow(21.0714833148668)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e769ae23_9250_440e_8a4e_3304421b649f
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1844, 885, "MSTR-023")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(376.40927910133)  # Temperature in K
MaterialStream3.SetPressure(30397.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(29.1031045574823)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2f456867_f0ea_46db_9c2d_cb13e8c4394f
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1444, 620, "MSTR-035")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(313.37993449546)  # Temperature in K
MaterialStream4.SetPressure(30397.5)  # Pressure in Pa
MaterialStream4.SetMassFlow(21.0714833148668)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e44e90c2_01c7_414a_9d20_de5a571476a9
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1553, 811, "MSTR-016")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(482.147762313586)  # Temperature in K
MaterialStream5.SetPressure(2026500)  # Pressure in Pa
MaterialStream5.SetMassFlow(50.174587872734)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9e3c817f_17f6_4e5a_a3bd_63444dd9a30c
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1685, 803, "MSTR-018")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(432)  # Temperature in K
MaterialStream6.SetPressure(1925175)  # Pressure in Pa
MaterialStream6.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f54a71e3_6f6c_4929_be3d_5ac352706a13
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1685, 835, "MSTR-019")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(432)  # Temperature in K
MaterialStream7.SetPressure(1925175)  # Pressure in Pa
MaterialStream7.SetMassFlow(50.174587872734)  # Mass Flow in kg/s

# Adding EnergyStream: EN_227fc5dd_e89b_45c3_be02_0c0b45d0a3d5
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1585, 859, "ESTR-020")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding RCT_Conversion: RC_daf81dc1_b0d2_4280_ad84_9428ee0a0e71
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1610, 794, "Reactor-2")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding NodeIn: MIST_80d68f2a_a4f2_44fe_9add_82f424981583
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1503, 801, "MIX-015")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_31b8e787_79f8_4be9_bafa_e357a17e5b1b
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1427, 809, "MSTR-013")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(434)  # Temperature in K
MaterialStream8.SetPressure(2026500)  # Pressure in Pa
MaterialStream8.SetMassFlow(39.6684595940289)  # Mass Flow in kg/s

# Adding EnergyStream: EN_9929ff67_b9c7_47c2_93aa_de1e0f54da75
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1329, 833, "ESTR-014")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_c29314b7_c62b_4912_ac92_94713fb5ffbb
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1427, 777, "MSTR-012")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(434)  # Temperature in K
MaterialStream9.SetPressure(2026500)  # Pressure in Pa
MaterialStream9.SetMassFlow(0)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_a814782f_e244_420b_bf29_f1deb35d4ac9
Reactor_Conversion2 = sim.AddObject(ObjectType.RCT_Conversion, 1353, 768, "Reactor-1")
Reactor_Conversion2 = Reactor_Conversion2.GetAsObject()

# Adding EnergyStream: EN_b5329802_bf1d_465d_bee4_052ead672ec7
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1269, 841, "ESTR-009")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_6eca0ed6_cdb5_495a_9981_0c924b1482c1
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1297, 789, "MSTR-008")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(753.717993125021)  # Temperature in K
MaterialStream10.SetPressure(2026500)  # Pressure in Pa
MaterialStream10.SetMassFlow(39.6684595940289)  # Mass Flow in kg/s

# Adding Pump: BB_8ffa81f9_e7eb_4d9c_9aa1_236702f07823
Pump1 = sim.AddObject(ObjectType.Pump, 1227, 786, "PUMP-007")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_9e76b45b_aaca_4e37_a64f_ab1c47f34075
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1164, 791, "MSTR-006")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(283.865363131088)  # Temperature in K
MaterialStream11.SetPressure(30397.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(39.6684595940289)  # Mass Flow in kg/s

# Adding NodeIn: MIST_2a58b235_cb82_4ee9_9aed_84eab45e85b1
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1114, 781, "MIX-005")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_d4e92a0c_0b5a_4e3e_a917_959d2a9a8062
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1045, 845, "ethylene")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(320)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(4.91412566666667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_97996395_5ed5_44f7_879f_a7294d4d5ecb
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1048, 775, "MSTR-003")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(311.28363980917)  # Temperature in K
MaterialStream13.SetPressure(30397.5)  # Pressure in Pa
MaterialStream13.SetMassFlow(34.7543339273622)  # Mass Flow in kg/s

# Adding NodeIn: MIST_0e4c5405_8c93_48a3_8b21_c3ec3a686b02
Mixer3 = sim.AddObject(ObjectType.NodeIn, 998, 765, "MIX-002")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_3fa1ce06_932e_46fd_bb5c_fd9ac9cbcc13
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 903, 805, "benzene")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(320)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(13.682969)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_e8222f7f_aa76_4306_af7d_401bfe15e97e
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1555, 643, "REC-034")
Recycle1 = Recycle1.GetAsObject()

# Adding EnergyStream: EN_dac8e4f5_d1e3_4471_93dd_88c4d52d5a82
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1729, 983, "ESTR-033")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding CapeOpenUO: COUO_d25436cb_90e7_45e5_953b_b310ddf9641a
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2082, 883, "DC-2")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_6f3ba021_1af3_4713_93be_7bc0eb60e27a
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2212, 802, "MSTR-027")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(335.0635422259)  # Temperature in K
MaterialStream15.SetPressure(10132.5)  # Pressure in Pa
MaterialStream15.SetMassFlow(18.5969776133465)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_06249523_7c93_416a_98b1_b403e4f8c7dc
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2019, 892, "MSTR-025")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(349.431911574445)  # Temperature in K
MaterialStream16.SetPressure(10132.5)  # Pressure in Pa
MaterialStream16.SetMassFlow(29.1031045574823)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_f9f1e5ea_bb1d_4ca3_958a_83b80c963851
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1754, 808, "DC-1")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding Valve: VALV_7e262375_7f7e_4206_a0f4_9086902a5108
Valve1 = sim.AddObject(ObjectType.Valve, 1969, 882, "VALV-024")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_8d607f93_efce_4214_b440_eb268c28e290
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2171, 955, "MSTR-028")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(379.83910838906)  # Temperature in K
MaterialStream17.SetPressure(10132.5)  # Pressure in Pa
MaterialStream17.SetMassFlow(10.5061269421075)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_b53cbb93_a982_41a9_8ae3_85e8e6e2aa8a
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1881, 956, "REC-029")
Recycle2 = Recycle2.GetAsObject()

# Adding Pump: BB_a5ccbace_f833_429e_910e_6f1d425f169e
Pump2 = sim.AddObject(ObjectType.Pump, 1686, 928, "PUMP-031")
Pump2 = Pump2.GetAsObject()

# Adding MaterialStream: MAT_6ce758ac_75b1_46ff_8ab5_d46307050143
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1798, 946, "MSTR-030")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(379.83910838906)  # Temperature in K
MaterialStream18.SetPressure(10132.5)  # Pressure in Pa
MaterialStream18.SetMassFlow(10.5061269421075)  # Mass Flow in kg/s

sim.ConnectObjects(EnergyStream1.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream1 to Reactor_Conversion1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Mixer1 to MaterialStream5
sim.ConnectObjects(MaterialStream18.GraphicObject, Pump2.GraphicObject, -1, -1)  # MaterialStream18 to Pump2
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(EnergyStream4.GraphicObject, Pump2.GraphicObject, -1, -1)  # EnergyStream4 to Pump2
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Mixer2 to MaterialStream11
sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream4 to Mixer3
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Pump1 to MaterialStream10
sim.ConnectObjects(MaterialStream16.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream16 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream15
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Recycle2 to MaterialStream18
sim.ConnectObjects(MaterialStream10.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # MaterialStream10 to Reactor_Conversion2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream7
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream6
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream2 to Recycle1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Valve1 to MaterialStream16
sim.ConnectObjects(EnergyStream2.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # EnergyStream2 to Reactor_Conversion2
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream8
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream2
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Mixer3 to MaterialStream13
sim.ConnectObjects(EnergyStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream3 to Pump1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream3
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream17
sim.ConnectObjects(MaterialStream14.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream14 to Mixer3
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream9
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream12 to Mixer2
sim.ConnectObjects(Pump2.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Pump2 to MaterialStream1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Recycle1 to MaterialStream4
sim.ConnectObjects(MaterialStream17.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream17 to Recycle2
sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO2
sim.ConnectObjects(MaterialStream5.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream5 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream11.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream11 to Pump1
sim.ConnectObjects(MaterialStream3.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream3 to Valve1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_43.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_43.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

