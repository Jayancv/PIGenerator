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
propylene = sim.AvailableCompounds["Propylene"]
sim.SelectedCompounds.Add(propylene.Name, propylene)
p_diisopropylbenzene = sim.AvailableCompounds["P-diisopropylbenzene"]
sim.SelectedCompounds.Add(p_diisopropylbenzene.Name, p_diisopropylbenzene)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)
cumene = sim.AvailableCompounds["Cumene"]
sim.SelectedCompounds.Add(cumene.Name, cumene)

# Adding Simulation Objects
# Adding CapeOpenUO: COUO_7fc3bb76_c134_46b9_bc84_8cceaed29a34
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2442, 948, "COUO-040")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_1e28622b_d6a1_4e36_a690_7b38a8a237d7
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2545, 911, "Cumene")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(424.870205358499)  # Temperature in K
MaterialStream1.SetPressure(100000)  # Pressure in Pa
MaterialStream1.SetMassFlow(3.19906103905051)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2833daa4_ba12_485e_adde_ccb2aacfd6de
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2386, 968, "MSTR-040")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(424.939453874569)  # Temperature in K
MaterialStream2.SetPressure(100000)  # Pressure in Pa
MaterialStream2.SetMassFlow(3.20309964429737)  # Mass Flow in kg/s

# Adding Valve: VALV_3aa03a0c_bf7c_4c27_b8da_9241cda54a03
Valve1 = sim.AddObject(ObjectType.Valve, 2288, 968, "VALV-039")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_3e0827ed_e122_400e_88e0_ad6e379935f8
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2545, 988, "p-DIB")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(474.172123982881)  # Temperature in K
MaterialStream3.SetPressure(100000)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.00403860524312934)  # Mass Flow in kg/s

# Adding EnergyStream: EN_703f67f9_e024_47f7_9e2f_5c9760db8ac3
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1290, 817, "ESTR-035")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_07b61e8b_391c_42b8_a18b_f30b59a14096
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1182, 882, "MSTR-035")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(323.924930107818)  # Temperature in K
MaterialStream4.SetPressure(2500001.68441433)  # Pressure in Pa
MaterialStream4.SetMassFlow(2.31004208487128)  # Mass Flow in kg/s

# Adding Pump: BB_4fda56a7_5648_4569_bd44_0b20c87b4885
Pump1 = sim.AddObject(ObjectType.Pump, 1336, 869, "PUMP-033")
Pump1 = Pump1.GetAsObject()

# Adding RCT_Conversion: RC_e79ce259_5cdc_4079_bd1c_22dfe826710a
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1885, 616, "RC-018")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding EnergyStream: EN_7b6b1a9f_5989_4b0a_8cf3_5ba9d61a9633
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1749, 689, "ESTR-017")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_abfec96f_39e8_42f0_a6a0_f07d97730cd5
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1781, 639, "MSTR-016")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(647.15)  # Temperature in K
MaterialStream5.SetPressure(2500000)  # Pressure in Pa
MaterialStream5.SetMassFlow(5.67599844965667)  # Mass Flow in kg/s

# Adding Heater: AQ_f9f68726_2f4b_4aa7_a600_e6e3364e010e
Heater1 = sim.AddObject(ObjectType.Heater, 1707, 634, "HEAT-015")
Heater1 = Heater1.GetAsObject()

# Adding HeatExchanger: HE_92dd49ca_faf7_4e37_9a00_8fa6b2e2d6b5
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1512, 559, "HE-014")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_ff7dd058_393c_4c55_9a31_03547852bf93
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1637, 638, "MSTR-013")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(580.15)  # Temperature in K
MaterialStream6.SetPressure(2500000)  # Pressure in Pa
MaterialStream6.SetMassFlow(5.67599844965667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_88d7c2c2_8d0b_4e25_acd3_c9c57d156da4
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1521, 675, "MSTR-012")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(607.975303697804)  # Temperature in K
MaterialStream7.SetPressure(2500000)  # Pressure in Pa
MaterialStream7.SetMassFlow(5.67601067534724)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e10b5f9d_01f8_42bb_9207_0b504c6aa40a
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1631, 534, "MSTR-011")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(692.15)  # Temperature in K
MaterialStream8.SetPressure(2500000)  # Pressure in Pa
MaterialStream8.SetMassFlow(5.67601067534724)  # Mass Flow in kg/s

