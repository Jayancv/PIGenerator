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
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
carbon_monoxide = sim.AvailableCompounds["Carbon monoxide"]
sim.SelectedCompounds.Add(carbon_monoxide.Name, carbon_monoxide)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)

# Adding Simulation Objects
# Adding EnergyStream: EN_bfaa2be1_1e89_4683_b51b_ef145653d863
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 684, 567, "ESTR-000")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_46fbda10_c393_463b_8716_732cc72e227c
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 888, 504, "MSTR-001")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(1000)  # Temperature in K
MaterialStream1.SetPressure(96143.0818857496)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0946608706037125)  # Mass Flow in kg/s

# Adding RCT_PFR: PFR_5f3ea195_7284_4d1d_b2be_f1a347522946
Reactor_PFR1 = sim.AddObject(ObjectType.RCT_PFR, 759, 504, "PFR-000")
Reactor_PFR1 = Reactor_PFR1.GetAsObject()

# Adding MaterialStream: MAT_407b6ae5_849b_4b85_aaa5_ce2ec4806f98
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 684, 504, "MSTR-000")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(1000)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.0946615522222222)  # Mass Flow in kg/s

sim.ConnectObjects(Reactor_PFR1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Reactor_PFR1 to MaterialStream1
sim.ConnectObjects(MaterialStream2.GraphicObject, Reactor_PFR1.GraphicObject, -1, -1)  # MaterialStream2 to Reactor_PFR1
sim.ConnectObjects(EnergyStream1.GraphicObject, Reactor_PFR1.GraphicObject, -1, -1)  # EnergyStream1 to Reactor_PFR1
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_4.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_4.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

