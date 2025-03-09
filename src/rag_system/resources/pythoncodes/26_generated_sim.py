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
propylene_oxide_1_2 = sim.AvailableCompounds["1,2-propylene oxide"]
sim.SelectedCompounds.Add(propylene_oxide_1_2.Name, propylene_oxide_1_2)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
propanediol_1_2 = sim.AvailableCompounds["2,5-dimethylhexane"]
sim.SelectedCompounds.Add(propanediol_1_2.Name, propanediol_1_2)

# Adding Simulation Objects
# Adding EnergyStream: EN_1596af9c_523c_409d_a7d0_94b00d64648e
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 3523, 1742, "Q-B4")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_40f57693_50f7_4de0_8f68_db78bbbdab6b
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 3521, 1695, "S7")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(453.466558822539)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.347209845456039)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_35fac29a_e533_4386_a212_b087bbf7160f
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 3452, 1698, "Cooler-B2")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_ce6800b4_b1ea_43f3_9b33_5a4c52df683f
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 3515, 1611, "Q-B3")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_1f2da2c2_0406_4230_bf0f_1a4e45a70002
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 3534, 1566, "S6")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(338.721281108191)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0873527835244609)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_226644a6_bd42_40b2_ab5d_4f72ce6cbe6e
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 3459, 1569, "Cooler-B1")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding EnergyStream: EN_04d1fa56_aedd_4164_b442_f87e8ec67daf
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 3533, 1335, "Q-A4")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_54aff2bf_d41e_46f3_8bc6_b820b02aa4a3
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 3558, 1280, "S-7")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(298.15)  # Temperature in K
MaterialStream3.SetPressure(100000)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.348060793466722)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_bf5fcf4d_431a_4bfe_a004_d84a5ab9e1d2
HeaterCooler3 = sim.AddObject(ObjectType.Heater, 3481, 1295, "Cooler-A2")
HeaterCooler3 = HeaterCooler3.GetAsObject()

# Adding EnergyStream: EN_38316ccd_5a44_4166_8c01_3cdc6d984d34
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 3554, 1169, "Q-A3")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_b517dcad_7070_40c9_83d5_1d3d2c5b6808
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 3578, 1116, "S-6")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(100000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0865351720010647)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_ff84afbf_91c7_4eb6_8ebe_3478135ae2ca
HeaterCooler4 = sim.AddObject(ObjectType.Heater, 3511, 1114, "Cooler-A1")
HeaterCooler4 = HeaterCooler4.GetAsObject()

# Adding MaterialStream: MAT_e6412512_0628_4ae2_8c56_1d1a1d66dcea
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 3381, 1570, "Distillate-B")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(338.721281108151)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0873527835244609)  # Mass Flow in kg/s

# Adding EnergyStream: EN_488d0fbc_d46d_458e_8d9c_bb553e4b64a6
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 3375, 1652, "R-Duty-B")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_93f99a56_e756_4664_bc6f_fbf7d8973c7f
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 3368, 1710, "Bottoms-B")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(453.466558821147)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.347209845456039)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ddcb11e8_37d8_49ca_bf88_5942d23ae538
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 3423, 1527, "C-Duty-B")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding DistillationColumn: DC_cb534760_e104_44d1_88e3_a196e3124b36
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 3167, 1536, "Rigorous-Distil")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_a26382ad_3640_46d4_be37_29b30b9d4b08
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2953, 1639, "Q-B2")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding EnergyStream: EN_e08e04f6_6876_49ae_b469_1ba7b2e6ef94
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 3392, 1259, "R-Duty-A")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding EnergyStream: EN_74d40376_b376_418d_87c3_cf54e21dfcb3
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 3395, 1120, "C-Duty-A")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_4ffc6585_61ba_44f5_91a0_a6545ff45abc
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 3391, 1315, "Bottoms-A")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(449.640217143429)  # Temperature in K
MaterialStream7.SetPressure(100000)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.348060793466722)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_10473610_44c6_4e16_8e77_2b02961689f5
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 3396, 1181, "Distillate-A")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(337.901504682844)  # Temperature in K
MaterialStream8.SetPressure(100000)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.0865351720010647)  # Mass Flow in kg/s

