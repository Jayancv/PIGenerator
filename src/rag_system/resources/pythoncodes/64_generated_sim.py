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
ethanol = sim.AvailableCompounds["Ethanol"]
sim.SelectedCompounds.Add(ethanol.Name, ethanol)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
diethyl_ether = sim.AvailableCompounds["Diethyl ether"]
sim.SelectedCompounds.Add(diethyl_ether.Name, diethyl_ether)

# Adding Simulation Objects
# Adding MaterialStream: MAT_ca50bf3b_6d04_4a81_86f7_afb5244c8dba
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 801, 614, "ETHANOL FEED")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(313.15)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.837218)  # Mass Flow in kg/s

# Adding NodeIn: MIST_b7f160bd_bc19_43d4_af95_8bf523080aae
Mixer1 = sim.AddObject(ObjectType.NodeIn, 889, 578, "MIXER")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_083b9b15_cd7a_4295_94e0_d5fc2bb38e4c
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 994, 418, "ETHANOL REC1")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(347.601772880945)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.875505473004801)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4ca7fb1d_237d_4f53_884d_af0fb0b005c3
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 967, 575, "mixer feed")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(331.201892044914)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.71329993315357)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_7313c423_4ae8_449f_893f_48c55984c816
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1017, 561, "conversion reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_5c0dbac7_28b6_4e16_ad60_6cd5856594ea
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1121, 540, "N")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(298.15)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ef82c3be_31ec_45d7_b856_bfaad3831f3e
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1131, 593, "converted product")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(298.15)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.71329993315357)  # Mass Flow in kg/s

# Adding EnergyStream: EN_34ee5eab_44f5_4bca_8f6c_0322c414a580
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1004, 646, "ESTR-007")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding CapeOpenUO: COUO_86b021a0_d23a_49f7_88ab_3e6ce12dc07b
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1217, 583, "Distillation column 1")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding OT_Recycle: REC_54435d4b_e6fa_40fa_a26c_47f82a714b01
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1242, 417, "ETHANOL REC22")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_438584c9_946f_4fdd_8746_3722bf5f775a
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1573, 657, "WATER")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(372.753251965422)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.206567203010557)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_91c908c4_8236_4f32_8ecb_63ae5ac5340b
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1350, 635, "Bottoms1")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(349.561747824402)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.08207267601536)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6077aad8_cabe_4d03_81db_83d5c54e307e
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1364, 500, "DIETHYL ETHER")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(307.895838707049)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.631227257138228)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_2d87c779_b9e0_4ad5_9bee_ca2be377250f
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1516, 418, "ETHANOL REC")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(347.601772880945)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.875505473004801)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_15bff9cc_2620_4e7f_baf7_d232ddccad9d
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1453, 576, "Distillation column 2")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(MaterialStream9.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream9 to Recycle1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream9
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream5
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream4
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream8
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Mixer1 to MaterialStream3
sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO2
sim.ConnectObjects(EnergyStream1.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream1 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream3.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream3 to Reactor_Conversion1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream7
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_64.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_64.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

