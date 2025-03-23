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
propylene = sim.AvailableCompounds["Propylene"]
sim.SelectedCompounds.Add(propylene.Name, propylene)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)
n_pentane = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(n_pentane.Name, n_pentane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_3a61cdd5_1d7f_4dba_a661_ce96f3667382
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1787, 1041, "MSTR-018")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(324.231046171099)  # Temperature in K
MaterialStream1.SetPressure(2137000)  # Pressure in Pa
MaterialStream1.SetMassFlow(57.2786871115142)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_06adb796_2f64_4cbf_91f5_0ac2771710d9
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2058, 1074, "REC-017")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_acbffac4_9b95_4563_ba45_81e9a0ed8c34
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2202, 933, "MSTR-016")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(324.231046171099)  # Temperature in K
MaterialStream2.SetPressure(2137000)  # Pressure in Pa
MaterialStream2.SetMassFlow(57.2786871115142)  # Mass Flow in kg/s

# Adding EnergyStream: EN_05904821_d7d4_4dd7_8d30_3a3aa2027670
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2060, 782, "Pump duty")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding Pump: BB_6711a679_0556_4019_8f01_7a68572a1c33
Pump1 = sim.AddObject(ObjectType.Pump, 2059, 863, "PUMP-014")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_7c3732f2_e0ce_4c97_bb98_2cd734829d70
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1646, 833, "B1")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(336.135990140144)  # Temperature in K
MaterialStream3.SetPressure(2271822.521)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.89769840770431)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_15bc1748_1f5b_4e8b_ba27_d10e593be86b
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1659, 675, "D1")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(323.635734857725)  # Temperature in K
MaterialStream4.SetPressure(1930532)  # Pressure in Pa
MaterialStream4.SetMassFlow(60.3969935329235)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_05764ece_bccf_481f_a7b9_344ab472d45a
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1978, 855, "B2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(323.902427095101)  # Temperature in K
MaterialStream5.SetPressure(1942943.1444)  # Pressure in Pa
MaterialStream5.SetMassFlow(57.2786871115142)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ca42296a_25b3_4a82_a027_2302251ecc17
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1974, 680, "D2")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(318.747373131745)  # Temperature in K
MaterialStream6.SetPressure(1896058)  # Pressure in Pa
MaterialStream6.SetMassFlow(3.11830565433173)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_0b135d58_9903_45d5_a7e1_77a6b09e05b7
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1786, 741, "Refluxed Absorber")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding NodeIn: MIST_08a0a8ec_9e16_427e_b96c_14e473432961
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1251, 718, "Mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_f860736c_1d08_49b9_88db_0fd391bc66ce
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 953, 674, "Propane")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(310.927777777778)  # Temperature in K
MaterialStream7.SetPressure(1999475.999393)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.994883)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_75125a0c_c3a6_4405_94be_46c40a91bbf0
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 953, 717, "Propylene")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(310.927777777778)  # Temperature in K
MaterialStream8.SetPressure(1999475.999393)  # Pressure in Pa
MaterialStream8.SetMassFlow(3.324805)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a7a2b2c8_8acc_44a1_8528_d8efd2e47acc
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 955, 768, "N Pentane")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(310.927777777778)  # Temperature in K
MaterialStream9.SetPressure(1999475.999393)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.066496)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ecdce8f6_0997_4fbe_9d6c_4c8ecec35808
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1315, 707, "Feed to pump1")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(310.922368240338)  # Temperature in K
MaterialStream10.SetPressure(1999475.999393)  # Pressure in Pa
MaterialStream10.SetMassFlow(5.386184)  # Mass Flow in kg/s

# Adding Pump: BB_816d7447_9574_4876_a3d4_aea43a3d0fb5
Pump2 = sim.AddObject(ObjectType.Pump, 1418, 696, "PUMP 1 ")
Pump2 = Pump2.GetAsObject()

# Adding MaterialStream: MAT_b601b4c2_6a5c_42fb_aae7_7c96336c4483
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1536, 663, "Feed to stripper")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(311.085228973729)  # Temperature in K
MaterialStream11.SetPressure(2137000)  # Pressure in Pa
MaterialStream11.SetMassFlow(5.386184)  # Mass Flow in kg/s

# Adding EnergyStream: EN_cff1f86b_e5ae_409f_b326_aeb5140f61bb
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1412, 761, "Pump duty1")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding CapeOpenUO: COUO_286ad56c_c75e_4153_9ce4_6d869c22f975
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1567, 747, "Reboiled Absorber")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

sim.ConnectObjects(MaterialStream10.GraphicObject, Pump2.GraphicObject, -1, -1)  # MaterialStream10 to Pump2
sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream4.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream4 to CapeOpenUO1
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Pump1 to MaterialStream2
sim.ConnectObjects(EnergyStream2.GraphicObject, Pump2.GraphicObject, -1, -1)  # EnergyStream2 to Pump2
sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(MaterialStream5.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream5 to Pump1
sim.ConnectObjects(Pump2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Pump2 to MaterialStream11
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream9 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream6
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream3
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream7 to Mixer1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream2 to Recycle1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Mixer1 to MaterialStream10
# sim.ConnectObjects(MaterialStream11.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream11 to CapeOpenUO2
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_66.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_66.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