# Adding ShortcutColumn: SC_2417c193_4b42_447a_a1aa_a589988aa13b
ShortcutColumn1 = sim.AddObject(ObjectType.ShortcutColumn, 3177, 1120, "Short-Cut-Distill")
ShortcutColumn1 = ShortcutColumn1.GetAsObject()

# Adding MaterialStream: MAT_b7e60af8_81fd_441a_85a1_aa37e5fce902
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 3084, 1617, "S5-L")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(473.15)  # Temperature in K
MaterialStream9.SetPressure(100000)  # Pressure in Pa
MaterialStream9.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f4321245_55af_4bcc_81fd_edcb9a4eaa82
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 3092, 1560, "S5-V")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(473.15)  # Temperature in K
MaterialStream10.SetPressure(100000)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_e2d1e17c_cd42_46aa_85e8_4abf18663751
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 2992, 1553, "Conversion-Reactor-B")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding EnergyStream: EN_927c3464_cc9c_46cd_a937_7eb5a7210ad2
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 2805, 1605, "Q-B1")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding MaterialStream: MAT_22494637_505b_4738_bd13_4a2faf9a760f
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2932, 1559, "S4")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(473.15)  # Temperature in K
MaterialStream11.SetPressure(100000)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_cb3a06f0_af05_46b8_bd96_cc14f76cb9e4
HeaterCooler5 = sim.AddObject(ObjectType.Heater, 2845, 1541, "Heater-B")
HeaterCooler5 = HeaterCooler5.GetAsObject()

# Adding MaterialStream: MAT_e1ccf836_7659_4ac7_a94f_8366abff7ee9
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2787, 1546, "S3")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(298.15)  # Temperature in K
MaterialStream12.SetPressure(100000)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding NodeIn: MIST_c2baff87_0b22_47e7_b709_0eed8ff6009c
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2716, 1544, "Mixer-B")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_e579e2c2_bae3_48b3_9395_69b678f3a2a7
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2637, 1608, "S2")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(298.15)  # Temperature in K
MaterialStream13.SetPressure(100000)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.102888055555556)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6aa6cd5f_af3f_488e_95ce_4cd91024d583
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2646, 1503, "S1")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(298.15)  # Temperature in K
MaterialStream14.SetPressure(100000)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.331704166666667)  # Mass Flow in kg/s

# Adding EnergyStream: EN_a88cd1b9_5d04_4d82_90d2_8658246168af
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 2792, 1266, "Q-A1")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding HeaterCooler: AQ_d228997c_1a3c_4ac1_8d93_a73f5167c3d6
HeaterCooler6 = sim.AddObject(ObjectType.Heater, 2849, 1191, "Heater-A")
HeaterCooler6 = HeaterCooler6.GetAsObject()

# Adding MaterialStream: MAT_4630b8b4_606e_4598_82af_5c3b0afec306
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2788, 1200, "S-3")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(298.15)  # Temperature in K
MaterialStream15.SetPressure(100000)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding NodeIn: MIST_c18f0869_2d7b_402d_ae94_3beb667b1863
Mixer2 = sim.AddObject(ObjectType.NodeIn, 2726, 1203, "Mixer-A")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_a4fe6b55_ef69_4516_923c_d27717d37dac
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2651, 1221, "S-2")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(298.15)  # Temperature in K
MaterialStream16.SetPressure(100000)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.102888055555556)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_51c4d7c7_84de_431b_bc55_c13e8c09b0a7
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2652, 1153, "S-1")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(298.15)  # Temperature in K
MaterialStream17.SetPressure(100000)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.331704166666667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c7443e02_2516_424f_9de0_c1159857419d
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2931, 1200, "S-4")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(473.15)  # Temperature in K
MaterialStream18.SetPressure(100000)  # Pressure in Pa
MaterialStream18.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_1ff8206d_c179_4e7b_ba66_895219d43a00
Reactor_Conversion2 = sim.AddObject(ObjectType.RCT_Conversion, 2990, 1189, "Conversion-Reactor-A")
Reactor_Conversion2 = Reactor_Conversion2.GetAsObject()

