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
chloroform = sim.AvailableCompounds["Chloroform"]
sim.SelectedCompounds.Add(chloroform.Name, chloroform)

# Adding Simulation Objects
# Adding MaterialStream: MAT_1d428e95_b735_4388_9eeb_eca03a82d3b8
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 614, 393, "Fresh Feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(300)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(2.10304166666667)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_f0ff4d97_378e_442a_a269_e3cceed9812e
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 710, 340, "Low Pressure Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_6e16f757_236c_4fc2_84e6_2698bfbef15b
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 619, 343, "Recycled Feed")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(404.8589285782)  # Temperature in K
MaterialStream2.SetPressure(1013250)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.64766993157299)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_996c815d_8ea7_4a0e_ba84_fa84663d716d
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 820, 310, "D1")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(326.123985567317)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(3.29807730263617)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_78a053dc_072d_490a_8441_763944a4a517
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 830, 416, "B1")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(337.515234010382)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.450549748648053)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_a4e92f07_1b57_4caa_aaff_29dc4ac6f39b
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 880, 342, "High Pressure Column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_710855a4_0191_4ced_8a31_5c51c40cca75
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1012, 306, "D2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(404.8589285782)  # Temperature in K
MaterialStream5.SetPressure(1013250)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.64766993157299)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8521f7c8_d3e4_4d42_9d42_5add2c1ed94e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1003, 425, "B2")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(425.233002553443)  # Temperature in K
MaterialStream6.SetPressure(1013250)  # Pressure in Pa
MaterialStream6.SetMassFlow(1.65040737105401)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_c224a42a_5d93_41cd_9e96_cd43e6a71c56
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 722, 256, "Recyle Block")
Recycle1 = Recycle1.GetAsObject()

sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(MaterialStream5.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream5 to Recycle1
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
# sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_69.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_69.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

