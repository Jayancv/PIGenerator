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
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
carbon = sim.AvailableCompounds["Carbon"]
sim.SelectedCompounds.Add(carbon.Name, carbon)
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)

# Adding Simulation Objects
# Adding EnergyStream: EN_5ec8fa6a_0871_4a3b_bcc7_1649cbcd559d
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1134, 500, "Heat")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding RCT_Conversion: RC_f710dbf3_03cf_4d65_bfc1_c9451c734518
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1199, 417, "RC-000")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_598dba63_1d22_4f08_8547_eee356d28872
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1309, 486, "Liquid / Solid")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(298.156088126115)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0053322387710772)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b80fc44f_98f4_4d44_9ae2_67fd78a35046
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1310, 405, "Gas")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298.156088126115)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.300223761228923)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1e652419_e880_404b_843f_c58bf93f7acc
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 993, 361, "Air")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(298.15)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.277778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8dd5d04c_5019_4d8d_8b25_07a7ca6735de
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 993, 448, "Carbon")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.027778)  # Mass Flow in kg/s

# Adding NodeIn: MIST_5530f54b_2117_4001_b361_0bda9161e003
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1045, 401, "MIX-000")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_978cb416_79f3_40b7_9326_c786e7003e62
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1105, 401, "Feed")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.156088126115)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.305556)  # Mass Flow in kg/s

sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream2
sim.ConnectObjects(EnergyStream1.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream1 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(MaterialStream5.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream5 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Mixer1 to MaterialStream5
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_5.xml")
 
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
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_5.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

