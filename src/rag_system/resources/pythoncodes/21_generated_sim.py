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
butanol_1 = sim.AvailableCompounds["1-butanol"]
sim.SelectedCompounds.Add(butanol_1.Name, butanol_1)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)

# Adding Simulation Objects
# Adding OT_Recycle: REC_864be21d_569d_4bb7_8365_36739e58688d
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1649, 755, "REC-017")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_eb52a438_0842_4467_b5df_d8c648aa5c34
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1578, 745, "MSTR-016")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(343.15)  # Temperature in K
MaterialStream1.SetPressure(50662.5)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.729767419111639)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5c846017_6af8_463b_a0ea_3de79270392b
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1578, 645, "MSTR-015")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(343.15)  # Temperature in K
MaterialStream2.SetPressure(50662.5)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.763490825923065)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_97af296c_0570_406e_a650_7a83377bc509
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1496, 676, "DECMODEL")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding OT_Recycle: REC_7844c3ba_c877_4a51_93ef_f4b0e9c8c368
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1591, 598, "REC-018")
Recycle2 = Recycle2.GetAsObject()

# Adding EnergyStream: EN_2aa3b97f_1ea8_4faf_b1db_6b8afcf08691
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1410, 553, "ESTR-013")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_ab43919f_aee1_4391_8018_e469b7b503b5
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1433, 662, "MSTR-012")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(343.15)  # Temperature in K
MaterialStream3.SetPressure(50662.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.49325824503467)  # Mass Flow in kg/s

# Adding Cooler: RESF_f5df5b1b_ee4e_4604_a48c_07202b79ed5c
Cooler1 = sim.AddObject(ObjectType.Cooler, 1473, 533, "COOL-011")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_330affce_e80a_4563_af3c_eca330a34422
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1455, 477, "MSTR-010")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(349.639143970148)  # Temperature in K
MaterialStream4.SetPressure(50662.5)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.49325824503467)  # Mass Flow in kg/s

# Adding NodeIn: MIST_ece5e4a4_e6d3_465f_9706_89286019c54b
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1445, 377, "MIX-009")
Mixer1 = Mixer1.GetAsObject()

# Adding CapeOpenUO: COUO_b0ee02c5_6931_4940_9277_6cc0d601598e
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1178, 503, "RABS1")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_74e46c09_8317_4252_84fc_1f22e6d948f1
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1270, 618, "WATER")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(354.354010469988)  # Temperature in K
MaterialStream5.SetPressure(50662.5)  # Pressure in Pa
MaterialStream5.SetMassFlow(4.91897871281932)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4caef934_4c9e_44aa_b378_731ca8e631ee
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1271, 466, "OH1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(351.13287268565)  # Temperature in K
MaterialStream6.SetPressure(50662.5)  # Pressure in Pa
MaterialStream6.SetMassFlow(1.12422157864927)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c2dff00e_ed32_413f_91ae_6e77e78fbbbe
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1131, 562, "AQUEOUS")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(343.15)  # Temperature in K
MaterialStream7.SetPressure(50662.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.727322515164363)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_aa35ce24_b742_4fcc_a837_d0b7947eca0c
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1132, 496, "FEED")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(351.125)  # Temperature in K
MaterialStream8.SetPressure(50662.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(5.31587777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b9c55315_237c_4a86_8978_3f501563edef
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1578, 538, "ORGANIC")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(343.15)  # Temperature in K
MaterialStream9.SetPressure(50662.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.768903130668916)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_c73e6fd8_0980_4847_bb25_6ab11c0e48df
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1620, 526, "RABS2")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_e2d36e1e_5b66_447f_89ea_51c8a4d8d177
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1704, 480, "OH2")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(348.90955001743)  # Temperature in K
MaterialStream10.SetPressure(50662.5)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.369036666385403)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_612e7d4f_f424_41d9_9e8e_a02d306a5278
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1704, 581, "BUTANOL")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(367.47862318588)  # Temperature in K
MaterialStream11.SetPressure(50662.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.399866464283631)  # Mass Flow in kg/s

sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Cooler1 to MaterialStream3
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Mixer1 to MaterialStream4
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler1 to EnergyStream1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream1.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream1 to Recycle1
sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO2
sim.ConnectObjects(MaterialStream4.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream4 to Cooler1
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream2 to Recycle2
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Recycle1 to MaterialStream7
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream11
sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO3
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream10
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream10 to Mixer1
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Recycle2 to MaterialStream9
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO1
sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO2
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_21.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_21.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

