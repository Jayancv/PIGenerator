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
tetrahydrofuran = sim.AvailableCompounds["Tetrahydrofuran"]
sim.SelectedCompounds.Add(tetrahydrofuran.Name, tetrahydrofuran)
ethylene_glycol = sim.AvailableCompounds["Ethylene glycol"]
sim.SelectedCompounds.Add(ethylene_glycol.Name, ethylene_glycol)

# Adding Simulation Objects
# Adding EnergyStream: EN_4ed1d521_019c_409d_ae35_e2aa73974ff0
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1269, 954, "Energy Stream")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_11a0434f_3a4b_49c2_8e62_4928f3de6ff1
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1100, 812, "Recyle Feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(320)  # Temperature in K
MaterialStream1.SetPressure(111457.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.828237824279818)  # Mass Flow in kg/s

# Adding NodeIn: MIST_cb430afe_7606_4d09_8952_2e23c6821ee7
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1096, 862, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_4dff83f3_02cf_48be_99f7_1d0b71fc879e
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1353, 892, "Recycle Stream")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(472.841669395627)  # Temperature in K
MaterialStream2.SetPressure(111458)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.828236029516106)  # Mass Flow in kg/s

# Adding Cooler: RESF_1eee5670_478a_4615_a00c_3a89019c2148
Cooler1 = sim.AddObject(ObjectType.Cooler, 1279, 888, "Cooler")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_bd0fd828_c09c_4adf_bb39_04d5e578bbde
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1206, 890, "Cold Recycle")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(320)  # Temperature in K
MaterialStream3.SetPressure(111458)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.827237824279818)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_d6d53e71_268e_4afc_a80e_a97666b86de7
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1425, 893, "REC-008")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_4da22c8b_4d4c_4ff5_8fca_7689bdda280e
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1443, 809, "99.9 wt % Ethlylene Glycol")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(472.841669395627)  # Temperature in K
MaterialStream4.SetPressure(111458)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.828236029516106)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7a9e0597_8d28_4aed_9121_3477b2186d56
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1444, 736, "88 wt % Water")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(348.978742401392)  # Temperature in K
MaterialStream5.SetPressure(111458)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0949827070503748)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_23d43790_4f36_4807_93a9_e9802a643a58
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1351, 773, "Column-II")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_b9092e77_bddc_4239_8944_00c61c06af3e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1266, 785, "Bottom-I")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(412.701614209286)  # Temperature in K
MaterialStream6.SetPressure(111458)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.92321873656643)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_06a945f9_8dfb_443e_a1bc_ab8ecc4c9cf4
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1267, 737, "99.9 wt. % THF")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(342.038743332854)  # Temperature in K
MaterialStream7.SetPressure(111458)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.738351760623911)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_94e091e9_cb5d_4657_ad05_816438606a7f
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1145, 902, "Make Up")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(320)  # Temperature in K
MaterialStream8.SetPressure(111457.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.001)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_f365371f_53bf_459f_aed3_2e662d29d8db
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1176, 765, "Column-I")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_363bb51a_f88a_4cc4_b2a7_494f1c67ca8a
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1086, 757, "Feed")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(320)  # Temperature in K
MaterialStream9.SetPressure(111457.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.833332672910512)  # Mass Flow in kg/s

sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO1
sim.ConnectObjects(MaterialStream2.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream2 to Cooler1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Cooler1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
# sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_61.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_61.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

