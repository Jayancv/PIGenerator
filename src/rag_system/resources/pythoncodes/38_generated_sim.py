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
dimethyl_sulfoxide = sim.AvailableCompounds["Dimethyl sulfoxide"]
sim.SelectedCompounds.Add(dimethyl_sulfoxide.Name, dimethyl_sulfoxide)
acetone = sim.AvailableCompounds["Acetone"]
sim.SelectedCompounds.Add(acetone.Name, acetone)

# Adding Simulation Objects
# Adding OT_Recycle: REC_b0366fe1_3e80_4553_84c7_94d78ce9e0f6
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 833, 655, "REC-014")
Recycle1 = Recycle1.GetAsObject()

# Adding EnergyStream: EN_32cca008_325c_42eb_92e0_b91c93f99234
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1391, 546, "LOAD")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_91f53f02_5a8c_4b05_9064_005f72f66f9d
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1396, 654, "ENTRAINER RECYCLE")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(320)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(16.2769256813952)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e767724a_b42a_4fd1_b504_46364be84cf9
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1194, 479, "MET-DMSO")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(390.39290065968)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(18.6805698733408)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fca931c9_7319_41f0_bec8_748ee178bf8a
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1189, 360, "PURE ACETONE")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(329.28396919201)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(4.35562772891678)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_1ddeddee_e2b3_47c4_be34_5040eed7135a
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1082, 414, "EXTRACTIVE DISTI")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_fe922e0f_2ed8_45ce_80b3_65efb0324104
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 981, 386, "ENTRAINER")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(320)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(16.2770476022574)  # Mass Flow in kg/s

# Adding NodeIn: MIST_bc6e1e23_bdf0_4cb3_a103_e436c1a3fa74
Mixer1 = sim.AddObject(ObjectType.NodeIn, 917, 386, "MIX-003")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_bec0bc89_93bc_422d_94d4_d5908d3beb50
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 823, 397, "COOLED DMSO")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(320)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(16.2768305650352)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f70b635e_6bda_4ef4_9b80_abfc50d34ba1
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 873, 466, "MAKE UP")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(320)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.000217037222222222)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a5ba64e6_a7b3_4e28_8889_0919db3db3f0
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 981, 458, "FEED")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(320)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(6.75915)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_27a67dd6_905f_44af_80af_aaa0ac593a56
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1373, 445, "DMSO")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(462.352633604809)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(16.2769256813952)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dc68a840_e509_46e5_b0a2_69c13a2360f6
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1371, 371, "PURE METHANOL")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(337.215730710553)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.4036441919454)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_c14f5f48_6c43_4f7f_9b93_409e7612501d
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1258, 403, "DISTILATION")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding Cooler: RESF_d163582b_77c4_499e_8de0_7e2b4b548b6c
Cooler1 = sim.AddObject(ObjectType.Cooler, 1440, 474, "COOL-011")
Cooler1 = Cooler1.GetAsObject()

sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Mixer1 to MaterialStream4
sim.ConnectObjects(MaterialStream1.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream1 to Recycle1
sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream5 to Mixer1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream9
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO2
# sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO1
sim.ConnectObjects(MaterialStream8.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream8 to Cooler1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle1 to MaterialStream5
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Cooler1 to MaterialStream1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_38.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_38.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

