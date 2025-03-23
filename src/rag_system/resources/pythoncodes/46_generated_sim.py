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
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
acetonitrile = sim.AvailableCompounds["Acetonitrile"]
sim.SelectedCompounds.Add(acetonitrile.Name, acetonitrile)

# Adding Simulation Objects
# Adding OT_Recycle: REC_1448cad9_e799_4688_ab22_310709749a74
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 997, 325, "REC-011")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_4b152aa4_595d_4103_b77c_cf62aad37531
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1182, 447, "BENZENE")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(424.786251202346)  # Temperature in K
MaterialStream1.SetPressure(608000)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0276811045445058)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8591e0ba_c13a_448e_869a_201b611ac95f
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1182, 377, "D3")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(388.194496759931)  # Temperature in K
MaterialStream2.SetPressure(608000)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.375527031830662)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_17a3b59e_17bb_4825_9d17_785beeaf9314
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1056, 397, "COUO-008")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_94c67b7f_456e_48ee_8ff0_45b098593c63
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 995, 466, "METHANOL")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(337.661776390793)  # Temperature in K
MaterialStream3.SetPressure(101000)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.194802936357375)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d5c936ba_707d_4567_998c_bb8d19df3867
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 991, 383, "D2")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(331.7133616844)  # Temperature in K
MaterialStream4.SetPressure(101000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.40320813637418)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_81d07fdb_2509_417f_95c4_574774035442
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 872, 408, "COUO-005")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_8033f4d2_94e1_4c62_b0d0_3a09264fc164
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 807, 475, "ACETONITRILE")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(424.19508707804)  # Temperature in K
MaterialStream5.SetPressure(608000)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.0552644551847915)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ce0e1fda_7b15_48d7_8438_30a761a8265f
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 811, 382, "D1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(387.837899731956)  # Temperature in K
MaterialStream6.SetPressure(608000)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.598011072732506)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_766298b5_ba52_4850_b1c6_ea4e0036ad5c
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 673, 392, "COUO-002")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_7be0827e_e9e7_4264_a68c_d5d66fa2b3ad
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 602, 443, "FEED")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(323)  # Temperature in K
MaterialStream7.SetPressure(608000)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_27973220_a780_4b19_9b93_74ec5f8d2e20
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 603, 372, "RECYCLE")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(388.194496759931)  # Temperature in K
MaterialStream8.SetPressure(608000)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.375527031830662)  # Mass Flow in kg/s

sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO3
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream3
sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream2 to Recycle1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream6
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Recycle1 to MaterialStream8
# sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO3
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_46.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_46.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

