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
acetone = sim.AvailableCompounds["Acetone"]
sim.SelectedCompounds.Add(acetone.Name, acetone)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
isopropanol = sim.AvailableCompounds["Isopropanol"]
sim.SelectedCompounds.Add(isopropanol.Name, isopropanol)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)

# Adding Simulation Objects
# Adding EnergyStream: EN_6676eecc_a153_43fd_8ac6_5c9e9a9f1f4c
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2448, 1103, "r1 duty")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_b835f4c4_2095_4be1_912e_003c063e82b0
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2409, 886, "Vent")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(351.215390812672)  # Temperature in K
MaterialStream1.SetPressure(202650)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.000750196326146782)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4fe1dfc0_8634_4321_8721_63fc0304b4f4
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2081, 988, "Absorber Gas")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(287.145347663719)  # Temperature in K
MaterialStream2.SetPressure(151987.5)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0945043163085917)  # Mass Flow in kg/s

# Adding EnergyStream: EN_81dc1d6f_351b_41ab_9b4c_dd7968bb9018
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1714, 1146, "Energy Flash")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_cd547fab_0a71_44de_ab58_0fe5a61e5417
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2078, 1166, "Absorber Bottoms")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(319.154537376282)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.10055886336588)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9f05ab0f_3b86_45e3_a497_3e803e7442ac
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1837, 1014, "Gas")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.630071060633)  # Temperature in K
MaterialStream4.SetPressure(263445)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0949800272090703)  # Mass Flow in kg/s

# Adding NodeIn: MIST_c6586ccd_6d22_4e37_9b85_97ab52a80705
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2174, 1193, "Mixer 2")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_edb8f4e5_7adc_48ea_9c53_c0eb89b6c365
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2075, 1216, "Liquid")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(247.633754539248)  # Temperature in K
MaterialStream5.SetPressure(263445)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.646119935098183)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_626a8e4f_86c5_43ec_a9fb_9be9b62bad81
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1750, 905, "Liquid Outlet Zero")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(426.372274945605)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0)  # Mass Flow in kg/s

# Adding EnergyStream: EN_72f83d69_57be_4f51_9bc1_592c9cbb96c1
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1607, 945, "LP Steam For Energy")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding HeaterCooler: RESF_dd42e482_b2f4_420d_b6bb_87d5a69d9300
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1956, 726, "HX 1")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding EnergyStream: EN_01cd6596_f71a_48a1_9117_9b3e5555ea44
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1779, 820, "Energy Reactor")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding EnergyStream: EN_97a17dd2_8a40_4d4e_a974_7fa8550360db
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2065, 788, "Refrig.")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_783c54bd_a38c_48fc_b887_188790bc488a
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1882, 834, "No Outlet")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(623)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0e522a2d_a50c_40ae_8a4c_d713770f502b
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2010, 729, "HX 2 IN")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(297.695665131469)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.74110009965)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_dc1a457c_9a69_46c2_b4bc_98090ba4b5a1
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 2065, 727, "HX 2")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding MaterialStream: MAT_45c9da49_d489_46f2_bebf_db116f8ea4bf
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1705, 1053, "To Flash tank")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(286.080101440396)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.74110009965)  # Mass Flow in kg/s

# Adding EnergyStream: EN_0bd553df_3055_49c6_9779_c9360f96ae70
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1999, 781, "CW")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding RCT_Conversion: RC_70985f95_87a7_4c74_b757_0c1b971d12ab
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1803, 755, "Reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_7a0639f4_03ed_4adc_9854_ed8e0a059160
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1888, 729, "Rout")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(623)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.74110009965)  # Mass Flow in kg/s

# Adding Vessel: SEP_6507a3e1_a9a7_4ff5_80db_3fbc78bc750b
Separator1 = sim.AddObject(ObjectType.Vessel, 1624, 815, "Vaporizer")
Separator1 = Separator1.GetAsObject()

# Adding MaterialStream: MAT_9d92c0b5_8192_425d_945d_ac74bcdfe519
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1440, 858, "Feed")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(320)  # Temperature in K
MaterialStream11.SetPressure(263445)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.666953797)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_267259e1_caed_4994_a32e_501c5e7770ec
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1506, 753, "Recycle")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(389)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.07414630265)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_87189bfc_ccd1_4271_8d8a_3cb967428530
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1584, 844, "To Vaporizer")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(351.465971740365)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.74110009965)  # Mass Flow in kg/s

# Adding NodeIn: MIST_63c32771_a932_431d_aede_6caea5f71f2a
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1530, 844, "Mixer")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_4e3292b7_5374_4e6e_87fe_ac842b2c7130
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1741, 773, "Rin")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(426.372274945605)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.74110009965)  # Mass Flow in kg/s

# Adding Vessel: SEP_a88c2ff0_bc55_4905_843f_52418b1d1470
Separator2 = sim.AddObject(ObjectType.Vessel, 1766, 1049, "Flash Tank")
Separator2 = Separator2.GetAsObject()

