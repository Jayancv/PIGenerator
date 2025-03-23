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
acetone = sim.AvailableCompounds["Acetone"]
sim.SelectedCompounds.Add(acetone.Name, acetone)
isopropanol = sim.AvailableCompounds["Isopropanol"]
sim.SelectedCompounds.Add(isopropanol.Name, isopropanol)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)

# Adding Simulation Objects
# Adding MaterialStream: MAT_e70d20d5_015d_468e_bd2e_d0449375dc0f
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1864, 872, "recycled stream")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(325.613957513086)  # Temperature in K
MaterialStream1.SetPressure(742746.989950082)  # Pressure in Pa
MaterialStream1.SetMassFlow(132.04107541848)  # Mass Flow in kg/s

# Adding NodeIn: MIST_9c116b82_0148_44be_a702_725e1f89c226
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1952, 930, "stream mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_15941de8_61de_4c72_91fe_1723c7fe0ba3
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2585, 908, "mixed stream")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(352.051595572263)  # Temperature in K
MaterialStream2.SetPressure(110535.91)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.530034292978694)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_5e5262de_4070_4b50_ba55_78a16b2bd8cc
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2583, 831, "Recycle stream")
Recycle1 = Recycle1.GetAsObject()

# Adding DistillationColumn: DC_173fb024_d992_4ef6_b3c7_63e52eba649c
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2236, 646, "Distilation cloumn 2")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_05baf940_8bbd_432e_82bc_4d3f8a8ad27e
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1841, 783, "Energy stream 2")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_80fbdd6e_7fe9_46ef_b865_cb844fae1cd9
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1843, 712, "Hydrogen")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(325)  # Temperature in K
MaterialStream3.SetPressure(1374958.06990016)  # Pressure in Pa
MaterialStream3.SetMassFlow(12.7189595395672)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5883db75_e25e_44a6_9fb9_d40e8f76641c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1880, 767, "mix 3")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(325)  # Temperature in K
MaterialStream4.SetPressure(1374958.06990016)  # Pressure in Pa
MaterialStream4.SetMassFlow(131.511041116465)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_6d441d8d_3e22_4d66_b40a_e1c45694f0c2
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1764, 756, "FLASH SEP")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()
print("CapOpenUO1 added")

# Adding MaterialStream: MAT_26c40c38_e0cd_4435_a49b_1c18c3d93fbd
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2133, 895, "mix A+ISOWE")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(337.155230636886)  # Temperature in K
MaterialStream5.SetPressure(111457)  # Pressure in Pa
MaterialStream5.SetMassFlow(58.6323332913423)  # Mass Flow in kg/s
print("MaterialStream5 added")

# Adding MaterialStream: MAT_5d8983af_b367_4213_be02_afd25918380b
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2136, 673, "ACETONE")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(61.3397988780552)  # Temperature in K
MaterialStream6.SetPressure(101315)  # Pressure in Pa
MaterialStream6.SetMassFlow(73.3819965559059)  # Mass Flow in kg/s
print("MaterialStream6 added")

# Adding EnergyStream: EN_155413d9_4e10_4022_a235_565346fcacce
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2142, 833, "Energy stream 4")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding DistillationColumn: DC_5a0bafc5_00d7_4028_9cc4_3e52f9883427
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 1943, 664, "Distilation column 1")
DistillationColumn2 = DistillationColumn2.GetAsObject()
print("DistillationColumn2 added")

# Adding EnergyStream: EN_f265618c_5b97_417f_8e86_677dd1836c08
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2137, 632, "Energy stream 3")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_21426e07_88f7_4612_9f6a_ccf6b0004278
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1600, 859, "Energy stream 1")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_b3de90e8_160b_4e34_8ba0_f66ea558acde
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1698, 854, "unreacted stream")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(530)  # Temperature in K
MaterialStream7.SetPressure(1376958.06990016)  # Pressure in Pa
MaterialStream7.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fd9ed7b9_0810_4bcc_8e28_d2babb35eaa9
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1712, 770, "mix 2")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(530)  # Temperature in K
MaterialStream8.SetPressure(1376958.06990016)  # Pressure in Pa
MaterialStream8.SetMassFlow(144.230000656032)  # Mass Flow in kg/s

# Adding RCT_Equilibrium: RE_c9513a82_edb5_497f_9bdd_d8fe2b649a3d
Reactor_Equilibrium1 = sim.AddObject(ObjectType.RCT_Equilibrium, 1640, 766, "reactor")
Reactor_Equilibrium1 = Reactor_Equilibrium1.GetAsObject()
print("Reactor_Equilibrium1 added")

