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
helium_4 = sim.AvailableCompounds["Helium-4"]
sim.SelectedCompounds.Add(helium_4.Name, helium_4)

# Adding Simulation Objects
# Adding OT_Recycle: REC_07ea28a3_a18b_4a55_bac7_e83e91967f7c
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1433, 747, "REC-011")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_bb5d80c8_e7b1_4408_bd5d_2b64b5f28bcd
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1990, 571, "adiabatic compressor outlet")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(599.999809094647)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(1)  # Mass Flow in kg/s

# Adding EnergyStream: EN_82562c09_2e1b_405a_a4d3_2bc174b96107
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1732, 452, "adiabatic compressor energy")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding CompressorExpander: COMP_52b9ea33_580e_4c96_b695_ddf073858a01
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1889, 526, "adiabatic compressor")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_1a395c93_12cd_47b0_86e5_27e09f833e70
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1740, 566, "adiabatic compressor inlet")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(475.023256720912)  # Temperature in K
MaterialStream2.SetPressure(40530)  # Pressure in Pa
MaterialStream2.SetMassFlow(1)  # Mass Flow in kg/s

# Adding Valve: VALV_b78eebfa_4179_407e_ba3e_952a03ecfe01
Valve1 = sim.AddObject(ObjectType.Valve, 1627, 517, "iso-compressor")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_31719453_55bc_4e5d_9f44_3aac33e397ad
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1532, 563, "iso-compressor inlet")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(475.023256720912)  # Temperature in K
MaterialStream3.SetPressure(20000)  # Pressure in Pa
MaterialStream3.SetMassFlow(1)  # Mass Flow in kg/s

# Adding EnergyStream: EN_74c22061_9713_4821_84a2_432082dc043c
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1366, 447, "adiabatic expander energy ")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding CompressorExpander: TURB_11e572e1_cedf_4364_8997_8469d311421f
AdiabaticExpanderCompressor2 = sim.AddObject(ObjectType.Compressor, 1417, 508, "adiabatic expander")
AdiabaticExpanderCompressor2 = AdiabaticExpanderCompressor2.GetAsObject()

# Adding MaterialStream: MAT_f39fffd7_2d2d_4d75_9c2a_62b79eabacdd
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1301, 557, "adiabatic expander inlet")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(600)  # Temperature in K
MaterialStream4.SetPressure(50000)  # Pressure in Pa
MaterialStream4.SetMassFlow(1)  # Mass Flow in kg/s

# Adding Valve: VALV_a58ab9e1_91fe_436d_a4b4_c7fde5f45018
Valve2 = sim.AddObject(ObjectType.Valve, 1197, 507, "iso-expander")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_740b1c49_2f1f_41c6_b7e5_0d27b3a35bd9
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1108, 558, "iso-expander inlet")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(600)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream1.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream1 to Recycle1
# sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to EnergyStream2
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Valve1 to MaterialStream2
sim.ConnectObjects(AdiabaticExpanderCompressor2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor2 to MaterialStream3
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream1
sim.ConnectObjects(MaterialStream4.GraphicObject, AdiabaticExpanderCompressor2.GraphicObject, -1, -1)  # MaterialStream4 to AdiabaticExpanderCompressor2
sim.ConnectObjects(MaterialStream2.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream2 to AdiabaticExpanderCompressor1
sim.ConnectObjects(EnergyStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream5.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream5 to Valve2
sim.ConnectObjects(MaterialStream3.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream3 to Valve1
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Valve2 to MaterialStream4
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle1 to MaterialStream5
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_17.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_17.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