# Adding MaterialStream: MAT_e0b1c5a8_874b_4ad1_a075_da6396c7462b
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 3086, 1192, "S-5-V")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(473.15)  # Temperature in K
MaterialStream19.SetPressure(100000)  # Pressure in Pa
MaterialStream19.SetMassFlow(0.434592222222223)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5d533df7_3ba8_4717_bb20_8210bf01bad1
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 2931, 1287, "Q-A2")
EnergyStream12 = EnergyStream12.GetAsObject()

# Adding MaterialStream: MAT_b4019b97_8838_419d_9e98_4f1e5cb046ab
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 3093, 1246, "S-5-L")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(473.15)  # Temperature in K
MaterialStream20.SetPressure(100000)  # Pressure in Pa
MaterialStream20.SetMassFlow(0)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream5)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream6)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream6)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream5)  # ConnectReboilerDuty 
sim.ConnectObjects(HeaterCooler3.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeaterCooler3 to MaterialStream3
sim.ConnectObjects(EnergyStream12.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # EnergyStream12 to Reactor_Conversion2
sim.ConnectObjects(MaterialStream10.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream10 to DistillationColumn1
sim.ConnectObjects(MaterialStream8.GraphicObject, HeaterCooler4.GraphicObject, -1, -1)  # MaterialStream8 to HeaterCooler4
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream1
sim.ConnectObjects(MaterialStream15.GraphicObject, HeaterCooler6.GraphicObject, -1, -1)  # MaterialStream15 to HeaterCooler6
sim.ConnectObjects(HeaterCooler2.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler2 to EnergyStream2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream9
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream8
sim.ConnectObjects(MaterialStream16.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream16 to Mixer2
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream13 to Mixer1
sim.ConnectObjects(HeaterCooler4.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # HeaterCooler4 to EnergyStream4
sim.ConnectObjects(EnergyStream10.GraphicObject, HeaterCooler5.GraphicObject, -1, -1)  # EnergyStream10 to HeaterCooler5
sim.ConnectObjects(MaterialStream18.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # MaterialStream18 to Reactor_Conversion2
sim.ConnectObjects(MaterialStream12.GraphicObject, HeaterCooler5.GraphicObject, -1, -1)  # MaterialStream12 to HeaterCooler5
sim.ConnectObjects(MaterialStream14.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream14 to Mixer1
sim.ConnectObjects(EnergyStream11.GraphicObject, HeaterCooler6.GraphicObject, -1, -1)  # EnergyStream11 to HeaterCooler6
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream20
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream2
sim.ConnectObjects(MaterialStream19.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # MaterialStream19 to ShortcutColumn1
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Mixer2 to MaterialStream15
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler2
sim.ConnectObjects(MaterialStream7.GraphicObject, HeaterCooler3.GraphicObject, -1, -1)  # MaterialStream7 to HeaterCooler3
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream19
sim.ConnectObjects(EnergyStream8.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # EnergyStream8 to ShortcutColumn1
sim.ConnectObjects(HeaterCooler3.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # HeaterCooler3 to EnergyStream3
sim.ConnectObjects(HeaterCooler5.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # HeaterCooler5 to MaterialStream11
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream7
sim.ConnectObjects(EnergyStream7.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream7 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream6.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream6 to HeaterCooler1
sim.ConnectObjects(MaterialStream17.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream17 to Mixer2
sim.ConnectObjects(MaterialStream11.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream11 to Reactor_Conversion1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream1
sim.ConnectObjects(HeaterCooler4.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # HeaterCooler4 to MaterialStream4
sim.ConnectObjects(ShortcutColumn1.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # ShortcutColumn1 to EnergyStream9
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Mixer1 to MaterialStream12
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream10
sim.ConnectObjects(HeaterCooler6.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # HeaterCooler6 to MaterialStream18
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_26.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_26.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

