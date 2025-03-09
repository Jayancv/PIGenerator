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
metano = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(metano.Name, metano)
etano = sim.AvailableCompounds["Ethane"]
sim.SelectedCompounds.Add(etano.Name, etano)
nitrogenio = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogenio.Name, nitrogenio)
ibutano = sim.AvailableCompounds["Isobutane"]
sim.SelectedCompounds.Add(ibutano.Name, ibutano)
nbutano = sim.AvailableCompounds["N-butane"]
sim.SelectedCompounds.Add(nbutano.Name, nbutano)
propano = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propano.Name, propano)
agua = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(agua.Name, agua)
dioxidodecarbono = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(dioxidodecarbono.Name, dioxidodecarbono)
npentano = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(npentano.Name, npentano)
ipentano = sim.AvailableCompounds["Isopentane"]
sim.SelectedCompounds.Add(ipentano.Name, ipentano)

# Adding Simulation Objects
# Adding MaterialStream: MAT_3db7a05a_1687_4d83_8ecb_f0248321369a
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1539, 1364, "PRODUCED GAS")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(305.15)  # Temperature in K
MaterialStream1.SetPressure(3923523.717328)  # Pressure in Pa
MaterialStream1.SetMassFlow(11.489981)  # Mass Flow in kg/s

# Adding CompressorExpander: TURB_dd59bb46_6f6c_4649_a208_7745337dd9fd
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1617, 1360, "TURB-000")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_847e0b84_e2fc_47ed_8bbd_27ac6b6491a0
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1686, 1360, "MAT-005")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(259.322887002629)  # Temperature in K
MaterialStream2.SetPressure(980871.120523)  # Pressure in Pa
MaterialStream2.SetMassFlow(11.489981)  # Mass Flow in kg/s

# Adding Vessel: SEP_b2f51d01_9efc_451c_b049_fa35af8197d4
Separator1 = sim.AddObject(ObjectType.Vessel, 1749, 1338, "SEP-001")
Separator1 = Separator1.GetAsObject()

# Adding MaterialStream: MAT_041afb7d_f7fa_4b5c_8a57_7b8cccbdb653
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1835, 1317, "MAT-006")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(259.322887002629)  # Temperature in K
MaterialStream3.SetPressure(980871.120523)  # Pressure in Pa
MaterialStream3.SetMassFlow(10.2793422070458)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_46e4e5db_f9a9_4b8c_826a_1f8620dea4f6
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1817, 1370, "MAT-007")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(259.322887002629)  # Temperature in K
MaterialStream4.SetPressure(980871.120523)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.21064990434296)  # Mass Flow in kg/s

# Adding EnergyStream: EN_f9c23fc0_ede4_4132_8ec8_e5ec15ed0206
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1667, 1417, "EN-000")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding HeaterCooler: RESF_ac4548b8_930a_4138_88af_bce2bd994723
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1894, 1310, "RESF-000")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_83c25006_15c9_453f_9b9c_26e0412f62db
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1956, 1314, "MAT-008")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(210.483418996203)  # Temperature in K
MaterialStream5.SetPressure(980871.120523)  # Pressure in Pa
MaterialStream5.SetMassFlow(10.2793422070458)  # Mass Flow in kg/s

# Adding EnergyStream: EN_a9cf3f46_ee5a_4905_9706_44589ed032d5
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1875, 1365, "EN-001")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding DistillationColumn: DC_c9ce1522_6097_4ff6_8006_e57cc2e1ae1a
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2019, 1362, "DEMETHANIZER")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_60ef0635_1155_44e8_a6a3_7b51a76ea9a2
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2242, 1331, "EN-002")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_60ef3279_c580_4f20_bfbb_89a240bb2553
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2249, 1372, "MAT-011")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(134.902706004339)  # Temperature in K
MaterialStream6.SetPressure(980880.929332)  # Pressure in Pa
MaterialStream6.SetMassFlow(6.51617212055673)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_cf8244b9_aff5_4034_a17a_1ecd31c4ac51
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2249, 1566, "MAT-012")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(259.069415573451)  # Temperature in K
MaterialStream7.SetPressure(980880.929332)  # Pressure in Pa
MaterialStream7.SetMassFlow(3.76724603433777)  # Mass Flow in kg/s

