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
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
acetic_acid = sim.AvailableCompounds["Acetic acid"]
sim.SelectedCompounds.Add(acetic_acid.Name, acetic_acid)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
acetaldehyde = sim.AvailableCompounds["Acetaldehyde"]
sim.SelectedCompounds.Add(acetaldehyde.Name, acetaldehyde)
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)

# Adding Simulation Objects
# Adding MaterialStream: MSTR_bc3270b0_2821_40d7_8343_39037a106af0
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1846, 1065, "Acetaldehyde recycle")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(298.15)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0562092427372419)  # Mass Flow in kg/s

# Adding EnergyStream: EN_13e0d4c1_9459_4697_b5d2_a8d46aeabbcd
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2826, 1320, "E5")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_c0b49308_fcac_45a4_9eb0_4839bb25f069
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2699, 1268, "Recycle2")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298.15)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0562092427372419)  # Mass Flow in kg/s

# Adding Heater: AQ_24ea832e_0534_4e17_a37f_70d1a6027c5c
Heater1 = sim.AddObject(ObjectType.Heater, 2836, 1265, "Heater2")
Heater1 = Heater1.GetAsObject()

# Adding OT_Recycle: REC_440b473f_3926_45b7_a738_3048957b8f15
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2530, 1204, "Water Recycle")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MSTR_b0608c07_f139_4362_89cb_d7b59c1dc744
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2407, 1087, "Water to recycle")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(359.07783108899997)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.0589755574140367)  # Mass Flow in kg/s

# Adding EnergyStream: EN_cd09c888_6d1b_4319_80b0_c2d1bb153f3c
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2614, 867, "E3")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding Heater: AQ_e409685f_916c_48b4_b32e_2b459700c0e1
Heater2 = sim.AddObject(ObjectType.Heater, 2638, 796, "Heater1")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_e8a370e5_e326_4620_84b1_cf6ee452dffa
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2703, 1203, "Complex column output")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(359.09299294261)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.05893657491071)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_75c29822_cda4_4278_9d54_9d0419a646d1
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2918, 1266, "Recycle1")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(113.72254334496)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0562092427372419)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_f7d9d8c4_8260_4627_9a1a_e492755a7df6
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2792, 1115, "Complex Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_e9d31e9e_ea8c_402e_a696_712eb82df733
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2782, 1029, "Recycle I/P")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(196.12879208218)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.115145817646343)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c28f5b26_fd0f_47c7_a7fb_c86b154d1d32
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2888, 768, "Nitrogen")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(230.86203308036)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.150188839979957)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_b282ccfa_c4f4_4e38_9642_99d95af7e55c
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 2809, 841, "Absorption column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_884359d6_5db3_4cbd_8890_b2d7559720c2
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2576, 797, "Separator O/P")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(73.8205695667116)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.20608132248769)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c26acf0c_a988_4e9c_a043_948814f6016e
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2908, 908, "Acetic Acid")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(393.069851558703)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.0923527503417189)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_58268f62_875c_4c41_824d_06c3e3ee052d
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 2460, 788, "Complex Column1")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding EnergyStream: EN_fe2e2577_6e39_4b0d_b7a1_baff57388fb3
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2276, 862, "E2")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_fa58c471_3b6e_4e80_8707_bfc81acd5a7d
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2369, 799, "Cooler O/P")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(297.567097)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.298434072869729)  # Mass Flow in kg/s

# Adding Cooler: RESF_4f82f70a_5a36_46b1_8bcb_c1bc090d8851
Cooler1 = sim.AddObject(ObjectType.Cooler, 2274, 797, "Cooler")
Cooler1 = Cooler1.GetAsObject()

# Adding EnergyStream: EN_a6d0dae4_8c65_4515_aa68_793661e61b62
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2063, 1002, "E1")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_47fdf717_51f9_4b2b_b070_989fe840552a
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2200, 959, "Null")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(1185.95411491573)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_22c73400_c342_4f29_b851_f28e8054db2f
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2156, 798, "Reactor O/P")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(1185.95411491573)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.298434072869729)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_34c30a35_ab0a_4be6_a9b3_44c9755cdac1
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 2072, 927, "Conversion Reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()
print("Reactor_Conversion1")
# Adding MaterialStream: MAT_eb6b5df8_0ee2_4e90_b956_fd679c69bd7a
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2014, 943, "Mix. O/P")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(297.581289014064)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.298434072869729)  # Mass Flow in kg/s

