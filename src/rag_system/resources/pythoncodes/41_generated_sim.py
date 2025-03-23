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
cyclohexane = sim.AvailableCompounds["Cyclohexane"]
sim.SelectedCompounds.Add(cyclohexane.Name, cyclohexane)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)

# Adding Simulation Objects
# Adding EnergyStream: EN_11c728ba_73d3_4773_8357_cf9524ce67a8
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2185, 882, "ESTR-049")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_0f3cbd3b_f6bc_41a8_b66e_e9cffa3ab836
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2248, 842, "Feed to Distillation Column")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(323)  # Temperature in K
MaterialStream1.SetPressure(253312.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(7.8223564468116)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_cb6775b7_2c97_4f4d_9035_83a47287a45d
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 2182, 790, "COOL-049")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_904cc9d7_892b_4fc4_885e_839d97c5f609
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2441, 883, "Reboiler Duty")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding EnergyStream: EN_935a753d_5fcf_4884_917b_4551b4d61ba0
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2479, 670, "Condenser Dutry")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_9a7d5a8c_8744_4d58_a617_c7ccd75004e8
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2514, 742, "Distillate")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(397.686775812323)  # Temperature in K
MaterialStream2.SetPressure(1114575)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.27912174408727)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_09a85c4c_d5f0_422f_9bc2_e378ab63362a
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2305, 675, "DC-046")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_96eeafe0_c8cf_47b2_b51c_3ea1c1afdc4f
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2492, 560, "Fuel Gas")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(368.261610540229)  # Temperature in K
MaterialStream3.SetPressure(303975)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.16488202090401)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0c57f91b_71e1_47e9_9d8e_5f0de471fdf5
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2518, 853, "Cyclohexane")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(427.708438449901)  # Temperature in K
MaterialStream4.SetPressure(607950)  # Pressure in Pa
MaterialStream4.SetMassFlow(6.54321894799144)  # Mass Flow in kg/s

# Adding NodeIn: MIST_d116fe86_bfc3_4fe2_bb34_21283a4663d6
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2294, 605, "MIX-040")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_972d440b_fa6d_483a_b405_8620b59d9c89
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1962, 879, "ESTR-036")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_e00ebfd4_b88d_4220_9a49_55c82a61b838
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2116, 841, "Bottom Product")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(370)  # Temperature in K
MaterialStream5.SetPressure(303975)  # Pressure in Pa
MaterialStream5.SetMassFlow(7.8223564468116)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_48aa9f3e_6a18_4f8d_af47_cca52af55615
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2115, 724, "Top Product (Fuel Gas)")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(370)  # Temperature in K
MaterialStream6.SetPressure(303975)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.234801402761484)  # Mass Flow in kg/s

# Adding Vessel: SEP_605605b9_8730_4cae_b2df_c15956374772
Separator1 = sim.AddObject(ObjectType.Vessel, 2007, 763, "Low Pressure Separator")
Separator1 = Separator1.GetAsObject()

# Adding EnergyStream: EN_970eda95_ccea_430f_92d7_c739fd165318
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1861, 838, "ESTR-032")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_fa8a3ab4_48aa_446b_87f5_9e7ad0255e96
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1479, 677, "ESTR-030")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_fcc6d245_ea30_4614_a11a_1d7a72fd7150
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 877, 740, "Hydrogen Recycle")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(311)  # Temperature in K
MaterialStream7.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.103342290904725)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_964ec019_d4a4_48fb_b099_5cd2bdbf0cc6
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1052, 661, "REC-028")
Recycle1 = Recycle1.GetAsObject()

# Adding EnergyStream: EN_c53ad2f6_4d48_4fff_941f_aa63b9eee74a
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 1412, 865, "ESTR-010")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_88acfc2d_b6d6_4736_8b7c_a8d97e69b6a2
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1509, 820, "Reactor Bottoms")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(497)  # Temperature in K
MaterialStream8.SetPressure(3234800.6)  # Pressure in Pa
MaterialStream8.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a4871529_695c_456f_b55c_034577343c7e
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1509, 733, "Reactor Top")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(497)  # Temperature in K
MaterialStream9.SetPressure(3234800.6)  # Pressure in Pa
MaterialStream9.SetMassFlow(9.0905822001825)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_668f494d_336c_4dc3_9536_16b29148c491
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1392, 744, "Conversion Reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding NodeIn: MIST_1dbd2d7c_66bf_4f4c_9839_76a84f29e212
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1127, 778, "Feed Mixer")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_8f292ca5_35ae_41e2_b918_029d9d54ab6b
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1036, 808, "Benzene")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(311)  # Temperature in K
MaterialStream10.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream10.SetMassFlow(8.0379306)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_295dcb7b_2c87_4353_9dae_984932a63ab9
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 877, 796, "Hydrogen")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(311)  # Temperature in K
MaterialStream11.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.949309309277778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_46fd173d_61ab_4622_9e9f_01f8b4dcfae6
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1207, 811, "Mixed Feed")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(308.146815591644)  # Temperature in K
MaterialStream12.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream12.SetMassFlow(9.0905822001825)  # Mass Flow in kg/s