# Adding EnergyStream: EN_08047aa9_aba3_4a7c_a276_61339f144a7c
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1319, 616, "ESTR-010")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_460b395b_42e9_46e0_9ded_2f1f2bf0af62
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1442, 557, "MSTR-009")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(483.15)  # Temperature in K
MaterialStream9.SetPressure(2500000)  # Pressure in Pa
MaterialStream9.SetMassFlow(5.67599844965667)  # Mass Flow in kg/s

# Adding Heater: AQ_8e6d0018_d38d_4324_a1a5_620796944a48
Heater2 = sim.AddObject(ObjectType.Heater, 1356, 554, "HEAT-008")
Heater2 = Heater2.GetAsObject()

# Adding NodeIn: MIST_49d9a67d_01cb_419f_b809_ea08685ad032
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1184, 556, "MIX-007")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_cd4062de_62e9_4332_bafd_b58dd83249b4
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1290, 556, "MSTR-006")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(321.581824535354)  # Temperature in K
MaterialStream10.SetPressure(2500000)  # Pressure in Pa
MaterialStream10.SetMassFlow(5.67599844965667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6387c39e_c81a_4bf0_9720_a0fdc8167845
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1107, 728, "MSTR-005")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(329.33)  # Temperature in K
MaterialStream11.SetPressure(2500000)  # Pressure in Pa
MaterialStream11.SetMassFlow(4.45463879535551)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1aaf1957_25a3_46e3_a13c_e6c5d9597f50
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1054, 583, "Excess Benzene")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(281.491045666007)  # Temperature in K
MaterialStream12.SetPressure(2500000)  # Pressure in Pa
MaterialStream12.SetMassFlow(2.1658043868)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_65a7b269_576a_43bc_9cca_30949d387f65
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1024, 630, "MAKEUP MIXER")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_50ff937f_a06f_4568_ae7c_e035bcc0c4a3
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 910, 712, "MakeUp Benzene")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(323.915877404967)  # Temperature in K
MaterialStream13.SetPressure(2500001.68441433)  # Pressure in Pa
MaterialStream13.SetMassFlow(2.31007648863199)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9640dbf0_17c6_4844_bb2d_8b63df2fcbd7
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 905, 610, "Fresh Benzene")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(298.15)  # Temperature in K
MaterialStream14.SetPressure(2500000)  # Pressure in Pa
MaterialStream14.SetMassFlow(4.3396701384)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5c4a36de_9fb3_4a69_8f62_ccdddb9b5353
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 910, 546, "C3")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(298.15)  # Temperature in K
MaterialStream15.SetPressure(2500000)  # Pressure in Pa
MaterialStream15.SetMassFlow(1.22135965430116)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5f238e56_6a64_489a_9eb9_a607255cbf55
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1962, 537, "MSTR-019")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(692.15)  # Temperature in K
MaterialStream16.SetPressure(2500000)  # Pressure in Pa
MaterialStream16.SetMassFlow(5.67599844965667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e7f628cd_c74d_4f02_80cc_05f6f58d54c7
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2006, 648, "MSTR-020")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(692.15)  # Temperature in K
MaterialStream17.SetPressure(2500000)  # Pressure in Pa
MaterialStream17.SetMassFlow(6.30162416654553E-16)  # Mass Flow in kg/s

# Adding EnergyStream: EN_cc1d4f61_d598_410e_b079_e4c8b2dba037
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1861, 681, "ESTR-021")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding Cooler: RESF_16fd5e0a_74d0_4e2a_9c7e_e2b8d37faa13
Cooler1 = sim.AddObject(ObjectType.Cooler, 1520, 730, "COOL-022")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_bf4bb464_95aa_4d7b_8d2d_aded2ac1d7d5
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1562, 791, "MSTR-023")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(363.15)  # Temperature in K
MaterialStream18.SetPressure(2500000)  # Pressure in Pa
MaterialStream18.SetMassFlow(5.67601067534724)  # Mass Flow in kg/s

