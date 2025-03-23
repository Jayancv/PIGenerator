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
ethylene_glycol = sim.AvailableCompounds["Ethylene glycol"]
sim.SelectedCompounds.Add(ethylene_glycol.Name, ethylene_glycol)
diethylene_glycol = sim.AvailableCompounds["Diethylene glycol"]
sim.SelectedCompounds.Add(diethylene_glycol.Name, diethylene_glycol)
ethylene_oxide = sim.AvailableCompounds["Ethylene oxide"]
sim.SelectedCompounds.Add(ethylene_oxide.Name, ethylene_oxide)

# Adding Simulation Objects
# Adding OT_Adjust: AJ27bd946c_91b4_41ee_bd5a_5900295fa23c
Adjust1 = sim.AddObject(ObjectType.OT_Adjust, 2246, 1257, "ADJ-028")
Adjust1 = Adjust1.GetAsObject()

# Adding OT_Adjust: AJ4523d63d_3ca3_4abc_90aa_d7cbc94807f9
Adjust2 = sim.AddObject(ObjectType.OT_Adjust, 2628, 1241, "ADJ-029")
Adjust2 = Adjust2.GetAsObject()

# Adding MaterialStream: MAT_97d8b481_a727_427e_983e_2ef1bf79622d
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2727, 1575, "MSTR-027")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(391.223324968349)  # Temperature in K
MaterialStream1.SetPressure(184327.938517809)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.98866382862295)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d5f782ea_bce3_4bb6_940e_347d1e3b3e3d
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2800, 1537, "MSTR-026")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(339.36048183776)  # Temperature in K
MaterialStream2.SetPressure(24885.9022266318)  # Pressure in Pa
MaterialStream2.SetMassFlow(14.1045229673182)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d63e7b41_ef49_44af_ba67_fdd7a7864939
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2679, 1526, "MSTR-025")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(339.338047271181)  # Temperature in K
MaterialStream3.SetPressure(24885.9022266318)  # Pressure in Pa
MaterialStream3.SetMassFlow(14.1045229673182)  # Mass Flow in kg/s

# Adding Valve: VALV_47903811_5863_40de_a24a_f91765a4e6b1
Valve1 = sim.AddObject(ObjectType.Valve, 2628, 1493, "VALV-024")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_e35e7376_80bf_400b_a517_cea60f12e4b4
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2569, 1494, "MSTR-023")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(392.480307458695)  # Temperature in K
MaterialStream4.SetPressure(184327.938517809)  # Pressure in Pa
MaterialStream4.SetMassFlow(14.1045229673182)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_866fddfb_8498_4f38_87ec_6dd950e4d1ef
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 2736, 1465, "HE-022")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_96a85abe_0d36_4d7a_a193_f5b701bfff14
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2562, 1344, "MSTR-021")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(392.480315352845)  # Temperature in K
MaterialStream5.SetPressure(184327.938517809)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.98866382862295)  # Mass Flow in kg/s

# Adding Vessel: SEP_513a9b85_9865_4511_82be_81de325789de
Separator1 = sim.AddObject(ObjectType.Vessel, 2485, 1392, "SEP-022")
Separator1 = Separator1.GetAsObject()

# Adding EnergyStream: EN_4ae887ce_0561_4392_8514_f58ee320c9ec
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1554, 1323, "ESTR-006")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_5bfe7df7_f449_4d2c_bf8d_ab676fe6139c
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1685, 1259, "MSTR-005")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(482.749500486745)  # Temperature in K
MaterialStream6.SetPressure(2017221.10343227)  # Pressure in Pa
MaterialStream6.SetMassFlow(18.0470232597204)  # Mass Flow in kg/s

# Adding RCT_PFR: PFR_82ddb282_4be4_44e9_840e_5e5aecbedfd2
Reactor_PFR1 = sim.AddObject(ObjectType.RCT_PFR, 1562, 1244, "PFR-004")
Reactor_PFR1 = Reactor_PFR1.GetAsObject()

# Adding MaterialStream: MAT_487a9869_ea4b_48c6_8a38_4eeb0c46e973
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1483, 1273, "MSTR-003")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(482.749500486745)  # Temperature in K
MaterialStream7.SetPressure(2026500)  # Pressure in Pa
MaterialStream7.SetMassFlow(18.0470164909535)  # Mass Flow in kg/s

