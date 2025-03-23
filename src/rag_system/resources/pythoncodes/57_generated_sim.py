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
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
acetonitrile = sim.AvailableCompounds["Acetonitrile"]
sim.SelectedCompounds.Add(acetonitrile.Name, acetonitrile)

# Adding Simulation Objects
# Adding EnergyStream: EN_3ac97d92_fbdd_429a_ab6e_3b0718950331
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1427, 1085, "Energy Stream")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_020103c0_a49d_446b_bf05_dfe8e0c31b7d
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1479, 1016, "Feed to Column-II")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(348.139265508018)  # Temperature in K
MaterialStream1.SetPressure(303975)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.84515007440752)  # Mass Flow in kg/s

# Adding Pump: BB_e3c27774_1d6b_4f0c_8b36_f1e8b14181c4
Pump1 = sim.AddObject(ObjectType.Pump, 1423, 1023, "PUMP")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_fbae4de1_6fa8_46f1_8108_00e2248410f7
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1207, 975, "Split Stream")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(361.564727933643)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.49590705159351)  # Mass Flow in kg/s

# Adding Valve: VALV_e507fcab_178e_4014_b4ec_dba3ab7209ca
Valve1 = sim.AddObject(ObjectType.Valve, 1171, 926, "VALVE")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_2cfc8bbd_41e9_48ce_8e21_b8c1e6e2155c
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1371, 895, "Recycle")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(382.84217065922)  # Temperature in K
MaterialStream3.SetPressure(303975)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.49585154490066)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_cb6acaa6_3e07_4c54_b807_d4c3cccaa534
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1596, 922, "Recycle Block")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_6bd99770_eba5_4d97_95f0_a3f015294e5c
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1576, 1114, "99 mol% ACN")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(394.243933674927)  # Temperature in K
MaterialStream4.SetPressure(303975)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.349298529506874)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_2f8f1cc4_ee03_4838_a834_ba8ad41a00e3
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1526, 1008, "Column-II 3 atm")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_06224209_8606_4631_aa39_203b91bda7f5
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1596, 987, "Distillate-2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(382.84217065922)  # Temperature in K
MaterialStream5.SetPressure(303975)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.49585154490066)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0d0d56a2_0a6a_4300_8736_72794c0dc641
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1365, 1081, "Steam")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(373.130299019514)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.346342997678711)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_36ba110a_564e_4ff0_9251_3853e87d09cc
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1376, 1002, "Azeotrope")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(348.02074341282)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.84515007440752)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_176e4afc_af51_4a00_be7f_7b76d5a01977
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 1286, 1001, "COUO-001")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_367c78e8_43bc_4f3c_b381_598de311d073
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1082, 1049, "Fresh Feed")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(308)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.695586020540551)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_0468c0f4_a708_4896_8532_8e6db8a61be7
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1144, 1046, "Heat Exchanger")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_734b71cc_0498_4e58_af74_8abbaa1604d5
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1149, 995, "Water")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(345.714645935292)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.346346705232472)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_89cc5f92_e45b_43d8_b485_c397fefe4ba7
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1213, 1045, "Feed to Distillation")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(326.846622728592)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.695586020540551)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_86bb7c87_46d8_44dc_a52a_a312255d6f49
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1289, 1135, "RECYCLE")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_5fa75570_3378_432b_bd6f_8ebd5593edf5
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1189, 1126, "Steam to Heat Exchamger")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(373.130299019514)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(0.346342997678711)  # Mass Flow in kg/s

sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Recycle2 to MaterialStream11
sim.ConnectObjects(MaterialStream11.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream11 to HeatExchanger1
sim.ConnectObjects(MaterialStream7.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream7 to Pump1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream9
sim.ConnectObjects(MaterialStream8.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream8 to HeatExchanger1
sim.ConnectObjects(MaterialStream2.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream2 to CapeOpenUO2
# sim.ConnectObjects(MaterialStream10.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream10 to CapeOpenUO2
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Pump1 to MaterialStream1
sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO1
sim.ConnectObjects(MaterialStream3.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream3 to Valve1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Valve1 to MaterialStream2
sim.ConnectObjects(MaterialStream5.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream5 to Recycle1
sim.ConnectObjects(EnergyStream1.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream1 to Pump1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Recycle1 to MaterialStream3
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream6 to Recycle2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream10
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_57.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_57.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

