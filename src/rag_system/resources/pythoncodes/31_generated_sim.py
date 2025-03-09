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
carbon_monoxide = sim.AvailableCompounds["Carbon monoxide"]
sim.SelectedCompounds.Add(carbon_monoxide.Name, carbon_monoxide)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_1784b3b6_2815_48e1_948f_83d607e0fcd6
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1225, 871, "feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(298.15)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.03254573)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_5d578a67_deb6_48f0_8f69_81e81fa2be9a
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1309, 869, "compressor")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding EnergyStream: EN_c08cfca6_fedd_4f99_ae92_eb87f0406b41
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1229, 933, "ESTR-002")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_0110bd5a_3dbd_434d_b3eb_5170d1f95779
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1409, 872, "compressed feed")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(1757.01044609301)  # Temperature in K
MaterialStream2.SetPressure(30397500)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.03254573)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_7a5d9f40_70c5_4944_ba5e_16cffb412d60
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1765, 853, "convertion reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_2f25cf6a_30d8_40fa_9729_cb202ae7994c
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1904, 853, "product")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(2347.63917565472)  # Temperature in K
MaterialStream3.SetPressure(30397500)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.0650914600000416)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_32d38aa8_a27b_428b_9db7_d9927b672e4d
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1894, 944, "MSTR-006")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(2347.63917565472)  # Temperature in K
MaterialStream4.SetPressure(30397500)  # Pressure in Pa
MaterialStream4.SetMassFlow(0)  # Mass Flow in kg/s

# Adding EnergyStream: EN_67245b3b_011d_468b_b5f3_a438f778e453
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1736, 941, "reactor energy")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding HeaterCooler: RESF_eba77b2d_6de8_41d4_a730_181a3760122a
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 2008, 852, "COOL-008")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_be96ee96_159f_420f_bafb_7b5dec567a60
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2120, 853, "cooled product")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(30397500)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0650914600000416)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4dda176c_cac7_4b36_948e_9f5cba35bffc
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2063, 904, "ESTR-010")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding Vessel: SEP_29e4298c_3612_44f0_94cd_d47366326dce
Separator1 = sim.AddObject(ObjectType.Vessel, 2225, 854, "gas liquid seperator")
Separator1 = Separator1.GetAsObject()

# Adding MaterialStream: MAT_062b2345_52d3_43b4_a115_048ff8d357c3
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2310, 791, "gases from separator")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(30397500)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.0241997972795862)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a0498b2a_dbfd_4c62_93cf_62881635e2cd
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2353, 941, "methanol with some impurities")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(30397500)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.0408916673422789)  # Mass Flow in kg/s

# Adding EnergyStream: EN_d3d3d445_2cc5_49ab_8a0b_1fc61d2301d8
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2208, 973, "energy for g-l separator")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding ComponentSeparator: CS_31e73222_1e13_4d04_827a_5666e78fe23f
ComponentSeparator1 = sim.AddObject(ObjectType.ComponentSeparator, 2783, 1079, "CS-034")
ComponentSeparator1 = ComponentSeparator1.GetAsObject()

# Adding ComponentSeparator: CS_10506b7c_d182_49b1_b2ee_cc5d3dcc54e6
ComponentSeparator2 = sim.AddObject(ObjectType.ComponentSeparator, 2387, 718, "compound seperator")
ComponentSeparator2 = ComponentSeparator2.GetAsObject()

# Adding MaterialStream: MAT_95599169_28f9_4820_90fb_56e9f8072931
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2186, 693, "MSTR-017")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(298.15)  # Temperature in K
MaterialStream8.SetPressure(30397500)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.03254573)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_73a388e4_b4c2_452d_b178_f677d10eff99
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2510, 827, "waste gases")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(298.15)  # Temperature in K
MaterialStream9.SetPressure(30397500)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.0232026656623432)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5e30afac_d727_4c8c_a9ae_488d600fd2c4
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2422, 816, "ESTR-019")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_e52da5f7_605b_4d87_9788_1bd74d87e9fb
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2483, 1035, "ESTR-025")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_b6e3e54b_936b_4c7d_bc79_5dcb168c234a
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2552, 979, "MSTR-024")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(299.251193306702)  # Temperature in K
MaterialStream10.SetPressure(1418550)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.0408916673422789)  # Mass Flow in kg/s

# Adding CompressorExpander: TURB_a614ee27_8dd5_4944_8d37_50aa40c9e7bd
AdiabaticExpanderCompressor2 = sim.AddObject(ObjectType.Compressor, 2450, 976, "depressurizer")
AdiabaticExpanderCompressor2 = AdiabaticExpanderCompressor2.GetAsObject()

