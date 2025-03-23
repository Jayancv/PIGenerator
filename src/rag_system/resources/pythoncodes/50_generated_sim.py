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
ethyl_acetate = sim.AvailableCompounds["Ethyl acetate"]
sim.SelectedCompounds.Add(ethyl_acetate.Name, ethyl_acetate)
acetic_acid = sim.AvailableCompounds["Acetic acid"]
sim.SelectedCompounds.Add(acetic_acid.Name, acetic_acid)

# Adding Simulation Objects
# Adding MaterialStream: MAT_6a2a4145_10c2_48a2_917b_b28648d3904f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1771, 786, "To treatment")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(371.33063607153)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.921509469846599)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_75e900b7_61f8_4967_a58a_d0d4fec85a71
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1770, 679, "Top Product 2")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(359.871270266231)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0758509225663981)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a417a92a_a2c8_40e3_9e3c_d96fd11dd00e
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1609, 783, "Steam")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(373.15)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.018381254)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_117f0627_0dbf_44c8_a4f2_89af711b5964
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1690, 716, "Solvent Recovery")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_e042956d_b758_4cb3_9996_c05ca578f744
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1611, 706, "Recovery Feed")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.978979134184117)  # Mass Flow in kg/s

# Adding NodeIn: MIST_6fe10187_f9f5_42b1_b281_ee06625b22fc
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1528, 709, "Mixer 1")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_65d1b42b_a79e_4824_98cf_d2e1996c7437
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1512, 626, "Water")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.256472281242369)  # Mass Flow in kg/s

# Adding EnergyStream: EN_d9635e06_f7c8_4e32_a2b7_692dd4cddeb6
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1313, 566, "Energy Stream 1")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_ca15181b_56ad_4c7a_8f24_0583703325ba
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1333, 521, "25 C 1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(4.01015355452879)  # Mass Flow in kg/s

# Adding Cooler: RESF_b620a124_a168_451a_abd4_e67e917ed41f
Cooler1 = sim.AddObject(ObjectType.Cooler, 1270, 519, "Cooler 1")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_81da79b6_0c83_4530_bd00_475aa967a9d3
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1080, 743, "Raffinate")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.722506852941749)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a60f7fc5_7505_493d_ab16_789ed74f1c7a
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1071, 549, "Extract")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(298.15)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(4.37062058856455)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7e83f13f_24be_4fc8_9499_73cef9885103
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 911, 553, "Acid Water Feed")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(298.15)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.26355479121893)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_4ddfca2a_bf02_483d_b0a2_88c9ceaf0b06
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 971, 582, "Extraction")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_03327f2c_9c7e_4d99_aa84_d5450f9888bd
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1209, 624, "Acid Product")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(389.12790696692)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.360467034035801)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8738027c_164a_4f97_ace7_83a8328125f8
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1205, 518, "Top Product 1")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(346.149930675846)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(4.01015355452879)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_c076d961_16c0_40dc_bd28_59b304316302
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1127, 563, "Acid Recovery")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding Cooler: RESF_b2f7df77_b60d_45c3_a21c_b3689856c749
Cooler2 = sim.AddObject(ObjectType.Cooler, 1853, 676, "Cooler 2")
Cooler2 = Cooler2.GetAsObject()

# Adding EnergyStream: EN_34408186_1e42_4faf_a2f9_4b74c5b7d7a5
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1861, 739, "Energy Stream 2")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_5e5b47dc_78b7_4469_bb86_b0388c494233
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1941, 678, "25 C 2")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(298.15)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.0758509225663981)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0c9ce7bf_cadc_4f5c_8748_512948f1590a
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1288, 861, "MakeUp EA")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(298.15)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.01110117)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_62f6a2e5_5a77_4141_898f_685d0625bcd7
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 1474, 496, "Decanter")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()

# Adding MaterialStream: MAT_3fabacdd_0fbc_4776_9114_545ae1765db3
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1256, 804, "Recycle")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(298.15)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(3.82956467462503)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_3457360f_0b32_4d0b_863b_d804040f0b4a
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 911, 735, "REC-028")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_ecf4445f_e4de_4446_bd95_abe24ea3bbc2
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 882, 616, "Solvent")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(298.15)  # Temperature in K
MaterialStream15.SetPressure(101325)  # Pressure in Pa
MaterialStream15.SetMassFlow(3.84066584462503)  # Mass Flow in kg/s

# Adding NodeIn: MIST_de888242_21df_4003_918a_8746876e31ad
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1196, 833, "MIX-028")
Mixer2 = Mixer2.GetAsObject()

# Adding OT_Recycle: REC_b521b166_d960_455f_a1e7_558db1527025
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1915, 537, "REC-024")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_73f90623_3310_4d02_abfc_aa4937c0166e
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1128, 837, "MSTR-027")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(298.15)  # Temperature in K
MaterialStream16.SetPressure(101325)  # Pressure in Pa
MaterialStream16.SetMassFlow(3.84066584462503)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_85a85ee4_16c6_46c4_85b6_e6378fb713d0
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1822, 487, "MSTR-028")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(298.15)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.0758509225663981)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO3
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Mixer2 to MaterialStream16
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream5
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO4
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Cooler1 to MaterialStream6
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # Cooler2 to EnergyStream2
sim.ConnectObjects(MaterialStream16.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream16 to Recycle1
sim.ConnectObjects(MaterialStream11.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream11 to Cooler1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream10
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Recycle1 to MaterialStream15
sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO2
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO1
sim.ConnectObjects(MaterialStream12.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream12 to Recycle2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Mixer1 to MaterialStream4
# sim.ConnectObjects(MaterialStream15.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream15 to CapeOpenUO2
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream7 to Mixer1
sim.ConnectObjects(MaterialStream14.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream14 to Mixer2
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream14
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream5 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(MaterialStream2.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream2 to Cooler2
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Recycle2 to MaterialStream17
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Cooler2 to MaterialStream12
# sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream11
# sim.ConnectObjects(MaterialStream17.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream17 to CapeOpenUO4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_50.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_50.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