# Adding EnergyStream: EN_0d5cf8fd_eebf_4025_b624_d25e2dfb8553
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2249, 1522, "EN-003")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding Valve: VALV_e661f136_141d_4fb7_abe5_2c89823ac087
Valve1 = sim.AddObject(ObjectType.Valve, 2309, 1566, "VALV-000")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_4301c56b_e3ad_4c07_bd7e_e0bf2d9906b6
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2376, 1568, "MAT-013")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(250.322451801576)  # Temperature in K
MaterialStream8.SetPressure(687597.531462)  # Pressure in Pa
MaterialStream8.SetMassFlow(3.76724603433777)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_3d52b57c_82f9_461f_9a7e_10d7c31d9e16
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 2451, 1492, "DEETHANIZER")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding MaterialStream: MAT_b715419e_7e85_4571_a7f6_bdadb2c9ea14
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2752, 1417, "MAT-015")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(255.673472056427)  # Temperature in K
MaterialStream9.SetPressure(686616.650532)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.68574749448329)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ebddc756_9c2d_44c1_8afa_b9b4eaae5d62
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2686, 1657, "MAT-016")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(304.889204171059)  # Temperature in K
MaterialStream10.SetPressure(686616.650532)  # Pressure in Pa
MaterialStream10.SetMassFlow(2.08169447801482)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3f2b8698_db34_49e4_bf58_8ad368fbd407
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2619, 1623, "EN-004")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_c43436ff_aadd_4f1c_aff7_c8661f40827e
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2694, 1512, "EN-005")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding Valve: VALV_6e136d63_6873_4634_99ed_9f198daa9870
Valve2 = sim.AddObject(ObjectType.Valve, 2746, 1656, "VALV-001")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_a6d9257a_a31f_4cff_9c99_24c84a28eced
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2808, 1656, "MAT-017")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(293.706053515635)  # Temperature in K
MaterialStream11.SetPressure(489459.583736)  # Pressure in Pa
MaterialStream11.SetMassFlow(2.08169447801482)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_510009a5_e185_4f0a_a1fe_3123023c46f2
DistillationColumn3 = sim.AddObject(ObjectType.DistillationColumn, 2865, 1574, "DEBUTANIZER")
DistillationColumn3 = DistillationColumn3.GetAsObject()

# Adding MaterialStream: MAT_e2415c7d_45ba_4bcd_9739_efa8bc836dbc
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 3060, 1609, "MAT-018")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(290.330625748928)  # Temperature in K
MaterialStream12.SetPressure(488478.702807)  # Pressure in Pa
MaterialStream12.SetMassFlow(1.97597468130922)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_53d7df7d_91a1_4af8_b091_a045e1890052
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 3049, 1748, "MAT-019")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(360.73011113177)  # Temperature in K
MaterialStream13.SetPressure(490440.464666)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.105668740598555)  # Mass Flow in kg/s

# Adding EnergyStream: EN_7331e0e6_908c_4639_bb89_c6506b15c89d
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 3040, 1709, "EN-006")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding EnergyStream: EN_4b9de6a5_f556_49e0_ac4d_6b7ba0f8dea4
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 3039, 1568, "EN-007")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding Pump: BB_1044aecf_9f74_48c1_b29c_2b098a21abc8
Pump1 = sim.AddObject(ObjectType.Pump, 3112, 1607, "BB-000")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_da1bc1aa_1576_49a3_8734_10b86961fd00
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 3206, 1610, "LPG")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(291.685469206071)  # Temperature in K
MaterialStream14.SetPressure(1959800.096805)  # Pressure in Pa
MaterialStream14.SetMassFlow(1.97597468130922)  # Mass Flow in kg/s

# Adding EnergyStream: EN_49d74952_4f79_4eff_815d_dba5c44a1fb2
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 3073, 1660, "EN-008")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_30b1713c_9fdb_4c63_bc76_2ecd5fd5a851
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 3211, 1734, "C5+ (NATURAL GASOLINE)")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(361.149032988047)  # Temperature in K
MaterialStream15.SetPressure(980880.929332)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.105668740598555)  # Mass Flow in kg/s

# Adding EnergyStream: EN_d35c6b63_736f_4fa1_8f57_7e6f1a858a9e
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 3077, 1797, "EN-009")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding Pump: BB_9e05860a_4175_460e_bce3_acd77e06104b
Pump2 = sim.AddObject(ObjectType.Pump, 3110, 1749, "BB-001")
Pump2 = Pump2.GetAsObject()

# Adding Valve: VALV_243a4344_90f8_498e_ba7e_a07eef8772ff
Valve3 = sim.AddObject(ObjectType.Valve, 2312, 1370, "VALV-002")
Valve3 = Valve3.GetAsObject()

