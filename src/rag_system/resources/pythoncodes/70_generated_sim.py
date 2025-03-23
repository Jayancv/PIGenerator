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
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
biphenyl = sim.AvailableCompounds["Biphenyl"]
sim.SelectedCompounds.Add(biphenyl.Name, biphenyl)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)

# Adding Simulation Objects
# Adding EnergyStream: EN_53f2edab_8aff_4194_9450_26f9344e1d30
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1052, 635, "ESTR-033")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_fbb3765b_f874_471f_8472_23474b1ae42b
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 890, 567, "MSTR-032")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(380.033378944153)  # Temperature in K
MaterialStream1.SetPressure(2550000)  # Pressure in Pa
MaterialStream1.SetMassFlow(2.86441523683136)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5fe58946_4902_4b44_9caf_12c6fd521aec
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 948, 694, "Mixed Toulene")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(376.698453116043)  # Temperature in K
MaterialStream2.SetPressure(200000)  # Pressure in Pa
MaterialStream2.SetMassFlow(2.86441523683136)  # Mass Flow in kg/s

# Adding Pump: BB_c9606bd5_42ed_4567_a4c4_709682ab8b81
Pump1 = sim.AddObject(ObjectType.Pump, 954, 610, "PUMP-030")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_391bb960_5b3d_401c_afca_fa7ba04cb756
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1166, 742, "Recycle Toulene")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(541.97056792247)  # Temperature in K
MaterialStream3.SetPressure(2350000)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.0489916974895176)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_3020e62b_4fd0_48ac_ab22_dabcc2ab4d44
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1489, 791, "REC-028")
Recycle1 = Recycle1.GetAsObject()

# Adding NodeIn: MIST_a705a2a3_1618_4387_b2ab_95fc1edcccb3
Mixer1 = sim.AddObject(ObjectType.NodeIn, 871, 689, "Toulene Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_abb28c8f_0baa_4d66_be14_e8f407a24514
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2106, 486, "ESTR-032")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding EnergyStream: EN_66a9897c_12cc_4695_812e_04714606a032
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2109, 618, "ESTR-031")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_958d0843_c96d_4b58_8101_58e91fc41885
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2112, 671, "Heavy 1")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(541.97056792247)  # Temperature in K
MaterialStream4.SetPressure(2350000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0489916974895176)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1f2134d3_4e3d_44ee_924f_c4fae75369b5
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2113, 548, "Pure Benzene")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(474.650448754981)  # Temperature in K
MaterialStream5.SetPressure(2350000)  # Pressure in Pa
MaterialStream5.SetMassFlow(2.13676481560084)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_755422ac_6b22_47a9_a78e_7255f5b7bf03
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 1920, 503, "DC-028")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_98458539_6b74_4d03_8e17_791d75bd5a3f
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1443, 393, "MSTR-018")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(353.15)  # Temperature in K
MaterialStream6.SetPressure(2350000)  # Pressure in Pa
MaterialStream6.SetMassFlow(84.792167497722)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_a37614c5_1909_4718_b0df_5d473258857a
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1506, 419, "REC-017")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_6b78fd55_ee2c_4d85_8846_7bcc2677a703
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1664, 461, "MSTR-016")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(353.15)  # Temperature in K
MaterialStream7.SetPressure(2350000)  # Pressure in Pa
MaterialStream7.SetMassFlow(85.6387845504257)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_930aa3d4_262b_4b70_b016_cf8614e4da9c
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1685, 603, "MSTR-015")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(353.15)  # Temperature in K
MaterialStream8.SetPressure(2350000)  # Pressure in Pa
MaterialStream8.SetMassFlow(2.18578726475383)  # Mass Flow in kg/s

# Adding Vessel: SEP_fbef0810_b014_46ad_97d6_56f3078f39bb
Vessel1 = sim.AddObject(ObjectType.Vessel, 1598, 535, "SEP-014")
Vessel1 = Vessel1.GetAsObject()

# Adding EnergyStream: EN_e0a906d9_44e2_470c_b9ba_0061b92347df
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1515, 590, "ESTR-013")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_823c34fc_efa6_4aa0_8088_804931f4a13c
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1566, 525, "MSTR-012")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(353.15)  # Temperature in K
MaterialStream9.SetPressure(2350000)  # Pressure in Pa
MaterialStream9.SetMassFlow(87.8245726673574)  # Mass Flow in kg/s