# Adding EnergyStream: EN_98bac179_aca0_4d38_8aa8_11faff8b7f33
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1439, 732, "ESTR-024")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_06e17ea9_3ef6_4b90_b515_ba3d2970d720
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1688, 791, "MSTR-025")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(358.459463329046)  # Temperature in K
MaterialStream19.SetPressure(174998.31558567)  # Pressure in Pa
MaterialStream19.SetMassFlow(5.67601067534724)  # Mass Flow in kg/s

# Adding Valve: VALV_2da5dfde_f144_4097_a967_8250e3f748b2
Valve2 = sim.AddObject(ObjectType.Valve, 1618, 791, "VALV-026")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_3ac94179_efcc_477f_84ca_03882d0a2414
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1985, 767, "Gas")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(363.15)  # Temperature in K
MaterialStream20.SetPressure(236297.039583817)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.162868660221355)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_291ef445_cbc8_44c7_aa17_b8742fe2572e
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1952, 931, "MSTR-029")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(363.15)  # Temperature in K
MaterialStream21.SetPressure(191094.870815609)  # Pressure in Pa
MaterialStream21.SetMassFlow(5.51314172916857)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_3bc785b4_d491_495d_8135_e41c22030428
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1839, 791, "COUO-033")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_4544beae_087d_47c7_ae22_2df4909d3bd3
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1470, 870, "MSTR-033")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(322.689006074666)  # Temperature in K
MaterialStream22.SetPressure(175000)  # Pressure in Pa
MaterialStream22.SetMassFlow(2.31004208487128)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_08728400_a9f6_4045_8ace_8e5792df4a23
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2212, 969, "MSTR-034")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(447.985316999515)  # Temperature in K
MaterialStream23.SetPressure(175000)  # Pressure in Pa
MaterialStream23.SetMassFlow(3.20309964429737)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_64c5e755_e3b8_420d_bc04_f75f24d9f51d
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 2068, 929, "COUO-034")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()

# Adding OT_Recycle: REC_ccabb181_9a26_4802_b2b5_d0d1aeaff4cc
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1777, 543, "REC-036")
Recycle1 = Recycle1.GetAsObject()

# Adding OT_Recycle: REC_5bd062ab_3f05_4100_84f3_db645f8ac4cd
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1009, 840, "REC-037")
Recycle2 = Recycle2.GetAsObject()

sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream17
sim.ConnectObjects(EnergyStream2.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream2 to Heater1
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # Cooler1 to EnergyStream5
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream4 to Recycle2
sim.ConnectObjects(MaterialStream21.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream21 to CapeOpenUO4
sim.ConnectObjects(MaterialStream19.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream19 to CapeOpenUO3
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Pump1 to MaterialStream4
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream15 to Mixer1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream16
sim.ConnectObjects(MaterialStream22.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream22 to Pump1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Cooler1 to MaterialStream18
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Recycle2 to MaterialStream13
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Valve2 to MaterialStream19
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Valve1 to MaterialStream2
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Heater1 to MaterialStream5
sim.ConnectObjects(MaterialStream18.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream18 to Valve2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(MaterialStream8.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream8 to HeatExchanger1
sim.ConnectObjects(MaterialStream5.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream5 to Reactor_Conversion1
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Heater2 to MaterialStream9
sim.ConnectObjects(MaterialStream13.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream13 to CapeOpenUO2
sim.ConnectObjects(MaterialStream16.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream16 to Recycle1
sim.ConnectObjects(EnergyStream3.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream3 to Heater2
# sim.ConnectObjects(MaterialStream14.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream14 to CapeOpenUO2
sim.ConnectObjects(MaterialStream23.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream23 to Valve1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream11
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Recycle1 to MaterialStream8
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream23
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Mixer1 to MaterialStream10
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream6
sim.ConnectObjects(MaterialStream9.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream9 to HeatExchanger1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream20
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_Conversion1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream21
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream22
sim.ConnectObjects(MaterialStream10.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream10 to Heater2
sim.ConnectObjects(MaterialStream7.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream7 to Cooler1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream7
sim.ConnectObjects(MaterialStream6.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream6 to Heater1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream12
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream11 to Mixer1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_34.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_34.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