# Adding NodeIn: MIST_fd37db97_eb86_48ea_b794_bfe34f5d26ef
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1413, 1273, "MIX-002")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_b0256d4d_56b5_48ef_8912_4785324f2aa8
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1309, 1302, "WAT")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(453.15)  # Temperature in K
MaterialStream8.SetPressure(2026500)  # Pressure in Pa
MaterialStream8.SetMassFlow(4.8720565866)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2390e282_dc79_4b87_ba0f_c233c51b35f5
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1345, 1243, "EO")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(453.15)  # Temperature in K
MaterialStream9.SetPressure(2026500)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.6739988)  # Mass Flow in kg/s

# Adding Valve: VALV_a33f860e_2ca3_4bf6_a271_aa84bb9efe7c
Valve2 = sim.AddObject(ObjectType.Valve, 1746, 1262, "VALV-007")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_866bd308_e76c_439f_bb14_dadb4f87148f
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1828, 1261, "MSTR-008")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(445.526648800585)  # Temperature in K
MaterialStream10.SetPressure(801321.10343227)  # Pressure in Pa
MaterialStream10.SetMassFlow(18.0470232597204)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_170ec14f_1984_4125_a12b_aac6fc95b39c
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1917, 1393, "HEAT-009")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_6a90b1ad_6e24_40c6_a778_604d0cd518c0
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1996, 1408, "MSTR-010")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(445.551212351391)  # Temperature in K
MaterialStream11.SetPressure(801321.10343227)  # Pressure in Pa
MaterialStream11.SetMassFlow(18.0470232597204)  # Mass Flow in kg/s

# Adding EnergyStream: EN_421782d5_451f_47a8_9942_c30a426f67ef
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1956, 1475, "ESTR-011")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding Vessel: SEP_e02baca9_fae1_471d_b22e_4df2efc2d2bd
Separator2 = sim.AddObject(ObjectType.Vessel, 2055, 1381, "SEP-012")
Separator2 = Separator2.GetAsObject()

# Adding MaterialStream: MAT_f16e2466_6ea3_492c_bc15_fe1ce4a9ff8d
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2196, 1343, "MSTR-013")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(445.551212351391)  # Temperature in K
MaterialStream12.SetPressure(801321.10343227)  # Pressure in Pa
MaterialStream12.SetMassFlow(1.95383635938683)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8795d232_ac03_4f0a_a0a6_b221e252aeab
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2160, 1446, "MSTR-014")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(445.551212351391)  # Temperature in K
MaterialStream13.SetPressure(801321.10343227)  # Pressure in Pa
MaterialStream13.SetMassFlow(16.0931868390451)  # Mass Flow in kg/s

# Adding Valve: VALV_5c54733d_3abf_463f_8300_0572d07d166b
Valve3 = sim.AddObject(ObjectType.Valve, 2237, 1425, "VALV-015")
Valve3 = Valve3.GetAsObject()

# Adding MaterialStream: MAT_74b651d6_6771_4cd1_b0db_cfc915005044
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2309, 1440, "MSTR-016")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(392.455723430707)  # Temperature in K
MaterialStream14.SetPressure(184327.938517809)  # Pressure in Pa
MaterialStream14.SetMassFlow(16.0931868390451)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_00c2b62b_8618_42ce_b4d8_65eb6eb4d0e8
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 2302, 1388, "HE-017")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_bddeea6d_45e0_4374_abca_ce601a49b242
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2400, 1569, "MSTR-018")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(444.389114915179)  # Temperature in K
MaterialStream15.SetPressure(801321.10343227)  # Pressure in Pa
MaterialStream15.SetMassFlow(1.95383635938683)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_888e2741_9f73_4400_b151_04db33b984a1
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2404, 1426, "MSTR-019")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(392.480315352845)  # Temperature in K
MaterialStream16.SetPressure(184327.938517809)  # Pressure in Pa
MaterialStream16.SetMassFlow(16.0931868390451)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_68bb738b_e1c3_497f_9567_14545d353418
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2888, 1338, "DC-030")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_9d7bf9db_b121_43fc_9bde_2589565d2a2f
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 3066, 1236, "MSTR-036")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(334.061699413948)  # Temperature in K
MaterialStream17.SetPressure(19323.3)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.376501753863398)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dc2e3f71_bc87_4f01_ae3d_12ffd69eef70
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 3032, 1551, "MSTR-032")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(420.451689444848)  # Temperature in K
MaterialStream18.SetPressure(19323.3)  # Pressure in Pa
MaterialStream18.SetMassFlow(2.22707464144673)  # Mass Flow in kg/s