# Adding HeaterCooler: AQ_af2d3a61_e1d5_469b_a760_117ecc6ce586
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 1250, 764, "Feed Pre-heater")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding MaterialStream: MAT_81cb0354_3e45_498c_8f5e_7289912ad8c5
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1337, 809, "Pre-heated Feed")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(422)  # Temperature in K
MaterialStream13.SetPressure(3338152.1)  # Pressure in Pa
MaterialStream13.SetMassFlow(9.0905822001825)  # Mass Flow in kg/s

# Adding EnergyStream: EN_67e3a305_71f5_43dd_ba0c_c8382e0c53b4
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 1262, 866, "ESTR-006")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding HeaterCooler: RESF_caef13b6_1633_4ecc_abf0_8ee1f24c959a
HeaterCooler3 = sim.AddObject(ObjectType.Heater, 1578, 788, "Post-cooler")
HeaterCooler3 = HeaterCooler3.GetAsObject()

# Adding MaterialStream: MAT_8dabbdf4_f46c_4229_8445_037a56d3a570
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1653, 734, "Cooled Products")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(370)  # Temperature in K
MaterialStream14.SetPressure(2626850.6)  # Pressure in Pa
MaterialStream14.SetMassFlow(9.0905822001825)  # Mass Flow in kg/s

# Adding EnergyStream: EN_251a954b_9b8a_4dc8_ae6c_977ea4596c6f
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 1603, 853, "ESTR-013")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_b067cc61_2e29_48ce_b00f_5722f361f09e
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2133, 637, "To fuel gas")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(370)  # Temperature in K
MaterialStream15.SetPressure(2431800)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.930080618142524)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fda5db6a_2105_4957_8824_aca1c733fd24
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2015, 595, "Flash Top")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(370)  # Temperature in K
MaterialStream16.SetPressure(2431800)  # Pressure in Pa
MaterialStream16.SetMassFlow(1.03342290904725)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a4429454_8aa5_4e72_9937_0d2a9133c0b2
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1119, 633, "Recycle Stream")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(311)  # Temperature in K
MaterialStream17.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.103342290904725)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_535096d1_3e0c_498d_b1fa_89a87b2e9dd2
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1947, 793, "Flash Bottoms")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(370)  # Temperature in K
MaterialStream18.SetPressure(2431800)  # Pressure in Pa
MaterialStream18.SetMassFlow(8.05715769636169)  # Mass Flow in kg/s

# Adding Pump: BB_aa5e5c05_17b1_4a41_a991_ef76d36268fe
Pump1 = sim.AddObject(ObjectType.Pump, 1472, 614, "Pump")
Pump1 = Pump1.GetAsObject()

# Adding NodeOut: DIV_b12e3dfa_921e_42b9_8be4_3eef0cbe1d47
Splitter1 = sim.AddObject(ObjectType.NodeOut, 1945, 635, "Stream Splitter")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_4fb1845b_a1e7_46f3_a43c_21d3521a3e65
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1351, 686, "To Cooler")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(429.227174833928)  # Temperature in K
MaterialStream19.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream19.SetMassFlow(0.103342290904725)  # Mass Flow in kg/s

# Adding Vessel: SEP_ea72c8a7_a36c_4c53_8538_db1151600e96
Separator2 = sim.AddObject(ObjectType.Vessel, 1886, 698, "High Pressure Separator")
Separator2 = Separator2.GetAsObject()

# Adding HeaterCooler: RESF_79562109_86f4_4ffb_90fd_0fe953bde8b4
HeaterCooler4 = sim.AddObject(ObjectType.Heater, 1236, 629, "COOL-025")
HeaterCooler4 = HeaterCooler4.GetAsObject()

