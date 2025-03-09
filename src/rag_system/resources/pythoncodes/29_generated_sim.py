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
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
ammonia = sim.AvailableCompounds["Ammonia"]
sim.SelectedCompounds.Add(ammonia.Name, ammonia)

# Adding Simulation Objects
# Adding EnergyStream: EN_aa1a0b31_07f6_4aef_825c_d2ffdbfc8ae8
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 911, 534, "energy stream 7")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding OT_Recycle: REC_b3667d2a_cdae_4eca_a4dd_c96cfba35337
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 334, 411, "recycle 2")
Recycle1 = Recycle1.GetAsObject()

# Adding Cooler: RESF_03eb30bb_1e6f_4242_9bb8_271dc3a5cf4e
Cooler1 = sim.AddObject(ObjectType.Cooler, 905, 427, "cooler 3")
Cooler1 = Cooler1.GetAsObject()

# Adding EnergyStream: EN_f287857d_72cc_470b_a0e0_34510be028b6
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1084, 509, "energy stream 6")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_e14d6777_0052_4f9a_a95d_6fb8a5675193
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1141, 434, "stream 7")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(862.655746964096)  # Temperature in K
MaterialStream1.SetPressure(9450662.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(23.9021598577333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ed053555_71c3_408c_b4bb_024257f4e98f
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1144, 379, "main product")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(862.655746940856)  # Temperature in K
MaterialStream2.SetPressure(9450662.5)  # Pressure in Pa
MaterialStream2.SetMassFlow(8.33204402326097)  # Mass Flow in kg/s

# Adding ComponentSeparator: CS_a51404f5_84c3_46f9_a3a4_907e6ade5f8d
ComponentSeparator1 = sim.AddObject(ObjectType.ComponentSeparator, 1050, 393, "compound seperator 2")
ComponentSeparator1 = ComponentSeparator1.GetAsObject()

# Adding ComponentSeparator: CS_ae765657_0439_4126_95fc_b5e1dd28dbdd
ComponentSeparator2 = sim.AddObject(ObjectType.ComponentSeparator, 1046, 234, "compound seperator")
ComponentSeparator2 = ComponentSeparator2.GetAsObject()

# Adding EnergyStream: EN_a27c3c9f_9054_45c2_a5d9_44781e4d1059
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1069, 317, "energy stream 4")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_6873afb3_2858_4698_bd82_28e4c3572561
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1131, 305, "stream 5")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(862.655746964096)  # Temperature in K
MaterialStream3.SetPressure(9450662.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(32.2342038809943)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4bdad3b5_79d6_416e_bf21_52316bce4178
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1133, 232, "stream 8")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(862.655759912884)  # Temperature in K
MaterialStream4.SetPressure(9450662.5)  # Pressure in Pa
MaterialStream4.SetMassFlow(24.8769131378052)  # Mass Flow in kg/s

# Adding EnergyStream: EN_2f3ad0c8_e530_4042_8096_19c493a2e613
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 708, 331, "energy stream 2")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_85f1578d_b032_4785_b9b4_4c447fe4ceb0
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 816, 333, "Reactor Bottom")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(863.416244402628)  # Temperature in K
MaterialStream5.SetPressure(10450662.5)  # Pressure in Pa
MaterialStream5.SetMassFlow(0)  # Mass Flow in kg/s

# Adding RCT_Equilibrium: RE_44c39330_692a_4e0d_bb22_f1be8acfa3b7
Reactor_Equilibrium1 = sim.AddObject(ObjectType.RCT_Equilibrium, 731, 242, "equlibruim reactor")
Reactor_Equilibrium1 = Reactor_Equilibrium1.GetAsObject()

# Adding MaterialStream: MAT_bfa1d0d1_06a2_44f3_b12c_7af8b8b83659
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 649, 391, "stream 10")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(300)  # Temperature in K
MaterialStream6.SetPressure(800000)  # Pressure in Pa
MaterialStream6.SetMassFlow(23.9021598577333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d47ef972_db4d_4e6f_9ed0_1dcb15d59153
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 658, 260, "stream 3")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(863.416244402628)  # Temperature in K
MaterialStream7.SetPressure(10450662.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(57.1110289577388)  # Mass Flow in kg/s

# Adding EnergyStream: EN_92323eba_85e1_4ac6_844f_0fd05bca9e7b
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 526, 329, "energy stream 1")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding Compressor: COMP_2946922a_2a67_476b_9f14_c1f1eee72eaa
Compressor1 = sim.AddObject(ObjectType.Compressor, 566, 276, "compressor")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_ddabda0c_c911_44a1_bfaf_d6cc9551c52c
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 522, 225, "stream 2")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(300.000000482349)  # Temperature in K
MaterialStream8.SetPressure(450662.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(57.1110289577388)  # Mass Flow in kg/s

# Adding NodeIn: MIST_7923d897_f8eb_42d5_bd4c_d9475beda5c0
Mixer1 = sim.AddObject(ObjectType.NodeIn, 465, 269, "MIXER")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_f07590c5_efaf_4c63_8b8c_0b492d0a4315
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 360, 330, "hydrogen")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(300.008192616508)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(26.3562508959178)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a5f3ad6b_8706_4680_8f8c_dba24fc3e488
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 371, 234, "nitrogen")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(300)  # Temperature in K
MaterialStream10.SetPressure(800000)  # Pressure in Pa
MaterialStream10.SetMassFlow(30.754778061821)  # Mass Flow in kg/s

