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
monoethanolamine = sim.AvailableCompounds["Monoethanolamine"]
sim.SelectedCompounds.Add(monoethanolamine.Name, monoethanolamine)
ethylene_oxide = sim.AvailableCompounds["Ethylene oxide"]
sim.SelectedCompounds.Add(ethylene_oxide.Name, ethylene_oxide)
triethanolamine = sim.AvailableCompounds["Triethanolamine"]
sim.SelectedCompounds.Add(triethanolamine.Name, triethanolamine)
ammonia = sim.AvailableCompounds["Ammonia"]
sim.SelectedCompounds.Add(ammonia.Name, ammonia)
diethanolamine = sim.AvailableCompounds["Diethanolamine"]
sim.SelectedCompounds.Add(diethanolamine.Name, diethanolamine)

# Adding Simulation Objects
# Adding MaterialStream: MAT_6cd3ae01_8002_40c8_851e_79d33790679f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2577, 1092, "effluent2")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(300)  # Temperature in K
MaterialStream1.SetPressure(301325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.252274167565511)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_273343c5_81bf_4559_820b_2c0973aad07d
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2366, 871, "Nh3 recycle")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(300)  # Temperature in K
MaterialStream2.SetPressure(301325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.00561696030670561)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5ed92a76_587d_46ed_b974_a59658be5697
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 3155, 1047, "Triethanolamine")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(609.189229046041)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.0433465953055814)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d3752b9e_dee8_4721_9b31_48458a6afcef
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 3138, 949, "Diethanolamine")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(541.234437392608)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.113318092775104)  # Mass Flow in kg/s

# Adding NodeOut: DIV_5c84398c_f746_4bb0_bc1c_2df713243365
Splitter1 = sim.AddObject(ObjectType.NodeOut, 2518, 814, "spliter")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_1e4e0dd0_3357_4136_91dc_988a3e265a17
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2918, 1181, "Di,triethanolamine")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(548.613969299583)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.156664688080645)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_84e5e155_04fd_4b6d_9cf7_c382e01794b1
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 3147, 870, "Monoehanolamine")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(443.405608152693)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.0695969585521622)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_adabffe0_6bd6_4f92_a224_57e986576c46
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2709, 777, "purge stream")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(309.426799721351)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.00546262934798538)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_365274f2_65f5_4df6_aa6f_9b30925ab834
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1968, 823, "Mixed recycle stream")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(305.198457847323)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.0261668516634125)  # Mass Flow in kg/s

# Adding NodeIn: MIST_14faec01_b727_4851_b620_786c258ac4b2
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2210, 827, "Mixer2")
Mixer1 = Mixer1.GetAsObject()

# Adding OT_Recycle: REC_1ae15fef_429a_48c5_aea9_ef612fafcd68
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1740, 824, "Recycle block")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_e38b2264_b99a_4ad6_9396_c0de6132798f
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1574, 826, "Recycle stream")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(305.198457847323)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.0261668516634125)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_bded3a61_b7fd_4165_9a73_d42d7c7cdb22
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2644, 1107, "Water stripper tower")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_70d6d31e_8b30_4718_9002_b1894e756031
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2070, 1083, "feed")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(303.15)  # Temperature in K
MaterialStream10.SetPressure(600000)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.257891124132946)  # Mass Flow in kg/s

# Adding EnergyStream: EN_85fcc60d_816a_4dd9_87a3_c065cdd84c87
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2014, 1258, "E3")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding Cooler: RESF_1dbeaa00_2859_4542_bea0_f5dcb64ed028
Cooler1 = sim.AddObject(ObjectType.Cooler, 1998, 1186, "Cooler1")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_0d5710c5_5c79_4632_ac2f_e0221caa861c
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1560, 1265, "ethylene oxide")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(298.15)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.1835525)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f4d11026_a03b_4f57_ac85_d6489f45858d
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1430, 1198, "Ammonia")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(303.15)  # Temperature in K
MaterialStream12.SetPressure(100000)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.0481283333333333)  # Mass Flow in kg/s

# Adding Compressor: COMP_f2c425b4_be25_45ac_80c1_199d29981a8a
Compressor1 = sim.AddObject(ObjectType.Compressor, 1653, 1235, "compressor")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_7cb48c82_7a7f_4cd8_9080_6bbb14c6e590
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1771, 1147, "compressed feed")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(408.394173890431)  # Temperature in K
MaterialStream13.SetPressure(601325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.1835525)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_209ff67b_60a2_4224_ad64_f48cf82d489f
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1580, 1012, "mix recycle+feed")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(303.783349859011)  # Temperature in K
MaterialStream14.SetPressure(100000)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.0743386241329464)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_cc819275_1e3f_4ee4_bf56_18706758f8ad
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1779, 1002, "feed stream")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(384.335289979291)  # Temperature in K
MaterialStream15.SetPressure(600000)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.0743386241329464)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_39009511_6fee_4017_b54a_3ecfd09a07b9
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1939, 1109, "Mixed feed")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(370.332399095903)  # Temperature in K
MaterialStream16.SetPressure(600000)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.257891124132946)  # Mass Flow in kg/s

# Adding EnergyStream: EN_e1457f0a_72cb_4bb1_ac8a_5b1e4cec186f
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1650, 1318, "E1")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding Pump: BB_221d9586_9135_4d59_ab77_0bd6f5a25707
Pump1 = sim.AddObject(ObjectType.Pump, 1687, 1010, "Pump")
Pump1 = Pump1.GetAsObject()

