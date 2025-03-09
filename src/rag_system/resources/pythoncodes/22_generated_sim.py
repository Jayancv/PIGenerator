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
isopentane = sim.AvailableCompounds["Isopentane"]
sim.SelectedCompounds.Add(isopentane.Name, isopentane)
n_butane = sim.AvailableCompounds["N-butane"]
sim.SelectedCompounds.Add(n_butane.Name, n_butane)
n_pentane = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(n_pentane.Name, n_pentane)
isobutane = sim.AvailableCompounds["Isobutane"]
sim.SelectedCompounds.Add(isobutane.Name, isobutane)
ethane = sim.AvailableCompounds["Ethane"]
sim.SelectedCompounds.Add(ethane.Name, ethane)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_bceb8ea3_0c0d_4496_a696_8e215a6f6661
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1295, 503, "MSTR-006")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(328.828827332532)  # Temperature in K
MaterialStream1.SetPressure(719407.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(99.8794525327772)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f6e0de95_a71c_49cb_8450_588f9d90e179
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1350, 626, "BOTTOM")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(372.324068991944)  # Temperature in K
MaterialStream2.SetPressure(749805)  # Pressure in Pa
MaterialStream2.SetMassFlow(37.1486423830208)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_373e498e_1bcb_4fdb_9ebc_2ba78b143c2f
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1185, 574, "DEBUTANIZER")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding CapeOpenUO: COUO_59cf66f0_fbb0_4839_bf13_b993e3af4cb5
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 833, 461, "DEPROPANIZER")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding Valve: VALV_99f22620_cb24_4be4_b0cc_ad804124ca28
Valve1 = sim.AddObject(ObjectType.Valve, 1048, 606, "REDUCTION VALVE")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_b46c7bb1_e7d1_4f73_8008_ebb0e3328875
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1137, 617, "MSTR-005")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(340.30715014336)  # Temperature in K
MaterialStream3.SetPressure(739672.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(137.028094915796)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b35ccc90_75d2_4ecf_b76c_b7a446e7deb7
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 978, 588, "MSTR-002")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(380.509434406489)  # Temperature in K
MaterialStream4.SetPressure(1773188)  # Pressure in Pa
MaterialStream4.SetMassFlow(137.028094915796)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9df36301_d455_41be_b65d_a173ae2be4fd
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 989, 420, "PROPANE")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(323.083699487155)  # Temperature in K
MaterialStream5.SetPressure(1722525)  # Pressure in Pa
MaterialStream5.SetMassFlow(48.8958331349764)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_af94ba40_5ead_4fc0_9627_2fa22d520b05
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 766, 498, "LIGHT-END")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(378)  # Temperature in K
MaterialStream6.SetPressure(1763055)  # Pressure in Pa
MaterialStream6.SetMassFlow(185.923928050774)  # Mass Flow in kg/s

# Adding Valve: VALV_33faba3a_4d03_40d6_9095_5969dc474bc7
Valve2 = sim.AddObject(ObjectType.Valve, 1387, 510, "VAPOUR REMOVAL")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_c94f258d_455a_4936_b1b5_4681d77174e8
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1493, 546, "MSTR-010")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(328.830562415413)  # Temperature in K
MaterialStream7.SetPressure(719437.8975)  # Pressure in Pa
MaterialStream7.SetMassFlow(99.8794525327772)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_5b28e33e_eb9d_4101_b165_f04e11ff3683
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1573, 483, "DEISOBUTANIZER")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_950c811c_b1b4_428f_9bcc_f2942e2b7a4b
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1720, 453, "ISOBUTANE-RICH")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(322.483651292742)  # Temperature in K
MaterialStream8.SetPressure(668745)  # Pressure in Pa
MaterialStream8.SetMassFlow(70.5268398315758)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4459ac03_02d7_46a9_8f8c_f1a2a8f7cf89
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1731, 572, "BUTANE-RICH")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(339.675578547882)  # Temperature in K
MaterialStream9.SetPressure(749805)  # Pressure in Pa
MaterialStream9.SetMassFlow(29.352612701201)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO3
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Valve1 to MaterialStream3
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO1
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Valve2 to MaterialStream7
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(MaterialStream1.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream1 to Valve2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream9
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream8
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_22.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_22.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

