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
n_n_dimethylformamide = sim.AvailableCompounds["N,n-dimethylformamide"]
sim.SelectedCompounds.Add(n_n_dimethylformamide.Name, n_n_dimethylformamide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
methylal = sim.AvailableCompounds["Methylal"]
sim.SelectedCompounds.Add(methylal.Name, methylal)

# Adding Simulation Objects
# Adding EnergyStream: EN_ad8dd87e_9987_477a_9cec_b8f8d78ba5fa
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1166, 321, "ESTR-014")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding Cooler: RESF_fb491b52_f611_4f6e_b8e7_2e75860ec0fb
Cooler1 = sim.AddObject(ObjectType.Cooler, 1231, 294, "COOL-013")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_019475b0_bd47_4854_8e13_2d7cb85e73e2
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1246, 401, "MSTR-012")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(425.998)  # Temperature in K
MaterialStream1.SetPressure(101325)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.802627777777778)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_1026a4bc_6b29_46c6_8483_b80beb6c38c0
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1214, 502, "REC-011")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_d6a84528_9f04_4ae4_9976_f2f8c2bf3f25
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1002, 474, "MSTR-007")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(394.299066505834)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.855931934470541)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ab864ada_edfd_432f_a983_9da8ec779ed0
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1037, 381, "PURE METHYLAL")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(315.286454452488)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.780039148861107)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_e50e50f1_b3eb_43bf_b54c_f7e97d587a4a
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 912, 410, "AZEO BREAKER")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_caf648aa_169a_4376_9ade_b0bb14d8319f
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 812, 377, "MSTR-004")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(300)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.80263775)  # Mass Flow in kg/s

# Adding NodeIn: MIST_f2d8c432_98ee_45af_906c_0db57a88a246
Mixer1 = sim.AddObject(ObjectType.NodeIn, 740, 354, "MIX-003")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_8015a462_99ff_48d7_865b_c2c12d6779ab
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 688, 372, "MAKE UP DMF")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(300)  # Temperature in K
MaterialStream5.SetPressure(120000)  # Pressure in Pa
MaterialStream5.SetMassFlow(9.97222222222222E-06)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_69c646be_7677_4b67_bb8c_bc95217981f4
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 779, 294, "R STREAM")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(300)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.802627777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_70e82d14_b3e1_458d_bc06_81e630b532ec
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 771, 459, "RAW METHYLAL")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(300)  # Temperature in K
MaterialStream7.SetPressure(110000)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.833333333333333)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_50414ba4_7b94_403d_8b94_af5dcfac68f7
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1072, 469, "RECOVERY")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_3fbfece4_10ab_4474_81c8_8f0220dc874c
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1164, 400, "METHANOL")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(337.809311332693)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.0534098683016827)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f2e9fe63_4964_4eee_a6ed_f582170eedb0
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1162, 501, "DMF")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(425.998222130711)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.802522066168812)  # Mass Flow in kg/s

sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream9
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(MaterialStream1.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream1 to Cooler1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
# sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO1
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Mixer1 to MaterialStream4
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream5 to Mixer1
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO2
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Cooler1 to MaterialStream6
sim.ConnectObjects(MaterialStream9.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream9 to Recycle1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_23.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_23.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

