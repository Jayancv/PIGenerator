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
n_pentane = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(n_pentane.Name, n_pentane)
isopentane = sim.AvailableCompounds["Isopentane"]
sim.SelectedCompounds.Add(isopentane.Name, isopentane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_ab0eb279_eaf4_4db4_bfe8_39796e7f2145
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1416, 553, "Final Outlet")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(297.940823757483)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(88.9)  # Mass Flow in kg/s

# Adding NodeIn: MIST_e7d45313_21f9_4c1f_93a6_4814ffee0b18
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1332, 553, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_45b723f1_5588_4321_b7c2_81d4fd587a8e
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1328, 414, "Energy")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_03ee8e15_b9c1_47c6_8ff1_22ed6928bef5
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1327, 473, "Low Stream")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298.150006045432)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(44.4)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e40e0c20_cb79_4461_8be8_8fb590dd9b3c
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1326, 317, "Side Stream")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(298.150000010804)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(11.1)  # Mass Flow in kg/s

# Adding ComponentSeparator: CS_1527cf2c_7503_42c5_bb29_856026aa8d75
ComponentSeparator1 = sim.AddObject(ObjectType.ComponentSeparator, 1175, 363, "Iso-Pentane Tower")
ComponentSeparator1 = ComponentSeparator1.GetAsObject()

# Adding MaterialStream: MAT_ecbd4f2f_771d_4180_aa8d_e4d189f7f6d0
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1083, 444, "Output_02")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(44.5)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c729b881_07c5_466e_88f8_4ef469004ce4
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1086, 378, "Output_01")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(55.5)  # Mass Flow in kg/s

# Adding NodeOut: DIV_f7b7f25f_763f_4f67_8210_c26277bf65ce
Splitter1 = sim.AddObject(ObjectType.NodeOut, 931, 408, "Splitter")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_dbe944f6_566b_43b3_948e_6dfffea2c195
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 810, 408, "Feed")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(100)  # Mass Flow in kg/s

sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Splitter1 to MaterialStream4
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream3
sim.ConnectObjects(ComponentSeparator1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # ComponentSeparator1 to EnergyStream1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream2
sim.ConnectObjects(MaterialStream5.GraphicObject, ComponentSeparator1.GraphicObject, -1, -1)  # MaterialStream5 to ComponentSeparator1
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Splitter1 to MaterialStream5
sim.ConnectObjects(MaterialStream6.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream6 to Splitter1
# sim.AutoLayout()
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_10.xml")
 
interf.SaveFlowsheet(sim, fileNameToSave, False)



# Export PFD image
clr.AddReference(dwsimpath + "SkiaSharp.dll")
clr.AddReference("System.Drawing")

from SkiaSharp import SKBitmap, SKImage, SKCanvas, SKEncodedImageFormat
from System.IO import MemoryStream
from System.Drawing import Image
from System.Drawing.Imaging import ImageFormat

# Render PFD to image
#sim.GetSurface().AutoArrange()
PFDSurface = sim.GetSurface()
bmp = SKBitmap(2024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_10.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