# Adding EnergyStream: EN_f7e0f03c_23bc_4a26_90ac_084a19cc4cfe
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 926, 345, "energy stream 3")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_27136dc2_6b97_45dd_b1c2_1f2453247333
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 819, 220, "Reactor Top")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(863.416244402628)  # Temperature in K
MaterialStream11.SetPressure(10450662.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(57.1111170187995)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_94741777_5fbb_412b_b99c_3a70d429f242
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 972, 230, "stream 4")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(862.655746964096)  # Temperature in K
MaterialStream12.SetPressure(9450662.5)  # Pressure in Pa
MaterialStream12.SetMassFlow(57.1111170187995)  # Mass Flow in kg/s

# Adding Cooler: RESF_e58b751a_15f0_4417_a7a2_68dad4e53b23
Cooler2 = sim.AddObject(ObjectType.Cooler, 904, 263, "cooler 1")
Cooler2 = Cooler2.GetAsObject()

# Adding Cooler: RESF_f05f8909_021d_442b_a7d4_b78517dfa457
Cooler3 = sim.AddObject(ObjectType.Cooler, 905, 99, "cooler 2")
Cooler3 = Cooler3.GetAsObject()

# Adding MaterialStream: MAT_5934d3cb_2d01_4359_a51e_330a206c8593
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 765, 150, "stream 9")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(300.000000000312)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(24.8769131378052)  # Mass Flow in kg/s

# Adding EnergyStream: EN_b7402cbc_09e6_4103_bab7_28fbe1de0a89
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 904, 189, "energy stream.5")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding OT_Recycle: REC_4fa6fa92_d1dc_44b1_adfe_fd8ec709f419
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 446, 174, "recycle")
Recycle2 = Recycle2.GetAsObject()

sim.ConnectObjects(ComponentSeparator2.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # ComponentSeparator2 to EnergyStream3
sim.ConnectObjects(EnergyStream4.GraphicObject, Reactor_Equilibrium1.GraphicObject, -1, -1)  # EnergyStream4 to Reactor_Equilibrium1
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream10 to Mixer1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Mixer1 to MaterialStream8
sim.ConnectObjects(MaterialStream12.GraphicObject, ComponentSeparator2.GraphicObject, -1, -1)  # MaterialStream12 to ComponentSeparator2
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Cooler1 to MaterialStream6
sim.ConnectObjects(MaterialStream4.GraphicObject, Cooler3.GraphicObject, -1, -1)  # MaterialStream4 to Cooler3
sim.ConnectObjects(ComponentSeparator1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # ComponentSeparator1 to EnergyStream2
sim.ConnectObjects(EnergyStream5.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream5 to Compressor1
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # Cooler2 to EnergyStream6
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Cooler2 to MaterialStream12
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream1
sim.ConnectObjects(ComponentSeparator2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # ComponentSeparator2 to MaterialStream4
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream2
sim.ConnectObjects(MaterialStream11.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream11 to Cooler2
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Recycle2 to MaterialStream9
sim.ConnectObjects(MaterialStream3.GraphicObject, ComponentSeparator1.GraphicObject, -1, -1)  # MaterialStream3 to ComponentSeparator1
sim.ConnectObjects(Cooler3.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Cooler3 to MaterialStream13
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Compressor1 to MaterialStream7
sim.ConnectObjects(MaterialStream13.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream13 to Recycle2
sim.ConnectObjects(Reactor_Equilibrium1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Reactor_Equilibrium1 to MaterialStream11
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Recycle1 to MaterialStream10
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream6 to Recycle1
sim.ConnectObjects(Cooler3.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # Cooler3 to EnergyStream7
sim.ConnectObjects(Reactor_Equilibrium1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Reactor_Equilibrium1 to MaterialStream5
sim.ConnectObjects(MaterialStream7.GraphicObject, Reactor_Equilibrium1.GraphicObject, -1, -1)  # MaterialStream7 to Reactor_Equilibrium1
sim.ConnectObjects(ComponentSeparator2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # ComponentSeparator2 to MaterialStream3
sim.ConnectObjects(MaterialStream1.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream1 to Cooler1
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream9 to Mixer1
sim.ConnectObjects(MaterialStream8.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream8 to Compressor1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_29.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_29.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