# Adding MaterialStream: MAT_a96de6c1_d6b7_4d1a_bd9b_35c05d526bdd
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1649, 681, "To Pump")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(370)  # Temperature in K
MaterialStream20.SetPressure(2431800)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.103342290904725)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4d82b3ff_6c4c_48e1_aa1c_b5aac696d90f
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 1258, 706, "ESTR-027")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding Valve: VALV_06409d43_b53e_43ec_b65f_1ca8bc12aa47
Valve1 = sim.AddObject(ObjectType.Valve, 1750, 792, "Pressure Reducing Valve")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_6dea5601_42ca_458e_9a7a_795645edfef6
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1787, 739, "Feed to Separator")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(369.463460166244)  # Temperature in K
MaterialStream21.SetPressure(2431800)  # Pressure in Pa
MaterialStream21.SetMassFlow(9.0905822001825)  # Mass Flow in kg/s

# Adding NodeIn: MIST_7e9ba772_202b_4a45_b869_bed191f4bb79
Mixer3 = sim.AddObject(ObjectType.NodeIn, 959, 770, "Hydrogen Mixer")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_7c4f86e6_a507_4eae_a368_8913b90ba008
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1038, 742, "Mixed Hydrogen")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(310.925587679119)  # Temperature in K
MaterialStream22.SetPressure(3819952.5)  # Pressure in Pa
MaterialStream22.SetMassFlow(1.0526516001825)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream2)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream4)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream3)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream2)  # ConnectReboilerDuty 
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Splitter1 to MaterialStream15
sim.ConnectObjects(HeaterCooler3.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # HeaterCooler3 to EnergyStream9
sim.ConnectObjects(MaterialStream1.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream1 to DistillationColumn1
sim.ConnectObjects(EnergyStream7.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream7 to Reactor_Conversion1
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Pump1 to MaterialStream19
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Separator1 to MaterialStream5
sim.ConnectObjects(MaterialStream14.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream14 to Valve1
sim.ConnectObjects(MaterialStream19.GraphicObject, HeaterCooler4.GraphicObject, -1, -1)  # MaterialStream19 to HeaterCooler4
sim.ConnectObjects(MaterialStream13.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream13 to Reactor_Conversion1
sim.ConnectObjects(HeaterCooler4.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # HeaterCooler4 to MaterialStream17
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream9
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler1
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream15 to Mixer1
sim.ConnectObjects(MaterialStream12.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream12 to HeaterCooler2
sim.ConnectObjects(HeaterCooler4.GraphicObject, EnergyStream10.GraphicObject, -1, -1)  # HeaterCooler4 to EnergyStream10
sim.ConnectObjects(EnergyStream8.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream8 to HeaterCooler2
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream13
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Mixer3 to MaterialStream22
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream1
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Separator2 to MaterialStream16
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Separator2 to MaterialStream18
sim.ConnectObjects(HeaterCooler3.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # HeaterCooler3 to MaterialStream14
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Recycle1 to MaterialStream7
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Mixer1 to MaterialStream3
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Valve1 to MaterialStream21
sim.ConnectObjects(MaterialStream18.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream18 to Separator1
sim.ConnectObjects(EnergyStream4.GraphicObject, Separator1.GraphicObject, -1, -1)  # EnergyStream4 to Separator1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Separator1 to MaterialStream6
sim.ConnectObjects(EnergyStream6.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream6 to Pump1
sim.ConnectObjects(MaterialStream21.GraphicObject, Separator2.GraphicObject, -1, -1)  # MaterialStream21 to Separator2
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Mixer2 to MaterialStream12
sim.ConnectObjects(MaterialStream20.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream20 to Pump1
sim.ConnectObjects(MaterialStream22.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream22 to Mixer2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream8
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream10 to Mixer2
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Splitter1 to MaterialStream20
sim.ConnectObjects(MaterialStream17.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream17 to Recycle1
sim.ConnectObjects(MaterialStream9.GraphicObject, HeaterCooler3.GraphicObject, -1, -1)  # MaterialStream9 to HeaterCooler3
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream11 to Mixer3
sim.ConnectObjects(EnergyStream5.GraphicObject, Separator2.GraphicObject, -1, -1)  # EnergyStream5 to Separator2
sim.ConnectObjects(MaterialStream16.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream16 to Splitter1
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream7 to Mixer3
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_41.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_41.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