# Adding MaterialStream: MAT_1088430e_ff9b_4e3f_8c7c_88b32039c78d
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2375, 1369, "MAT-022")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(124.931306758201)  # Temperature in K
MaterialStream16.SetPressure(490440.464666)  # Pressure in Pa
MaterialStream16.SetMassFlow(6.51617212055673)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_ff5fc450_4f5d_4e95_9fa9_f801d31a1887
AdiabaticExpanderCompressor2 = sim.AddObject(ObjectType.Compressor, 2444, 1363, "COMP-000")
AdiabaticExpanderCompressor2 = AdiabaticExpanderCompressor2.GetAsObject()

# Adding HeaterCooler: AQ_efb55093_201d_4094_8355_18c56721fec3
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 2811, 1415, "AQ-000")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding EnergyStream: EN_3176137c_92fa_4009_ace4_d8df9e9c168d
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 2421, 1425, "EN-010")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding MaterialStream: MAT_d95a9def_54df_4130_96b9_85e60c5dbdd5
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2538, 1367, "INDUSTRIAL METHANE")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(132.666450914174)  # Temperature in K
MaterialStream17.SetPressure(817296.510147554)  # Pressure in Pa
MaterialStream17.SetMassFlow(6.51617212055673)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1fbd0c0b_79ec_4d03_b4de_d5a023e7955b
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2921, 1417, "INDUSTRIAL ETHANE")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(314.919840201516)  # Temperature in K
MaterialStream18.SetPressure(686616.650532)  # Pressure in Pa
MaterialStream18.SetMassFlow(1.68574749448329)  # Mass Flow in kg/s

# Adding EnergyStream: EN_0b0c0d25_5ff2_43ce_a759_ac633a36cafc
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 2775, 1471, "EN-011")
EnergyStream12 = EnergyStream12.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream6)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream7)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream3)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream4)  # ConnectReboilerDuty 
DistillationColumn2.ConnectBottoms(MaterialStream10)  # ConnectBottoms 
DistillationColumn2.ConnectVaporProduct(MaterialStream9) # ConnectVaporProduct 
DistillationColumn2.ConnectCondenserDuty(EnergyStream6)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream5)  # ConnectReboilerDuty 
DistillationColumn3.ConnectDistillate(MaterialStream12)  # ConnectDistillate 
DistillationColumn3.ConnectBottoms(MaterialStream13)  # ConnectBottoms 
DistillationColumn3.ConnectCondenserDuty(EnergyStream8)  # ConnectCondenserDuty 
DistillationColumn3.ConnectReboilerDuty(EnergyStream7)  # ConnectReboilerDuty
AdiabaticExpanderCompressor1.GraphicObject.EnergyConnector.set_Active(True)
AdiabaticExpanderCompressor1.ConnectEnergyStream(EnergyStream1)

sim.ConnectObjects(MaterialStream9.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream9 to HeaterCooler2
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Valve3 to MaterialStream16
sim.ConnectObjects(MaterialStream2.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream2 to Separator1
sim.ConnectObjects(MaterialStream16.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # MaterialStream16 to AdiabaticExpanderCompressor2
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream5
sim.ConnectObjects(EnergyStream11.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # EnergyStream11 to AdiabaticExpanderCompressor2
sim.ConnectObjects(EnergyStream10.GraphicObject, Pump2.GraphicObject, -1, -1)  # EnergyStream10 to Pump2
sim.ConnectObjects(MaterialStream10.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream10 to Valve2
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.ConnectObjects(MaterialStream12.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream12 to Pump1
sim.ConnectObjects(MaterialStream5.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream5 to DistillationColumn1
sim.ConnectObjects(MaterialStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream8.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream8 to DistillationColumn2
sim.ConnectObjects(MaterialStream6.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream6 to Valve3
sim.ConnectObjects(MaterialStream13.GraphicObject, Pump2.GraphicObject, -1, -1)  # MaterialStream13 to Pump2
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Valve2 to MaterialStream11
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Pump1 to MaterialStream14
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Separator1 to MaterialStream4
sim.ConnectObjects(MaterialStream11.GraphicObject, DistillationColumn3.GraphicObject, -1, -1)  # MaterialStream11 to DistillationColumn3
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream18
sim.ConnectObjects(EnergyStream12.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream12 to HeaterCooler2
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Valve1 to MaterialStream8
sim.ConnectObjects(EnergyStream9.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream9 to Pump1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Separator1 to MaterialStream3
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream2
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to EnergyStream1

sim.ConnectObjects(Pump2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Pump2 to MaterialStream15
sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to MaterialStream17
sim.ConnectObjects(MaterialStream7.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream7 to Valve1
sim.ConnectObjects(MaterialStream3.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream3 to HeaterCooler1
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_7.xml")
 
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
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_7.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

