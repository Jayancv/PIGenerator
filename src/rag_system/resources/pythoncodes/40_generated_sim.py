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
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)

# Adding Simulation Objects
# Adding OT_Recycle: REC_9a795370_ec85_4055_aefe_b8eceb9defaf
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1334, 502, "REC-035")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MSTR_97c1affd_195f_4010_95d3_c965e1d0c201
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1402, 503, "MSTR-020 (2)")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(278.100427403389)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.126302223140084)  # Mass Flow in kg/s

# Adding MaterialStream: MSTR_d155d5e5_baf6_4a87_a5fd_9f55fe711329
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1821, 832, "S-10")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(111.61125834913)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0904964008941862)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_ebe6a91f_cfdc_4277_92a6_683f69d5f23f
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1739, 828, "REC-033")
Recycle2 = Recycle2.GetAsObject()

# Adding NodeIn: MIST_da99b743_e96b_4f2d_a14b_2d168c28eff0
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1612, 717, "MIX-029")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_baa20d4a_2b43_44fa_9e91_d146ebe78722
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1424, 777, "ESTR-028")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_23960371_913e_478c_87be_8d83ebe95a49
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1545, 707, "S-12")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(137.012402881473)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.0356603313420558)  # Mass Flow in kg/s

# Adding CompressorExpander: TURB_2d6b8aa1_b826_4330_acd9_8c638b98a0ff
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1477, 706, "EXPANDER")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_363ec0d6_1fa1_4b05_b843_acf6a9d5ab0c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1885, 588, "S-9")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(111.611249154077)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0164845931319811)  # Mass Flow in kg/s

# Adding Vessel: SEP_8ed2ead8_c194_466f_8fa5_8961f90c4fdf
Separator1 = sim.AddObject(ObjectType.Vessel, 1710, 535, "SEPARATOR")
Separator1 = Separator1.GetAsObject()

# Adding MaterialStream: MAT_584f7966_3c6e_40e4_9434_0be66fb692ae
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1659, 581, "S-8")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(111.611258300496)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.106980994026167)  # Mass Flow in kg/s

# Adding Valve: VALV_75b5ef91_ac2c_4082_ad60_a7109d116b9a
Valve1 = sim.AddObject(ObjectType.Valve, 1595, 573, "VALV-021")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_00fb2c9d_3e1b_460a_acf4_4c77cdf2589c
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1274, 504, "S-14")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(278.100427403389)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.126302223140084)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1af7dc4d_a1e3_46ee_91f8_49d2b18e63fd
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1589, 383, "S-13")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(118.757353529624)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.126302223140084)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1d19e18d_d4f6_46dd_a54c_708034d7e2ac
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1535, 533, "S-7")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(198.499957525326)  # Temperature in K
MaterialStream8.SetPressure(6079500)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.106980994026167)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_01512df7_aca1_4a88_8cf8_b11f7b48e71c
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1477, 499, "REG-II")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_ee71615c_b471_4d48_aee4_7c59bb346688
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1426, 553, "S-6")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(292.011265322337)  # Temperature in K
MaterialStream9.SetPressure(6079500)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.106980994026167)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_755856b5_ea12_40d6_813f_52da70e78afa
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1408, 656, "S-11")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(292.011265322337)  # Temperature in K
MaterialStream10.SetPressure(6079500)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.0356603313420558)  # Mass Flow in kg/s

# Adding NodeOut: DIV_bf40d546_8498_47ab_9438_d270dc073991
Splitter1 = sim.AddObject(ObjectType.NodeOut, 1361, 598, "SPLT-014")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_14ff96fe_13ad_4a00_bf9a_afa3dc02180c
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1154, 704, "S-15")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(289.147472958413)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.126492870163161)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8bc39dd2_5e67_4a4e_b251_622f4454c5c7
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1295, 585, "S-5")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(292.011265275903)  # Temperature in K
MaterialStream12.SetPressure(6079500)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.142641325368223)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_cafd3dfb_9c1b_40f8_ae11_23d707c35422
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 1226, 565, "REG-I")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_26754cba_3bad_4b25_ab51_00c7c13ab0ad
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 674, 556, "Gas Feed")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(298.15)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.016043)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7b542a98_3292_4244_a4a4_94534122d01a
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 869, 565, "S-2")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(290.181221225196)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.142641325368223)  # Mass Flow in kg/s

