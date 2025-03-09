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
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
# methoxy_2_propanol_1 = sim.AvailableCompounds["1-Methoxy-2-Propanol"]
# sim.SelectedCompounds.Add(methoxy_2_propanol_1.Name, methoxy_2_propanol_1)
propylene_oxide_1_2 = sim.AvailableCompounds["1,2-propylene oxide"]
sim.SelectedCompounds.Add(propylene_oxide_1_2.Name, propylene_oxide_1_2)
# (2_methoxypropoxy)propan_1_ol_2 = sim.AvailableCompounds["2-(2-methoxypropoxy)propan-1-ol"]
# sim.SelectedCompounds.Add((2_methoxypropoxy)propan_1_ol_2.Name, (2_methoxypropoxy)propan_1_ol_2)

# Adding Simulation Objects
# Adding EnergyStream: EN_bfc7ed33_3d9d_41b1_bbc8_53f560909e83
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2678, 1162, "E-7")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_fc7f33ee_fbd2_4e20_a092_b3094d801862
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2712, 1344, "E-6")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_646c0675_976f_4459_8b22_f8621ee1b36f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2506, 1038, "S-5")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(473.15)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.167276)  # Mass Flow in kg/s

# Adding NodeIn: MIST_3f07592d_b91f_41a0_af41_ffadc105bd58
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2456, 980, "B-4")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_694bebde_3d30_43b9_843c_1185dbd0088c
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2153, 1028, "S-4")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(323.15)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.167276)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_32bf0403_9ffb_48e4_9da6_00222858d287
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 2244, 954, "B-3")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_4889e6b5_82cb_4df5_976d_ce2531893672
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2363, 941, "S-5-1")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(473.15)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.14206839693914)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2728ea29_66c8_4704_a2c2_b0e4294d7218
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2364, 1004, "S-5-2")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(473.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0252076030608596)  # Mass Flow in kg/s

# Adding EnergyStream: EN_9ff2f449_495b_47b8_8cc1_629be63d0d56
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2273, 1044, "E-2")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_be23e93a_ff69_4ba2_8611_1f65f7b1adf7
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1888, 926, "S-1")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.111406)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_556ead6e_4867_4d26_aaae_66df5dc7109f
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1891, 1030, "S-2")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.05587)  # Mass Flow in kg/s

# Adding NodeIn: MIST_b7126e7a_6b32_4014_a6bc_89b2f953ec98
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1940, 970, "B-1")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_d749b58d_46ac_4f1a_917e_f231570bfd2e
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1997, 1038, "S-3")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.167276)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_82076be4_f523_412d_96e9_9f692a051588
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 2077, 943, "B-2")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_3504ca4a_9a0e_4460_8b92_1cbdffb83076
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2070, 1028, "E-1")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding HeaterCooler: AQ_dfd83e28_113a_453e_885c_8b39eb5939ce
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 2576, 953, "B-5")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding MaterialStream: MAT_e35be9f2_93da_47d0_8947_8a008af622ee
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2666, 1070, "S-6")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(438.15)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.167276)  # Mass Flow in kg/s

# Adding EnergyStream: EN_05caa6b0_bdc8_4a17_b3e7_eea3d7b2402b
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2581, 1043, "E-3")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_9b8d3435_9ab4_4bb8_90fd_0eaf2a253d56
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2185, 1241, "S-7")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(438.119063194402)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.148307216556966)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_be3746b2_d4f5_41b9_878f_abae84a29590
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2161, 1349, "S-11")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(438.4823089502)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.0189692735829287)  # Mass Flow in kg/s

# Adding ShortcutColumn: SC_b7f35cab_656b_4082_97c8_5cfa9800e772
ShortcutColumn1 = sim.AddObject(ObjectType.ShortcutColumn, 1905, 1182, "B-6")
ShortcutColumn1 = ShortcutColumn1.GetAsObject()

# Adding EnergyStream: EN_b10ed91e_5e1e_482d_a8c3_a4db89fda480
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2046, 1371, "E-4")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_c726fdc1_45db_4b85_9108_8880746c0a4b
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2603, 1409, "S-10")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(406.57138470902)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.120006241009384)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_a096d7a7_18c3_436e_a64f_4c5774933d14
HeaterCooler3 = sim.AddObject(ObjectType.Heater, 2268, 1187, "B-7")
HeaterCooler3 = HeaterCooler3.GetAsObject()

