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
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)

# Adding Simulation Objects
# Adding MaterialStream: MAT_b4a53ccb_9749_4546_8cb8_5add379525b3
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1160, 574, "sat liq/vap out")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(548.763735380292)  # Temperature in K
MaterialStream1.SetPressure(6000000)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0120333333333333)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ff657d39_ca5a_461d_bec9_295ea021953a
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1113, 627, "ESTR-007")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding HeaterCooler: RESF_fd9d01f6_ba87_45a8_93c1_003977b0c00a
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1070, 572, "Cooler")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_8f4e5135_1689_4acc_9e75_4b81f66e3f6f
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 947, 537, "Benzene out")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(573.149998098217)  # Temperature in K
MaterialStream2.SetPressure(200000)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.00433966666666667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_87058357_4759_4ce1_8954_3e24e94c43b4
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 783, 533, "Benzene in")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(773.15)  # Temperature in K
MaterialStream3.SetPressure(200000)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.00433966666666667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e3b8527e_b351_4515_a46d_848c4bac4642
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 975, 574, "sat liq/vap in")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(548.763735380292)  # Temperature in K
MaterialStream4.SetPressure(6000000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.0120333333333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1c4cdf2a_79e7_48be_943a_57e3485e8b14
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 926, 766, "Reccle out")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(548.15)  # Temperature in K
MaterialStream5.SetPressure(6000000)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0120333333333333)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_f6c59d10_7cf0_4c25_84e1_81755646249a
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 853, 528, "Heat ex 1")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding Vessel: SEP_1f9fe637_4fb3_490f_83d8_1ba89aadb357
Separator1 = sim.AddObject(ObjectType.Vessel, 1223, 555, "Separator")
Separator1 = Separator1.GetAsObject()

# Adding MaterialStream: MAT_59855f38_7555_417a_8858_785e5a970b91
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1328, 499, "Vapor")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(548.763730174203)  # Temperature in K
MaterialStream6.SetPressure(6000000)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.00120333333333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0fffa504_e1a2_4c47_817a_a0990ad55f5c
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1317, 605, "Sat liq 1")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(548.763735371331)  # Temperature in K
MaterialStream7.SetPressure(6000000)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.01083)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_5406bcc9_8d81_4070_b28a_7f3042899d9a
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 1433, 534, "Heat ex 2")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_deb7297b_81c6_4478_b7a3_a7c020864ad4
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1357, 539, "Methane in")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(373.15)  # Temperature in K
MaterialStream8.SetPressure(200000)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.00694444444444444)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8af57f24_b66c_48b5_b86e_93e078b4caa8
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1515, 538, "Methane out")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(533.150001049366)  # Temperature in K
MaterialStream9.SetPressure(200000)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.00694444444444444)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_baaee8a2_d049_4e58_93dd_97c60c07d2e3
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1465, 596, "sat liq 2")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(393.651227335709)  # Temperature in K
MaterialStream10.SetPressure(6000000)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.00120333333333333)  # Mass Flow in kg/s

# Adding NodeIn: MIST_63a17344_a102_4641_864e_8bb9a17ef2bc
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1507, 654, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_47f3cc7f_85a1_4a3c_8f99_2e9842b8ef40
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1564, 656, "Mixer out")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(537.07145680913)  # Temperature in K
MaterialStream11.SetPressure(6000000)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.0120333333333333)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_1c4cd882_389d_4768_89c6_9bc5df5a1f22
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1247, 739, "Recycle")
Recycle1 = Recycle1.GetAsObject()

sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream10 to Mixer1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle1 to MaterialStream5
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Separator1 to MaterialStream6
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream2
sim.ConnectObjects(MaterialStream11.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream11 to Recycle1
sim.ConnectObjects(MaterialStream4.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream4 to HeaterCooler1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream4
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream10
sim.ConnectObjects(MaterialStream8.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream8 to HeatExchanger2
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream7 to Mixer1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream1
sim.ConnectObjects(MaterialStream6.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream6 to HeatExchanger2
sim.ConnectObjects(Separator1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Separator1 to MaterialStream7
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream9
sim.ConnectObjects(MaterialStream1.GraphicObject, Separator1.GraphicObject, -1, -1)  # MaterialStream1 to Separator1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Mixer1 to MaterialStream11
sim.ConnectObjects(MaterialStream5.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream5 to HeatExchanger1
sim.ConnectObjects(MaterialStream3.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream3 to HeatExchanger1
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_67.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_67.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