# Adding MaterialStream: MAT_dd62fa95_dda2_4724_b4e8_9138e1db9832
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1586, 780, "ISOPROPANOL")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(399.999742538035)  # Temperature in K
MaterialStream9.SetPressure(463636.625227613)  # Pressure in Pa
MaterialStream9.SetMassFlow(144.230256)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_bbad07f5_baa2_4433_8204_3ddc85405c3c
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2135, 762, "SIDE STREAM")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(331.8904339877)  # Temperature in K
MaterialStream10.SetPressure(105930.45)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.0291007021015573)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b1167b4b_088e_4039_baf6_dcd84527a0af
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2436, 628, "side product")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(333.979800352328)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(58.1023113858421)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_db32ef4b_a30e_4838_88a1_09f0fd11dd6e
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2431, 967, "isopropanol")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(352.098992941166)  # Temperature in K
MaterialStream12.SetPressure(111457)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.5)  # Mass Flow in kg/s

# Adding EnergyStream: EN_9d463d9b_c65c_41de_8d86_7a42dc9830a7
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2438, 671, "Energy stream 5")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: EN_819e78dd_710c_4421_9b10_9fff15e10581
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2367, 932, "Energy stream 6")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_59c1a215_37e6_4ab4_a5bd_ded37d5d4c0d
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2439, 782, "Side stream")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(351.257176893096)  # Temperature in K
MaterialStream13.SetPressure(109614.82)  # Pressure in Pa
MaterialStream13.SetMassFlow(0.030034292978694)  # Mass Flow in kg/s

# Adding NodeIn: MIST_cfe5fa6f_a081_4186_8628_c64ba6dc40b3
Mixer2 = sim.AddObject(ObjectType.NodeIn, 2517, 776, "Mixer2")
Mixer2 = Mixer2.GetAsObject()
print("Mixer2 added")
# Adding OT_EnergyRecycle: EREC_2c1d680c_3190_4cba_8bbb_d4aaf6017097
EnergyRecycle1 = sim.AddObject(ObjectType.OT_EnergyRecycle, 2032, 943, "energy recycle")
EnergyRecycle1 = EnergyRecycle1.GetAsObject()
print("EnergyRecycle1 added")
# Adding MaterialStream: MAT_7f14aae7_527b_4065_991c_014c87f2be62
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2573, 773, "mx stream")
print("MaterialStream added")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(352.051595572263)  # Temperature in K
MaterialStream14.SetPressure(110535.91)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.530034292978694)  # Mass Flow in kg/s
print("Components added")

DistillationColumn1.ConnectDistillate(MaterialStream11)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream12)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream5)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream6)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream6)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream5)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream3)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream2)  # ConnectReboilerDuty 
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(EnergyRecycle1.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # EnergyRecycle1 to EnergyStream4
sim.ConnectObjects(Reactor_Equilibrium1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Reactor_Equilibrium1 to MaterialStream7
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream12 to Mixer2
sim.ConnectObjects(MaterialStream5.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream5 to DistillationColumn1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
# sim.ConnectObjects(EnergyStream2.GraphicObject, EnergyRecycle1.GraphicObject, -1, -1)  # EnergyStream2 to EnergyRecycle1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_Equilibrium1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_Equilibrium1
# sim.ConnectObjects(CapeOpenUO1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to EnergyStream1
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Mixer2 to MaterialStream14
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(MaterialStream14.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream14 to Recycle1
sim.ConnectObjects(DistillationColumn2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # DistillationColumn2 to MaterialStream10
sim.ConnectObjects(Reactor_Equilibrium1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Reactor_Equilibrium1 to MaterialStream8
sim.ConnectObjects(DistillationColumn1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # DistillationColumn1 to MaterialStream13
sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO1
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(MaterialStream1.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream1 to DistillationColumn2
sim.ConnectObjects(MaterialStream9.GraphicObject, Reactor_Equilibrium1.GraphicObject, -1, -1)  # MaterialStream9 to Reactor_Equilibrium1
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_52.xml")
 
interf.SaveFlowsheet(sim, fileNameToSave, False)

print("Flowsheet saved to: " + fileNameToSave)

# Export PFD image
clr.AddReference(dwsimpath + "SkiaSharp.dll")
clr.AddReference("System.Drawing")

from SkiaSharp import SKBitmap, SKImage, SKCanvas, SKEncodedImageFormat
from System.IO import MemoryStream
from System.Drawing import Image
from System.Drawing.Imaging import ImageFormat
print("Flowsheet")
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_52.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

