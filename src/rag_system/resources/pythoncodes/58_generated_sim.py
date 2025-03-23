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
methyl_methacrylate = sim.AvailableCompounds["Methyl methacrylate"]
sim.SelectedCompounds.Add(methyl_methacrylate.Name, methyl_methacrylate)
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_918415c8_ea59_4fb4_9de4_545492c20d6f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1090, 379, "Recycle")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(371.449392035164)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.256873136628168)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_0b65a612_50db_4fb4_b177_a7e8c0d2fee6
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1192, 380, "Recycle-I")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_17bf4f00_e82f_4a85_a4d4_cf70c05bfb07
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1247, 538, "99% MMA")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(373.166261477398)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.395525988138276)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7b8aef39_dcd8_46c0_b16b_cc8c4d754085
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1251, 424, "Distillate-II")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(371.449392035164)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.256873136628168)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_82b8cb1c_1179_46ac_9d82_db908a88b829
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1180, 451, "Column-II")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_553c5e52_4d38_41b1_a0ff_058d94f2644d
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1135, 572, "99% Water")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(323.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0645685205194379)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7e0800f4_bb86_4563_acb0_d60610a2c997
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1132, 459, "MMA, Water")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(323.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.652399124766439)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_b1575087_db5d_4707_b264_8c30819b0e18
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1051, 508, "Decanter")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding EnergyStream: EN_2a80d92f_c7ee_4f8d_ae3b_f3dfbdde2b95
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 864, 597, "Energy Stream")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_8434e744_995a_442b_8385_9384dc4e2dbb
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 999, 515, "Cold Feed")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(323.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.716967645285867)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_cc7d1c48_1dfc_4ace_953a_762bdc98281b
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 934, 523, "Mixed Feed")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(371.276346506658)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.716967645285867)  # Mass Flow in kg/s

# Adding Cooler: RESF_f36df9bc_128b_4ade_ab5c_9d11be6ce022
Cooler1 = sim.AddObject(ObjectType.Cooler, 933, 574, "Cooler")
Cooler1 = Cooler1.GetAsObject()

# Adding NodeIn: MIST_48a70b31_3399_4add_b34a_17045d65bdeb
Mixer1 = sim.AddObject(ObjectType.NodeIn, 933, 467, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_ce3a0fc0_221f_417b_9129_f6a556e3e2e3
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 831, 550, "Water, MMA")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(354.74417457051)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.46011020412521)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7f6e0a99_4c42_4efe_a62a_d42fa8f9d4d1
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 827, 414, "95.3% Methanol")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(339.503307899224)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.716126751430288)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_bb59baf1_3f70_4961_914d_40d1bfcfdcfc
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 682, 497, "Fresh Feed")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(298.15)  # Temperature in K
MaterialStream10.SetPressure(121590)  # Pressure in Pa
MaterialStream10.SetMassFlow(1.17623695555556)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_51e7752f_9459_4b89_85f3_b80a4b76ffac
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 738, 490, "Column-I")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(MaterialStream10.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream10 to CapeOpenUO3
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Cooler1 to MaterialStream6
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream8
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer1 to MaterialStream7
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(MaterialStream7.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream7 to Cooler1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream9
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
sim.ConnectObjects(MaterialStream3.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream3 to Recycle1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_58.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_58.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

