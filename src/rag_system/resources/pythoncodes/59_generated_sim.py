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
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_5707c86d_e93a_43a5_93e7_81810a74ce33
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1207, 604, "Bottom-II")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(425.544135899631)  # Temperature in K
MaterialStream1.SetPressure(506625)  # Pressure in Pa
MaterialStream1.SetMassFlow(3.47177266718016)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b6075efa_f296_48d2_b2c0_0b48b7a6fec1
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1210, 517, "Distillate-II")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(385.734143021054)  # Temperature in K
MaterialStream2.SetPressure(506625)  # Pressure in Pa
MaterialStream2.SetMassFlow(9.51651901281982)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_a91cf63c_32a6_40ae_a443_ac5a1170fff6
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1108, 551, "Column-II")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_51ed28be_67a0_46b0_a7c5_a4e8d015ecba
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1137, 629, "Bottom-I")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(359.408072317224)  # Temperature in K
MaterialStream3.SetPressure(60795)  # Pressure in Pa
MaterialStream3.SetMassFlow(3.62832188714807)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_17ba3ace_c19f_4db7_bee5_b701a379b460
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1121, 460, "Distillate-I")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(325.552761446771)  # Temperature in K
MaterialStream4.SetPressure(60795)  # Pressure in Pa
MaterialStream4.SetMassFlow(9.81458643285187)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_81883aa6_89d3_4bcc_b6cb_5efe726fe7db
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 951, 526, "Column-I")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_ba245c4b_2cf5_458b_8a72_2a841bed8095
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 937, 618, "Feed-2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(12.98829168)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1b58428b_efb2_4ffb_842d_fa303f9f8f16
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 896, 541, "Feed-1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(13.44290832)  # Mass Flow in kg/s

# Adding NodeOut: DIV_a00589f1_93d4_4590_8e8d_cc7fb0a91a46
Splitter1 = sim.AddObject(ObjectType.NodeOut, 824, 576, "Feed Splitter3")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MSTR_aeaaf0c3_758c_4df0_a953_dcf67f0eba19
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 757, 575, "Fresh Feed")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(26.4312)  # Mass Flow in kg/s

# Adding EnergyStream: EN_366cb25f_00de_4608_92a7_9036574f1b7a
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1404, 327, "C-Duty-2")
EnergyStream1 = EnergyStream1.GetAsObject()

sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Splitter1 to MaterialStream5
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream3
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Splitter1 to MaterialStream6
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream7.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream7 to Splitter1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_59.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_59.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