# Adding Cooler: RESF_78b6b1d3_61ba_4214_a9c4_fd80349a7a9f
Cooler1 = sim.AddObject(ObjectType.Cooler, 1472, 535, "COOL-011")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_0df90675_84ee_467d_95b8_bbe004de905f
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1005, 542, "MSTR-010")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(354.749081376773)  # Temperature in K
MaterialStream10.SetPressure(2350000)  # Pressure in Pa
MaterialStream10.SetMassFlow(87.8245726673574)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_13091108_4c61_407d_bf8c_6323ab14ebe2
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 862, 472, "Hydrogen Feed")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(298.15)  # Temperature in K
MaterialStream11.SetPressure(2550000)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.167989932804)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f2b818cc_0880_42fa_a543_f03c8712cbde
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 791, 702, "Toulene")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(373.15)  # Temperature in K
MaterialStream12.SetPressure(200000)  # Pressure in Pa
MaterialStream12.SetMassFlow(2.8154235396)  # Mass Flow in kg/s

# Adding NodeIn: MIST_05e13a80_c297_4b99_ba3b_164a29f73ab5
Mixer2 = sim.AddObject(ObjectType.NodeIn, 954, 532, "MIX-012")
Mixer2 = Mixer2.GetAsObject()

# Adding Heater: AQ_e2f1a91f_b162_4a21_a3f5_c01e0ebd1d42
Heater1 = sim.AddObject(ObjectType.Heater, 1131, 548, "HEAT-004")
Heater1 = Heater1.GetAsObject()

# Adding MaterialStream: MAT_55851377_5d21_4dba_b124_8eb1d6637614
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1223, 530, "Hot Mixed Stream")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(873.15)  # Temperature in K
MaterialStream13.SetPressure(2350000)  # Pressure in Pa
MaterialStream13.SetMassFlow(87.8245726673574)  # Mass Flow in kg/s

# Adding EnergyStream: EN_89a8a648_293a_4b89_baa8_a8db8c95a56d
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1119, 614, "ESTR-006")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_99f9780f_f673_4dca_8860_f88ace4e9193
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1400, 578, "Dummy stream")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(873.15)  # Temperature in K
MaterialStream14.SetPressure(2350000)  # Pressure in Pa
MaterialStream14.SetMassFlow(-1.95009725406331E-14)  # Mass Flow in kg/s

# Adding EnergyStream: EN_73367d80_bcc3_4193_aa9a_f7250a129c9f
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1265, 579, "ESTR-009")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_d6dead30_991a_42d7_a3b3_8542ca66228e
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1401, 486, "MSTR-008")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(873.15)  # Temperature in K
MaterialStream15.SetPressure(2350000)  # Pressure in Pa
MaterialStream15.SetMassFlow(87.8245726673574)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_1ea27bab_d904_4e22_a6d3_d981ae1ecdaa
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1289, 514, "RC-007")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding Heater: AQ_fed5885f_4ee8_4981_84b8_d985bef715a6
Heater2 = sim.AddObject(ObjectType.Heater, 1771, 562, "HEAT-019")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_9009aff3_21e2_47d8_b0ec_5d62e47a48ec
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1853, 584, "MSTR-020")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(373.15)  # Temperature in K
MaterialStream16.SetPressure(2350000)  # Pressure in Pa
MaterialStream16.SetMassFlow(2.18578726475383)  # Mass Flow in kg/s

# Adding EnergyStream: EN_d1dd061c_f599_4697_8162_f6b5cee40d0c
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 1770, 622, "ESTR-021")
EnergyStream7 = EnergyStream7.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream5)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream4)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream2)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream3)  # ConnectReboilerDuty 
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Vessel1 to MaterialStream7
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Heater2 to MaterialStream16
sim.ConnectObjects(MaterialStream9.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream9 to Vessel1
sim.ConnectObjects(MaterialStream2.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream2 to Pump1
sim.ConnectObjects(MaterialStream10.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream10 to Heater1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream15
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream6 to Mixer2
sim.ConnectObjects(EnergyStream7.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream7 to Heater2
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
sim.ConnectObjects(MaterialStream16.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream16 to DistillationColumn1
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream11 to Mixer2
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Recycle1 to MaterialStream3
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Vessel1 to MaterialStream8
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Cooler1 to MaterialStream9
sim.ConnectObjects(MaterialStream13.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream13 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream1 to Mixer2
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Recycle2 to MaterialStream6
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream12 to Mixer1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream14
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Mixer1 to MaterialStream2
sim.ConnectObjects(EnergyStream5.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream5 to Heater1
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Mixer2 to MaterialStream10
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Pump1 to MaterialStream1
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(MaterialStream15.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream15 to Cooler1
sim.ConnectObjects(MaterialStream8.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream8 to Heater2
sim.ConnectObjects(EnergyStream6.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream6 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream7.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream7 to Recycle2
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Heater1 to MaterialStream13
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # Cooler1 to EnergyStream4
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_70.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_70.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