# Adding NodeIn: MIST_560be1e9_d7e6_413b_b7a3_802dd08df1b5
Mixer2 = sim.AddObject(ObjectType.NodeIn, 797, 564, "MIX-002")
Mixer2 = Mixer2.GetAsObject()

# Adding CompressorExpander: COMP_a5f9303b_2ea0_41ea_96b5_47bdacf23901
AdiabaticExpanderCompressor2 = sim.AddObject(ObjectType.Compressor, 936, 563, "COMPRESSOR")
AdiabaticExpanderCompressor2 = AdiabaticExpanderCompressor2.GetAsObject()

# Adding MaterialStream: MAT_2035f100_4b31_45cb_831d_0cb8223d0700
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1006, 565, "S-3")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(725.671669373451)  # Temperature in K
MaterialStream15.SetPressure(6079500)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.142641325368223)  # Mass Flow in kg/s

# Adding EnergyStream: EN_a1fb3901_6bd3_460a_8a68_c514f8a664af
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 880, 625, "ESTR-006")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding HeaterCooler: RESF_52e275a4_4ae8_4136_96e5_4e8895b476e4
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1079, 565, "COOLER")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_c77f5edc_bea4_45b8_af42_a9c606a0a396
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1171, 573, "S-4")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(300.000000196622)  # Temperature in K
MaterialStream16.SetPressure(6079500)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.142641325368223)  # Mass Flow in kg/s

# Adding EnergyStream: EN_d0e933fd_0a7e_4c04_8037_74dfac085235
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1139, 620, "ESTR-009")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_bdb16a67_f94d_4dae_8a3c_55cf85609055
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 748, 694, "MSTR-029")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(289.147472958413)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.126492870163161)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_df101802_09fd_4298_948b_04215e3fe4a8
Recycle3 = sim.AddObject(ObjectType.OT_Recycle, 949, 694, "REC-028")
Recycle3 = Recycle3.GetAsObject()

# Adding MaterialStream: MSTR_d4da36be_bab3_43ce_9279_a702b6d57145
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1668, 824, "MSTR-024-2")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(111.61125834913)  # Temperature in K
MaterialStream18.SetPressure(101325)  # Pressure in Pa
MaterialStream18.SetMassFlow(0.0904964008941862)  # Mass Flow in kg/s

sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to MaterialStream15
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
# sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to EnergyStream1
sim.ConnectObjects(Recycle3.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Recycle3 to MaterialStream17
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Valve1 to MaterialStream5
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream2 to Recycle2
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Separator1 to MaterialStream2
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Splitter1 to MaterialStream10
sim.ConnectObjects(MaterialStream7.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream7 to HeatExchanger1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Recycle1 to MaterialStream6
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer1 to MaterialStream7
sim.ConnectObjects(MaterialStream17.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream17 to Mixer2
sim.ConnectObjects(MaterialStream15.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream15 to HeaterCooler1
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Recycle2 to MaterialStream18
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream3
sim.ConnectObjects(MaterialStream1.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream1 to Recycle1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Splitter1 to MaterialStream9
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream11
sim.ConnectObjects(MaterialStream6.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream6 to HeatExchanger2
sim.ConnectObjects(MaterialStream18.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream18 to Mixer1
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Mixer2 to MaterialStream14
sim.ConnectObjects(MaterialStream12.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream12 to Splitter1
sim.ConnectObjects(MaterialStream14.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # MaterialStream14 to AdiabaticExpanderCompressor2
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream16
sim.ConnectObjects(MaterialStream8.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream8 to Valve1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Separator1 to MaterialStream4
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream3
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream12
sim.ConnectObjects(MaterialStream5.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream5 to Separator1
sim.ConnectObjects(MaterialStream10.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream10 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream9.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream9 to HeatExchanger1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream8
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(MaterialStream11.GraphicObject, Recycle3.GraphicObject, -1, -1)  # MaterialStream11 to Recycle3
sim.ConnectObjects(MaterialStream16.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream16 to HeatExchanger2
sim.ConnectObjects(EnergyStream2.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # EnergyStream2 to AdiabaticExpanderCompressor2
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_40.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_40.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