# Adding MaterialStream: MAT_9b6667b4_842e_4ba8_a17f_f47552a9547d
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2382, 1264, "S-8")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(387.15)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.148307216556966)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4453366b_ed8c_4fa9_a5f2_df9b7fb1b2f6
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2293, 1306, "E-5")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_1a55dfc5_c2b3_4d9d_923e_c1379e9182a3
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2670, 1256, "S-9")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(328.03061091359)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.0282727312600935)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_e8b0cb75_01f4_49f4_bbaa_ef55e689de08
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2480, 1201, "B-9")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_77025035_0e85_44e5_8f0e_8d6006023a29
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2080, 1161, "E-8")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding HeaterCooler: RESF_58052c2e_2f14_4010_8a72_65d9a82c0be1
HeaterCooler4 = sim.AddObject(ObjectType.Heater, 2672, 1429, "B-10")
HeaterCooler4 = HeaterCooler4.GetAsObject()

# Adding EnergyStream: EN_0ce32546_aa20_423c_937e_438d4e84f4e2
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2723, 1475, "E-9")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_7fdcd685_4ee6_4da7_82d8_3ce6a68d38c7
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2765, 1402, "S-13")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(298.15)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.120006241009384)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_42e41bbc_84ff_49cf_9efb_2c1cfd1a89e6
HeaterCooler5 = sim.AddObject(ObjectType.Heater, 2272, 1395, "B-8")
HeaterCooler5 = HeaterCooler5.GetAsObject()

# Adding EnergyStream: EN_bdfc425c_aa55_44cc_bbdd_f02496d9e697
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 2386, 1442, "E-10")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding MaterialStream: MAT_5e9e9300_55d8_4182_bff8_52b5300e1c26
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2346, 1352, "S-12")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(298.15)  # Temperature in K
MaterialStream15.SetPressure(101325)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.0189692735829287)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream13)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream11)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream1)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream2)  # ConnectReboilerDuty 
sim.ConnectObjects(EnergyStream3.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream3 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream9.GraphicObject, HeaterCooler3.GraphicObject, -1, -1)  # MaterialStream9 to HeaterCooler3
sim.ConnectObjects(MaterialStream12.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream12 to DistillationColumn1
sim.ConnectObjects(HeaterCooler5.GraphicObject, EnergyStream10.GraphicObject, -1, -1)  # HeaterCooler5 to EnergyStream10
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream9
sim.ConnectObjects(ShortcutColumn1.GraphicObject, EnergyStream8.GraphicObject, -1, -1)  # ShortcutColumn1 to EnergyStream8
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream8
sim.ConnectObjects(MaterialStream8.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # MaterialStream8 to ShortcutColumn1
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer2 to MaterialStream7
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(EnergyStream7.GraphicObject, HeaterCooler3.GraphicObject, -1, -1)  # EnergyStream7 to HeaterCooler3
sim.ConnectObjects(EnergyStream6.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # EnergyStream6 to ShortcutColumn1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream3
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(EnergyStream4.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # EnergyStream4 to HeaterCooler1
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(MaterialStream2.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream2 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream1.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream1 to HeaterCooler2
sim.ConnectObjects(EnergyStream5.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream5 to HeaterCooler2
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream10
sim.ConnectObjects(HeaterCooler4.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # HeaterCooler4 to EnergyStream9
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream4
sim.ConnectObjects(MaterialStream10.GraphicObject, HeaterCooler5.GraphicObject, -1, -1)  # MaterialStream10 to HeaterCooler5
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream2
sim.ConnectObjects(HeaterCooler5.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # HeaterCooler5 to MaterialStream15
sim.ConnectObjects(MaterialStream11.GraphicObject, HeaterCooler4.GraphicObject, -1, -1)  # MaterialStream11 to HeaterCooler4
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream6 to Mixer2
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream5 to Mixer2
sim.ConnectObjects(MaterialStream7.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream7 to HeaterCooler1
sim.ConnectObjects(HeaterCooler4.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # HeaterCooler4 to MaterialStream14
sim.ConnectObjects(HeaterCooler3.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # HeaterCooler3 to MaterialStream12
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_30.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_30.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