# Adding NodeIn: MIST_78028ab2_3ba2_41a8_9716_b376ed336d84
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1543, 821, "MIX-023")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_4eea8781_50ab_4c16_9146_59363e123098
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1689, 837, "MSTR-024")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(1052.12505230205)  # Temperature in K
MaterialStream11.SetPressure(30397500)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.0650914600000416)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2c3fc6fa_4dc3_4034_a3cb_4e97a93a94c0
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1599, 684, "MSTR-025")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(298.15)  # Temperature in K
MaterialStream12.SetPressure(30397500)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.0325457300000416)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_0a9024ef_ebb5_4164_b7f9_6b2c98b47b37
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1932, 694, "REC-026")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_83920990_f336_4a6a_b652_f9e75545889f
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2929, 917, "Methanol")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(299.251192923972)  # Temperature in K
MaterialStream13.SetPressure(1418550)  # Pressure in Pa
MaterialStream13.SetMassFlow(3.2042)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_207ec7e6_5c40_4590_bef3_8bb96ff4e2e2
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2874, 1110, "remaining liquid")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(299.251193306702)  # Temperature in K
MaterialStream14.SetPressure(1418550)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.0119799779233508)  # Mass Flow in kg/s

# Adding EnergyStream: EN_afa03315_6958_4852_bca4_3651cba91a31
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2848, 1165, "ESTR-030")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding Vessel: SEP_62dc9881_c161_48ca_b06a_b68d2c0d81ba
Separator2 = sim.AddObject(ObjectType.Vessel, 2624, 980, "separator of liquida and gas")
Separator2 = Separator2.GetAsObject()

# Adding EnergyStream: EN_249c0a01_63e3_4fa9_94bc_7f754bba6e2e
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2578, 1085, "ESTR-032")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding MaterialStream: MAT_e6df0ec9_4746_41ed_896c_d4b5ef041f6f
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2710, 942, "MSTR-033")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(299.251193306702)  # Temperature in K
MaterialStream15.SetPressure(1418550)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.00204724528506825)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_cdcce1f8_e73a_4d2a_ab12_07308bc99cca
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2707, 1094, "MSTR-034")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(299.251193306702)  # Temperature in K
MaterialStream16.SetPressure(1418550)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.0388444220208631)  # Mass Flow in kg/s

sim.ConnectObjects(EnergyStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Mixer1 to MaterialStream11
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream2
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream5
sim.ConnectObjects(MaterialStream3.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream3 to HeaterCooler1
sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to MaterialStream10
sim.ConnectObjects(ComponentSeparator2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # ComponentSeparator2 to MaterialStream9
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Separator1 to MaterialStream7
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream3
sim.ConnectObjects(MaterialStream8.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream8 to Recycle1
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Separator2 to MaterialStream15
sim.ConnectObjects(MaterialStream11.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream11 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream6.GraphicObject, ComponentSeparator2.GraphicObject, -1, -1)  # MaterialStream6 to ComponentSeparator2
sim.ConnectObjects(EnergyStream2.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream2 to Reactor_Conversion1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Recycle1 to MaterialStream12
sim.ConnectObjects(ComponentSeparator2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # ComponentSeparator2 to MaterialStream8
# sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to EnergyStream6
sim.ConnectObjects(MaterialStream7.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # MaterialStream7 to AdiabaticExpanderCompressor2
sim.ConnectObjects(MaterialStream5.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream5 to Separator1
sim.ConnectObjects(ComponentSeparator2.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # ComponentSeparator2 to EnergyStream5
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream13
sim.ConnectObjects(MaterialStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream12 to Mixer1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # ComponentSeparator1 to EnergyStream7
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream4
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream3
sim.ConnectObjects(Separator2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Separator2 to MaterialStream16
sim.ConnectObjects(EnergyStream8.GraphicObject, Separator2.GraphicObject, -1, -1)  # EnergyStream8 to Separator2
sim.ConnectObjects(MaterialStream10.GraphicObject, Separator2.GraphicObject, -1, -1)  # MaterialStream10 to Separator2
sim.ConnectObjects(EnergyStream4.GraphicObject, Separator1.GraphicObject, -1, -1)  # EnergyStream4 to Separator1
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream14
sim.ConnectObjects(MaterialStream16.GraphicObject, ComponentSeparator1.GraphicObject, -1, -1)  # MaterialStream16 to ComponentSeparator1
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Separator1 to MaterialStream6
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_31.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_31.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

