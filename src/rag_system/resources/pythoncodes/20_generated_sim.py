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
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)

# Adding Simulation Objects
# Adding MaterialStream: MAT_ac69dd69_133f_4c9d_8faa_a586690e0f97
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 921, 646, "recycled bottoms")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(383.540344300248)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.15176132797205)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_89b5ed60_4893_4b5c_9e3e_6fee0b619768
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1315, 652, "REC-009")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_0256f50f_0094_4e9c_882f_6f77c1a49379
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 942, 483, "feed")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298.15)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(2.36465277777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_885ebb93_f688_487c_8451_4c1030976d95
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1210, 622, "cooled bottoms")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(356.472829318038)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.15176132797205)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_3dc57531_4c87_4b56_a0f0_18dec5e4bf19
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1095, 617, "HE-006")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding EnergyStream: EN_5d392d44_1477_4d2d_a149_7ae3acd8b8d9
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1356, 499, "r duty")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_251f41a3_17e2_4542_843e_28f11fd8b022
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1341, 323, "c duty")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_20c3dc4a_84bb_4d47_a00f_3f55331f38d5
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1361, 579, "bottoms")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(383.540341514734)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.15176131726743)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_93398209_a3f8_448b_a4af_2596ea13332b
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1398, 393, "distillate")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(355.19831333218)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.2128463619059)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_24fb46b5_6c48_41a8_9100_289a7a90e87f
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 1148, 385, "DC-001")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_62d7f6aa_4504_42fb_9b65_eb8b570bc868
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1071, 451, "preheated feed")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(313.46973907719)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(2.36465277777778)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream5)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream4)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream2)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream1)  # ConnectReboilerDuty 
sim.ConnectObjects(MaterialStream1.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream1 to HeatExchanger1
sim.ConnectObjects(MaterialStream6.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream6 to DistillationColumn1
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream6
sim.ConnectObjects(MaterialStream2.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream2 to HeatExchanger1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream3
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_20.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_20.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

