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
butanol_1 = sim.AvailableCompounds["1-butanol"]
sim.SelectedCompounds.Add(butanol_1.Name, butanol_1)
n_butyl_acetate = sim.AvailableCompounds["N-butyl acetate"]
sim.SelectedCompounds.Add(n_butyl_acetate.Name, n_butyl_acetate)
acetic_acid = sim.AvailableCompounds["Acetic acid"]
sim.SelectedCompounds.Add(acetic_acid.Name, acetic_acid)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_793e6b53_1a0d_4c67_b727_b2be0e8f4b5a
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1331, 585, "Product")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(398.926515811482)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.61169056088202)  # Mass Flow in kg/s

# Adding NodeIn: MIST_614007ca_1737_4d78_bc1f_d892a86cd5ff
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1324, 522, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_31928943_4470_4ae6_a3f3_9605a0d6eb44
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1214, 548, "Bottom")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(398.964686175296)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.61104004840081)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dc92e6cb_9e65_49e0_b409_de497694517b
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1222, 451, "Distillate")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(372.648277903648)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.252501667177275)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_02ca83c7_e675_4d96_b26c_fbad9fee35ca
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1033, 532, "Acetic Acid")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.834069451117)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_41f7cc36_4713_43ef_8d17_979e67515efa
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1031, 485, "Butanol")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.029486119347)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_55a797e4_3eb3_41a9_a6fe_82884a41d766
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1148, 498, "Reactive Distillation")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding CapeOpenUO: COUO_49ffbe96_6ea9_4287_887c_d74142804b17
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1276, 405, "Decanter")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_7c81ae41_6dcb_475a_9225_de4716ae3027
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1347, 428, "Top")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.000650512481217759)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d7f63cf6_6dd3_4e50_b8d4_2622ac8ee429
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1341, 360, "By-product")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.251851154696061)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO1
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
# sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_33.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_33.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

