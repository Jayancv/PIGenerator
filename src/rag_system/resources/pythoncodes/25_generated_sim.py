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
methyl_acetate = sim.AvailableCompounds["Methyl acetate"]
sim.SelectedCompounds.Add(methyl_acetate.Name, methyl_acetate)
acetic_acid = sim.AvailableCompounds["Acetic acid"]
sim.SelectedCompounds.Add(acetic_acid.Name, acetic_acid)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding MaterialStream: MAT_745afc6d_4981_46e1_bc5f_0cafd3a8f960
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1016, 617, "Acetic Acid")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(298)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.8340701117)  # Mass Flow in kg/s

# Adding MaterialStream: MSTR_84984d80_5947_4627_90f7_3cd97c8c1922
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1016, 400, "Methanol")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.4450281338)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_52e926a8_76b7_4f79_bd95_65b7a1bc4ed9
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1184, 412, "Reactive Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_dc1fd98b_9389_4a06_a614_819e1abc75db
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1429, 398, "Methyl Acetate")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(330.400994581435)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.02780822279538)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e2adc647_e64e_46d6_8d1f_2f228e21c9a0
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1429, 612, "Water")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(373.192299759022)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.251276209094341)  # Mass Flow in kg/s

sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
# sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_25.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_25.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

