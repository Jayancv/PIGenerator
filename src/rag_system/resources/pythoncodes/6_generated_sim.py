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
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)

# Adding Simulation Objects
# Adding MaterialStream: MAT_1316f091_758c_41fa_964b_d69f3e3d8e42
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 713, 578, "Equimolar Feed")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(300)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.044998)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_81065c8e_9af4_4e4e_80d6_5c6eeaf6f49d
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 793, 483, "Methanol Column (1 atm)")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_02e827bf_bf5c_429d_8c3b_7a8071516e1f
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1006, 483, "LP Azeotrope")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(329.801926862076)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.139890908056837)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a3577b59_ff83_4d28_814c_3a901d5acfda
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1023, 671, "Methanol")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(337.900656319786)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.016021)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ba02ef69_1a52_44ed_aa29_624c2eee7ea5
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 996, 545, "Condenser Duty")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_724fea90_1c4b_4f92_a23b_5f9ce8bd8489
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1000, 637, "Reboiler Duty")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_11467055_6808_43b2_a84e_b3cbd5974a8c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 716, 496, "Recycled HP Azeotrope")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(394.948946954018)  # Temperature in K
MaterialStream4.SetPressure(607950)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.110821868673413)  # Mass Flow in kg/s

# Adding Pump: BB_bd6f57b0_31ff_46ba_8468_b712aa1e2bb9
Pump1 = sim.AddObject(ObjectType.Pump, 1067, 482, "Pump")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_df21fa52_ddbf_4e61_a6bb_9fb208f76a2d
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1147, 479, "HP Feed")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(330.032360273354)  # Temperature in K
MaterialStream5.SetPressure(607950.057)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.139890908056837)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5de080e2_48d5_4d63_98fd_b02fa7fd619b
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1055, 529, "PE-1")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding DistillationColumn: DC_d8d17391_93e8_4990_b225_e42f4f7b0b33
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 1209, 437, "Acetone Column (6 atm)")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding MaterialStream: MAT_2bfc6fd0_cbc8_4b85_84f4_c990c3990d85
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1389, 412, "HP Azeotrope")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(394.948946954018)  # Temperature in K
MaterialStream6.SetPressure(607950)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.110821868673413)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4c626b03_8509_409c_a65d_9d3346c1fff6
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1411, 648, "Acetone Rich Product")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(394.948948149249)  # Temperature in K
MaterialStream7.SetPressure(607950)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.0290399996047787)  # Mass Flow in kg/s

# Adding EnergyStream: EN_b696460e_1663_400d_a21c_87d50b8de316
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1394, 482, "Condenser Duty (2)")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding EnergyStream: EN_4883c9b1_2698_4122_8d02_6b279638b979
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1399, 576, "Reboiler Duty (2)")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding OT_Recycle: REC_dbca834d_696b_435c_9254_f85250dd6aad
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 979, 412, "Recycle Op")
Recycle1 = Recycle1.GetAsObject()

# Adding OT_Adjust: AJ265650f7_9adc_4432_860e_119ac883973b
Adjust1 = sim.AddObject(ObjectType.OT_Adjust, 698, 649, "AJ000")
Adjust1 = Adjust1.GetAsObject()

DistillationColumn1.ConnectDistillate(MaterialStream2)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream3)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream1)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream2)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream6)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream7)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream4)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream5)  # ConnectReboilerDuty 
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Recycle1 to MaterialStream4
sim.ConnectObjects(MaterialStream5.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream5 to DistillationColumn2
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Pump1 to MaterialStream5
sim.ConnectObjects(MaterialStream2.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream2 to Pump1
sim.ConnectObjects(MaterialStream4.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream4 to DistillationColumn1
sim.ConnectObjects(MaterialStream1.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream1 to DistillationColumn1
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream6 to Recycle1
sim.ConnectObjects(EnergyStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream3 to Pump1
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_6.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_6.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

