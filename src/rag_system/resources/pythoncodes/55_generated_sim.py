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
dioxane_1_4 = sim.AvailableCompounds["1,4-dioxane"]
sim.SelectedCompounds.Add(dioxane_1_4.Name, dioxane_1_4)
triethylamine = sim.AvailableCompounds["Triethylamine"]
sim.SelectedCompounds.Add(triethylamine.Name, triethylamine)

# Adding Simulation Objects
# Adding OT_Recycle: REC_022a95c0_2db9_486b_bf68_8cb9242283fa
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1655, 510, "R-1")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_ba5c2759_0f2e_457f_b7c9_09d8a891c2b6
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1322, 509, "Recycle")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(295.085738634879)  # Temperature in K
MaterialStream1.SetPressure(810600)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.188436111111111)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4d6e4b90_6e17_4a2e_b78f_547c2cfc187a
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1569, 856, "E-3")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_d95bba60_5ad4_4d89_892f_a17d4d9def52
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1597, 555, "E-4")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding NodeIn: MIST_fe377ea0_06cf_4741_9870_9eed6baa0551
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1306, 711, "M-1")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_6891f958_199f_40e0_ab0d_bafe119910a4
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1352, 721, "S-4")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(345.949985186803)  # Temperature in K
MaterialStream2.SetPressure(107404.5)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.515425)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4ea0b899_a4d1_47d6_9c9e_46929a56f45c
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1660, 793, "S-6")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(374.872483861046)  # Temperature in K
MaterialStream3.SetPressure(108417.75)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.228852777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6ad8e5c8_4cde_4511_a1e0_bd1469b2b1f2
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1659, 690, "S-5")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(362.487407414702)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.286540086982478)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_a0600e99_27c7_478a_ac77_075072e5fce6
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 1399, 618, "DC-2")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding DistillationColumn: DC_02ed207f_4d4f_46d8_a0bd_f2ce17b648e2
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 1786, 612, "DC-3")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding EnergyStream: EN_7c7549d5_bf25_43a8_8a1f_32622298f31a
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1980, 853, "E-6")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_900c3055_83c6_40f6_99b3_696836693c3e
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2011, 558, "E-5")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_fd26fd1b_7fa3_4c32_9868_bdcabefaddc8
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2076, 794, "S-8")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(460.004631711651)  # Temperature in K
MaterialStream5.SetPressure(825798.75)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0981277777777777)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3472b434_7fa0_4cbf_b77b_a574d5888b08
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2142, 656, "S-7")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(434.77040019683)  # Temperature in K
MaterialStream6.SetPressure(810600)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.188380627258364)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5dcae43c_fb8d_49be_adfa_885dd3d5e863
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 916, 685, "S-1")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(299)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.332233333333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b65d0a1e_dc55_4df4_a237_abfb900a1016
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1194, 590, "S-2")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(350.697551312682)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.00521665926288011)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1ca34964_3ce4_42d2_96e3_6619b898d865
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1228, 737, "S-3")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(365.669356736895)  # Temperature in K
MaterialStream9.SetPressure(107404.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.326988888888889)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_72a8e9f0_7107_486c_9afc_cb1b6f26e6ee
DistillationColumn3 = sim.AddObject(ObjectType.DistillationColumn, 983, 610, "DC-1")
DistillationColumn3 = DistillationColumn3.GetAsObject()

# Adding EnergyStream: EN_e7dc551d_82c1_4ba4_85af_4537d67f96b5
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1175, 514, "E-2")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_5dab8799_11c2_4f08_9f30_ce0ed05561c3
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1165, 827, "E-1")
EnergyStream6 = EnergyStream6.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream4)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream3)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream2)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream1)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream6)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream5)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream4)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream3)  # ConnectReboilerDuty 
DistillationColumn3.ConnectDistillate(MaterialStream8)  # ConnectDistillate 
DistillationColumn3.ConnectBottoms(MaterialStream9)  # ConnectBottoms 
DistillationColumn3.ConnectCondenserDuty(EnergyStream5)  # ConnectCondenserDuty 
DistillationColumn3.ConnectReboilerDuty(EnergyStream6)  # ConnectReboilerDuty 
sim.ConnectObjects(MaterialStream2.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream2 to DistillationColumn1
sim.ConnectObjects(MaterialStream7.GraphicObject, DistillationColumn3.GraphicObject, -1, -1)  # MaterialStream7 to DistillationColumn3
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream6 to Recycle1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream9 to Mixer1
sim.ConnectObjects(MaterialStream4.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream4 to DistillationColumn2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Mixer1 to MaterialStream2
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_55.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_55.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

