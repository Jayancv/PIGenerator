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
toluene = sim.AvailableCompounds["Toluene"]
sim.SelectedCompounds.Add(toluene.Name, toluene)
methylcyclohexane = sim.AvailableCompounds["Methylcyclohexane"]
sim.SelectedCompounds.Add(methylcyclohexane.Name, methylcyclohexane)
phenol = sim.AvailableCompounds["Phenol"]
sim.SelectedCompounds.Add(phenol.Name, phenol)

# Adding Simulation Objects
# Adding EnergyStream: EN_d65ad138_0654_4938_88dc_277a88b01f40
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1521, 1026, "E-1")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_6df93a57_21b4_4acc_b73c_53c505de01fc
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1073, 816, "Excess Phenol MakeUp")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(373)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(4.70565)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_d6e30ff5_933c_4a44_8681_aacdc643ef03
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1152, 868, "MakeUp Mixer")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_1e8b724d_6835_4412_840d_3c6d3d214ff0
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1080, 948, "Recycle Solvent")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(373)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(4.70480495830423)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b3308a54_19f4_4e75_b007_daafe7408b13
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1190, 739, "Surplus Phenol makeUp")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(372.999158685156)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(4.70482460878651)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_32d3d7df_a869_49d3_b98e_c5b6b6c08982
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1251, 878, "Phenol")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(373)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(4.70563034951772)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_cbb995e0_63fe_4867_82bb_ac59cfbf2ce2
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1349, 867, "Extractive Column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_4a493649_2578_468a_8307_91cf105eb5d8
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1308, 737, "Toluene-MCH")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(384)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.90329)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e5a47ddb_ce3a_40b8_ba02_10cad8237355
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1488, 739, "MethylCycloHexane")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(374.003055282751)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.985855283660179)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d0c0128f_4812_4549_a5c5_d07554bd098f
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1487, 933, "Phenol-Toluene")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(419.195804247509)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(5.6230650658574)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_812a1180_a43f_4373_b040_080292c17ca3
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1595, 925, "Solvent Recovery")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_62584e1d_27d0_4bee_96d0_87595938e2b1
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1735, 839, "Toluene")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(383.551743017671)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.918519129313112)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6356a478_140d_4395_b1cd_c406919f76d4
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1733, 1005, "S-8")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(454.377913728177)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(4.70454593654485)  # Mass Flow in kg/s

# Adding Cooler: RESF_b3f150e8_de81_4a74_be05_fe11ad64ad6d
Cooler1 = sim.AddObject(ObjectType.Cooler, 1484, 1121, "Cooler")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_c3cd8a87_0a14_46a1_9f6d_fe86ef6119d0
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1368, 1123, "S-9")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(373)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(4.70454593654485)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_39653df1_c10e_4063_adc8_c3a8481d6549
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1188, 1123, "Recycle")
Recycle1 = Recycle1.GetAsObject()

sim.ConnectObjects(MaterialStream9.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream9 to Cooler1
sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO3
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
# sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream8
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream9
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
# sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Cooler1 to MaterialStream10
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(MaterialStream10.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream10 to Recycle1
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_28.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_28.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