# Adding NodeIn: MIST_730be960_09b4_4517_af5d_da1e3b4bbdad
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1934, 942, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_04022439_0e38_4f23_a4fd_c79659a0dc41
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1831, 965, "Air")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(298.15)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.173540383333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_944b5665_bcf4_41cf_b8d9_10e4e1cfd0fc
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1841, 896, "Acetaldehyde")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(298.15)  # Temperature in K
MaterialStream15.SetPressure(101325)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.0686627777777778)  # Mass Flow in kg/s
print("MaterialStream15")
# Adding MaterialStream: MAT_376ddcce_b8fa_4995_b449_6739c5fd4953
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2402, 918, "Fresh Water")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(298.15)  # Temperature in K
MaterialStream16.SetPressure(101325)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.000277777777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4ad546a6_4f69_48e9_a382_2b795bc56956
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2567, 961, "Mix o/p")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(358.898050023644)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.0592533351918145)  # Mass Flow in kg/s

# Adding NodeIn: MIST_07624089_cdfd_4ce5_ad2c_7dc7d0fae209
Mixer2 = sim.AddObject(ObjectType.NodeIn, 2504, 966, "Mixer2")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_8c2d3946_b12d_4ee6_8fd7_bafb110a2a8d
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2716, 797, "Vapor stream")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(79.5345996834723)  # Temperature in K
MaterialStream18.SetPressure(101325)  # Pressure in Pa
MaterialStream18.SetMassFlow(0.20608132248769)  # Mass Flow in kg/s

# Adding Cooler: RESF_157faa20_c073_4c3c_834e_9cb27722e837
Cooler2 = sim.AddObject(ObjectType.Cooler, 2631, 958, "Cooler2")
Cooler2 = Cooler2.GetAsObject()
print("Cooler2")
# Adding MaterialStream: MAT_c656cf1b_92c0_400d_bd73_a938f8ac91c7
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2719, 964, "Cool water")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(288.15)  # Temperature in K
MaterialStream19.SetPressure(101325)  # Pressure in Pa
MaterialStream19.SetMassFlow(0.0592533351918145)  # Mass Flow in kg/s

# Adding EnergyStream: EN_b8957637_744c_40b5_8b4c_0ff9fa404fc0
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2634, 1028, "E4")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding OT_Recycle: REC_1146094c_4d40_4667_9b30_32996d8f313f
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 2110, 1267, "Acetaldehyde recycle1")
Recycle2 = Recycle2.GetAsObject()

sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
sim.ConnectObjects(MaterialStream12.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream12 to Cooler1
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream3 to Mixer2
sim.ConnectObjects(EnergyStream1.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream1 to Heater1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream8
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream12
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream15 to Mixer1
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Heater2 to MaterialStream18
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Mixer1 to MaterialStream13
sim.ConnectObjects(MaterialStream10.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream10 to CapeOpenUO3
sim.ConnectObjects(MaterialStream18.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream18 to CapeOpenUO2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream11
sim.ConnectObjects(MaterialStream14.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream14 to Mixer1
# sim.ConnectObjects(MaterialStream19.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream19 to CapeOpenUO2
sim.ConnectObjects(MaterialStream8.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream8 to Heater2
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO1
sim.ConnectObjects(MaterialStream16.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream16 to Mixer2
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream9
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # Cooler2 to EnergyStream5
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # Cooler1 to EnergyStream3
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Recycle1 to MaterialStream3
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle2 to MaterialStream1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Cooler1 to MaterialStream10
sim.ConnectObjects(MaterialStream17.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream17 to Cooler2
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_Conversion1
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Heater1 to MaterialStream2
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Mixer2 to MaterialStream17
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Cooler2 to MaterialStream19
sim.ConnectObjects(EnergyStream2.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream2 to Heater2
sim.ConnectObjects(MaterialStream5.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream5 to Heater1
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream2 to Recycle2
sim.ConnectObjects(MaterialStream13.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream13 to Reactor_Conversion1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_60.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_60.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