# Adding EnergyStream: EN_e21a48ec_7e86_4105_bed7_1487fb0d58cd
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 3069, 1323, "ESTR-033")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_82086afe_6df8_4373_9212_ee8e2c96349e
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 3065, 1469, "ESTR-034")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_c15316fd_b1a7_4f69_8929_3f18a50798ce
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2986, 1176, "MSTR-035")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(334.061701502096)  # Temperature in K
MaterialStream19.SetPressure(19323.3)  # Pressure in Pa
MaterialStream19.SetMassFlow(11.5006532092496)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_f3aee190_c671_4231_913f_141de17ff8ee
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2819, 1155, "REC-036")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_eb18a9ca_deb0_4a7d_a1aa_a5dfc1690365
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2669, 1105, "MSTR-037")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(334.061701502096)  # Temperature in K
MaterialStream20.SetPressure(19323.3)  # Pressure in Pa
MaterialStream20.SetMassFlow(11.5006532092496)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_944992aa_ca1c_4566_9432_8306212e0315
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 3409, 1276, "MSTR-038")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(388.513204354038)  # Temperature in K
MaterialStream21.SetPressure(5066.25)  # Pressure in Pa
MaterialStream21.SetMassFlow(2.20584603553224)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3210e7b0_265d_49a4_9b79_ecf5124c4269
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 3401, 1532, "MSTR-039")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(430.847355814742)  # Temperature in K
MaterialStream22.SetPressure(5066.25)  # Pressure in Pa
MaterialStream22.SetMassFlow(0.021201201808053)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_e0777b8f_2543_462f_a0b4_14f6d5e44828
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 3179, 1327, "DC-040")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding EnergyStream: EN_ca4b19a2_6e67_4e97_a72e_07862b34695e
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 3417, 1356, "ESTR-041")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_fe72a5fc_f070_413d_8f9e_89068055f7ff
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 3419, 1444, "ESTR-042")
EnergyStream6 = EnergyStream6.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream17)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream18)  # ConnectBottoms 
DistillationColumn1.ConnectVaporProduct(MaterialStream19) # ConnectVaporProduct 
DistillationColumn1.ConnectCondenserDuty(EnergyStream3)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream4)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream21)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream22)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream5)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream6)  # ConnectReboilerDuty 
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Valve1 to MaterialStream3
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Recycle1 to MaterialStream20
sim.ConnectObjects(Reactor_PFR1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Reactor_PFR1 to MaterialStream6
sim.ConnectObjects(MaterialStream10.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream10 to HeaterCooler1
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Separator2 to MaterialStream12
sim.ConnectObjects(MaterialStream5.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream5 to HeatExchanger1
sim.ConnectObjects(MaterialStream20.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream20 to Mixer1
sim.ConnectObjects(MaterialStream13.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream13 to Valve3
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream11
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream1
sim.ConnectObjects(EnergyStream2.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # EnergyStream2 to HeaterCooler1
sim.ConnectObjects(EnergyStream1.GraphicObject, Reactor_PFR1.GraphicObject, -1, -1)  # EnergyStream1 to Reactor_PFR1
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream16
sim.ConnectObjects(MaterialStream19.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream19 to Recycle1
sim.ConnectObjects(MaterialStream16.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream16 to Separator1
sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream9 to Mixer1
sim.ConnectObjects(MaterialStream11.GraphicObject, Separator2.GraphicObject, -1, -1)  # MaterialStream11 to Separator2
sim.ConnectObjects(MaterialStream3.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream3 to HeatExchanger1
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Separator2 to MaterialStream13
sim.ConnectObjects(MaterialStream12.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream12 to HeatExchanger2
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Separator1 to MaterialStream4
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Separator1 to MaterialStream5
sim.ConnectObjects(MaterialStream2.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream2 to DistillationColumn1
sim.ConnectObjects(MaterialStream18.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream18 to DistillationColumn2
sim.ConnectObjects(MaterialStream7.GraphicObject, Reactor_PFR1.GraphicObject, -1, -1)  # MaterialStream7 to Reactor_PFR1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer1 to MaterialStream7
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Valve2 to MaterialStream10
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream15
sim.ConnectObjects(MaterialStream6.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream6 to Valve2
sim.ConnectObjects(MaterialStream14.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream14 to HeatExchanger2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream2
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Valve3 to MaterialStream14
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_56.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_56.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