# Adding AbsorptionColumn: ABS_473ff3cf_8d30_434b_9b9c_376d7b6e4a42
AbsorptionColumn1 = sim.AddObject(ObjectType.AbsorptionColumn, 1902, 999, "Absorber")
AbsorptionColumn1 = AbsorptionColumn1.GetAsObject()

# Adding MaterialStream: MAT_07e2b555_6467_4f3d_ab03_fa111aa87f7f
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1840, 952, "Water")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(320)  # Temperature in K
MaterialStream15.SetPressure(101325)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.100083333333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_78f9dc9d_6b87_4fdb_8435_8e41b506a9bb
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2213, 1037, "Distill IN")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(230.466022635514)  # Temperature in K
MaterialStream16.SetPressure(101325)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.746678798464063)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_291237bc_bb69_4e3f_8589_1b54131d4e31
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2281, 964, "C1")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_9896483d_38c5_41a2_b92f_9fcea260c41b
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2466, 969, "c1 duty")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_c18bba9d_fa5c_4c71_a7e5_2c822cf21b7b
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2474, 1008, "Acetone Product")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(292.518989037249)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.486640675850956)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_63f1014d_c302_483a_99d4_e544e3eaa6ba
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2535, 1065, "B1")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(344.986851777473)  # Temperature in K
MaterialStream18.SetPressure(303975)  # Pressure in Pa
MaterialStream18.SetMassFlow(0.259233080023351)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_e15cf285_913e_43d6_8c43_9f3bb6b37f17
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 2602, 965, "C2")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding EnergyStream: EN_c2322acd_f9c6_4d64_9081_2ec367b1d862
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2770, 1103, "r2 duty")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding MaterialStream: MAT_0d2b4a48_c4f4_4a37_a979_43e5fddcac92
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2768, 1160, "Water Product")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(374.057338661067)  # Temperature in K
MaterialStream19.SetPressure(101325)  # Pressure in Pa
MaterialStream19.SetMassFlow(0.184454847040033)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d17649a9_1a5d_4a74_8b5d_265b208405a6
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2784, 936, "To Recycle")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(319.238759504888)  # Temperature in K
MaterialStream20.SetPressure(101325)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.0747528333600706)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3d6ec183_c873_4100_8f7f_abfbfffa7a4f
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2809, 980, "c2 duty")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding OT_Recycle: REC_aeaee497_f761_4a93_a2c6_c70d6e08b220
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2324, 668, "REC-039")
Recycle1 = Recycle1.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream17)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream18)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream7)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream1)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream20)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream19)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream9)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream8)  # ConnectReboilerDuty 
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Separator1 to MaterialStream6
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream9
sim.ConnectObjects(EnergyStream2.GraphicObject, Separator2.GraphicObject, -1, -1)  # EnergyStream2 to Separator2
sim.ConnectObjects(MaterialStream20.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream20 to Recycle1
sim.ConnectObjects(AbsorptionColumn1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # AbsorptionColumn1 to MaterialStream3
sim.ConnectObjects(MaterialStream16.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream16 to DistillationColumn1
sim.ConnectObjects(MaterialStream4.GraphicObject, AbsorptionColumn1.GraphicObject, -1, -1)  # MaterialStream4 to AbsorptionColumn1
sim.ConnectObjects(MaterialStream8.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream8 to HeaterCooler2
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Separator1 to MaterialStream14
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream11 to Mixer2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Mixer1 to MaterialStream16
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream8
sim.ConnectObjects(MaterialStream18.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream18 to DistillationColumn2
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Mixer2 to MaterialStream13
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream10
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(MaterialStream14.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream14 to Reactor_Conversion1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Recycle1 to MaterialStream12
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream5 to Mixer1
sim.ConnectObjects(MaterialStream10.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream10 to HeaterCooler1
sim.ConnectObjects(HeaterCooler2.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # HeaterCooler2 to EnergyStream5
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream12 to Mixer2
sim.ConnectObjects(EnergyStream3.GraphicObject, Separator1.GraphicObject, -1, -1)  # EnergyStream3 to Separator1
sim.ConnectObjects(MaterialStream13.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream13 to Separator1
sim.ConnectObjects(MaterialStream9.GraphicObject, Separator2.GraphicObject, -1, -1)  # MaterialStream9 to Separator2
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Separator2 to MaterialStream4
sim.ConnectObjects(DistillationColumn1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # DistillationColumn1 to MaterialStream1
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Separator2 to MaterialStream5
sim.ConnectObjects(AbsorptionColumn1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # AbsorptionColumn1 to MaterialStream2
sim.ConnectObjects(MaterialStream15.GraphicObject, AbsorptionColumn1.GraphicObject, -1, -1)  # MaterialStream15 to AbsorptionColumn1
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream6
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream7
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_63.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_63.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