# Adding NodeIn: MIST_bf9a3a07_c4a4_4b65_883a_ded540183570
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1483, 1105, "Mixer1")
Mixer2 = Mixer2.GetAsObject()

# Adding EnergyStream: EN_9ee0ceaf_7e07_4973_911e_3c75126760a2
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1676, 1078, "E2")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding RCT_CSTR: CSTR_7a9ea56f_8d8d_4cde_917b_d46d8971b40d
Reactor_CSTR1 = sim.AddObject(ObjectType.RCT_CSTR, 2141, 1061, "cont. stirred reactor")
Reactor_CSTR1 = Reactor_CSTR1.GetAsObject()

# Adding NodeIn: MIST_a9e96241_ec9c_4e90_a800_650bc4889b32
Mixer3 = sim.AddObject(ObjectType.NodeIn, 1861, 1110, "Mixer2")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_00ff88fd_03ff_42e1_aa78_9eb91d4fa1c6
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2186, 966, "Nulll")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(373.15)  # Temperature in K
MaterialStream17.SetPressure(600000)  # Pressure in Pa
MaterialStream17.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_daee7ce4_87c8_4333_81b6_eb0aa01fe7b0
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2243, 1086, "product effluent")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(373.15)  # Temperature in K
MaterialStream18.SetPressure(600000)  # Pressure in Pa
MaterialStream18.SetMassFlow(0.257891124132946)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5632499a_d187_4641_861a_a8685ade70f2
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2146, 1166, "E4")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding CapeOpenUO: COUO_0d25f050_c82f_48ed_aa2d_9bdf0f8b0f2e
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 2478, 1082, "Flash tower")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_b0ba43bf_0da1_4f9a_8063_20e8890ea9d7
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2609, 833, "H2O stream")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(309.426799721351)  # Temperature in K
MaterialStream19.SetPressure(101325)  # Pressure in Pa
MaterialStream19.SetMassFlow(0.0260125207046923)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2f93be13_afa3_4fcc_8a7b_2dc51820b67c
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2774, 1090, "Product stream")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(473.333540485653)  # Temperature in K
MaterialStream20.SetPressure(101325)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.226261646860804)  # Mass Flow in kg/s

# Adding Cooler: RESF_a92c12fd_0fc7_43b3_9183_38ffa4440f9c
Cooler2 = sim.AddObject(ObjectType.Cooler, 2310, 1179, "cooler2")
Cooler2 = Cooler2.GetAsObject()

# Adding MaterialStream: MAT_114d3744_f3b2_4641_9563_1a52c0615be6
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 2382, 1089, "effluent")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(300.15)  # Temperature in K
MaterialStream21.SetPressure(300000)  # Pressure in Pa
MaterialStream21.SetMassFlow(0.257891124132946)  # Mass Flow in kg/s

# Adding EnergyStream: EN_797f2d73_42d9_4832_b43c_eceeef3faf8d
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2301, 1248, "E5")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_92eb4103_f800_4e7e_87d3_cb73ecf1901a
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 2374, 822, "H2O recycle")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(309.426799721351)  # Temperature in K
MaterialStream22.SetPressure(101325)  # Pressure in Pa
MaterialStream22.SetMassFlow(0.0205498913567069)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_94980dab_4ce7_44fc_9aae_f60a787369ed
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 2873, 1078, "comple column (mono)")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding CapeOpenUO: COUO_65845c63_69dd_465a_9564_7ddfd426e1ed
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 2994, 1170, "complex column2")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()

sim.ConnectObjects(MaterialStream16.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream16 to Cooler1
sim.ConnectObjects(MaterialStream14.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream14 to Pump1
sim.ConnectObjects(MaterialStream22.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream22 to Mixer1
sim.ConnectObjects(MaterialStream19.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream19 to Splitter1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream6
sim.ConnectObjects(MaterialStream8.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream8 to Recycle1
sim.ConnectObjects(MaterialStream20.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream20 to CapeOpenUO3
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream5
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream1
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Compressor1 to MaterialStream13
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # Cooler2 to EnergyStream5
sim.ConnectObjects(EnergyStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream3 to Pump1
sim.ConnectObjects(MaterialStream11.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream11 to Compressor1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Cooler1 to MaterialStream10
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream13 to Mixer3
sim.ConnectObjects(MaterialStream10.GraphicObject, Reactor_CSTR1.GraphicObject, -1, -1)  # MaterialStream10 to Reactor_CSTR1
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Pump1 to MaterialStream15
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream3
sim.ConnectObjects(MaterialStream21.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream21 to CapeOpenUO2
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO4
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream2
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Splitter1 to MaterialStream22
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_CSTR1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_CSTR1
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream12 to Mixer2
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Cooler2 to MaterialStream21
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream19
sim.ConnectObjects(EnergyStream2.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream2 to Compressor1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Splitter1 to MaterialStream7
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream15 to Mixer3
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Mixer1 to MaterialStream8
sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream9 to Mixer2
sim.ConnectObjects(MaterialStream18.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream18 to Cooler2
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream20
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Mixer3 to MaterialStream16
sim.ConnectObjects(Reactor_CSTR1.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Reactor_CSTR1 to MaterialStream17
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Recycle1 to MaterialStream9
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Mixer2 to MaterialStream14
sim.ConnectObjects(Reactor_CSTR1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Reactor_CSTR1 to MaterialStream18
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_62.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_62.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

