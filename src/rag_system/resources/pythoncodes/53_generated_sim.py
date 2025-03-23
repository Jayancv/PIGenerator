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
n_heptane = sim.AvailableCompounds["N-heptane"]
sim.SelectedCompounds.Add(n_heptane.Name, n_heptane)
methyl_1_propanol_2 = sim.AvailableCompounds["2-methyl-1-propanol"]
sim.SelectedCompounds.Add(methyl_1_propanol_2.Name, methyl_1_propanol_2)

# Adding Simulation Objects
# Adding MaterialStream: MAT_02e64f2a_1339_4522_a8e9_0597c918fda8
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2759, 757, "Recycle from HPC")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(439.94425694086)  # Temperature in K
MaterialStream1.SetPressure(1215900)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.26563704955944)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_caf19184_9568_4d85_8914_cb0f0a9212ad
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2856, 756, "REC-025")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_f016d390_e04c_4c7e_81ce_cf05ac17f0f8
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 3132, 1077, "MSTR-024")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(439.94425694086)  # Temperature in K
MaterialStream2.SetPressure(1215900)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.26563704955944)  # Mass Flow in kg/s

# Adding Valve: VALV_d850963c_c33c_4bb3_9a29_a3127c71306d
Valve1 = sim.AddObject(ObjectType.Valve, 3039, 1067, "VALV-023")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_8a941a1b_8b3f_4004_9d20_54cb77ca5083
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2940, 1132, "MSTR-022")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(439.94425694086)  # Temperature in K
MaterialStream3.SetPressure(1215900)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.26563704955944)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3d924e79_a036_4601_94db_0a610718142a
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2990, 915, "N-HEPTANE")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(425.28761014804)  # Temperature in K
MaterialStream4.SetPressure(1215900)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.556039788923872)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_72448039_2072_4a88_bea0_842833867b87
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2862, 1002, "HPC")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_efa95d0c_b0da_4131_b870_dafcdf130eb5
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2782, 1009, "MSTR-019")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(374.766306363664)  # Temperature in K
MaterialStream5.SetPressure(1215900)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.82167675112242)  # Mass Flow in kg/s

# Adding Valve: VALV_41032154_7329_4ed4_91c5_02a2695c7a98
Valve2 = sim.AddObject(ObjectType.Valve, 2732, 999, "VALV-018")
Valve2 = Valve2.GetAsObject()

# Adding CapeOpenUO: COUO_73105f5e_bf44_4352_9d47_54efc2f2d58b
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 2518, 959, "LPC")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()
print(" CapeOpenUO2")

# Adding MaterialStream: MAT_f46baff6_aeb6_4a31_abaa_66502f272aa9
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2603, 899, "MSTR-016")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(374.766306363664)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(1.82167675112242)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_079b0cb0_78bf_426e_9188_1df25a4174e3
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2609, 1123, "ISOBUTANOL")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(380.797046544106)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.64996970729321)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_193819dc_bb22_45ad_b234_717109db823d
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2443, 1041, "Feed2")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(313.15)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(2.20386666666667)  # Mass Flow in kg/s
print("MaterialStream8")

# Adding MaterialStream: MAT_6f0f030d_51a9_42d5_bdde_54fba1d7def0
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1279, 1211, "feed")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(313.15)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.20386666666667)  # Mass Flow in kg/s
print("MaterialStream9")
# Adding CapeOpenUO: COUO_92297909_ae1d_4ab1_8f5e_93785858e6f1
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO,1415,1159 , "LPC1")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()
print("CapeOpenUO3")
# Adding MaterialStream: MAT_ef38e397_d8d2_49e2_971d_3190f3694e81
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1491, 1113, "MSTR-003")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(374.766487414927)  # Temperature in K
MaterialStream10.SetPressure(101325)  # Pressure in Pa
MaterialStream10.SetMassFlow(1.75564768125028)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_839610a3_b7ec_440a_abb0_e6d4fdaef187
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1493, 1310, "Isobutanol")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(380.797046544108)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(1.64899626632298)  # Mass Flow in kg/s

# Adding Valve: VALV_3bf55fc6_fa83_49f8_81b0_71e82f87b6b0
Valve3 = sim.AddObject(ObjectType.Valve, 1621, 1110, "VALV-005")
Valve3 = Valve3.GetAsObject()

# Adding MaterialStream: MAT_bfccbeaf_c679_4829_8706_b5e71b7ebd39
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1708, 1121, "MSTR-006")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(374.766487414927)  # Temperature in K
MaterialStream12.SetPressure(405300)  # Pressure in Pa
MaterialStream12.SetMassFlow(1.75564768125028)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_c3a8d7c2_9db0_42c5_a580_21d98fbf1284
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 1809, 1124, "HPC1")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()
print("CapeOpenUO4")
# Adding MaterialStream: MAT_686107bb_8974_4dda_ba2a_ea058103d24f
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1921, 1037, "Recyle back to first column")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(404.29185179997)  # Temperature in K
MaterialStream13.SetPressure(405300)  # Pressure in Pa
MaterialStream13.SetMassFlow(1.200775788509)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0600d28e_d1ae_49c5_9383_a1c13f0ddaa9
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1905, 1287, "N-heptane")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(426.82058808471)  # Temperature in K
MaterialStream14.SetPressure(405300)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.554871887257877)  # Mass Flow in kg/s

# Adding Valve: VALV_42381f53_f1a9_496e_b234_65aa1e9846e2
Valve4 = sim.AddObject(ObjectType.Valve, 1787, 969, "VALV-010")
Valve4 = Valve4.GetAsObject()
print( " Valve4")

# Adding MaterialStream: MAT_2e801a04_d8e2_447b_853b_6cee906613c3
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1721, 934, "MSTR-011")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(376.185882532388)  # Temperature in K
MaterialStream15.SetPressure(101325)  # Pressure in Pa
MaterialStream15.SetMassFlow(1.200775788509)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_39a6fac5_115a_4527_b4a4_c996a6560cde
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1600, 940, "REC-012")
Recycle2 = Recycle2.GetAsObject()
print("Recycle2: ")
# Adding MaterialStream: MAT_52f17ee4_757a_451b_bc36_fe11ed3cd4fe
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1305, 945, "Recycle stream")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(376.185882532388)  # Temperature in K
MaterialStream16.SetPressure(101325)  # Pressure in Pa
MaterialStream16.SetMassFlow(1.200775788509)  # Mass Flow in kg/s
print( "MaterialStream16")
sim.ConnectObjects(MaterialStream1.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream1 to CapeOpenUO2
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Valve3 to MaterialStream12
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream6.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream6 to Valve2
sim.ConnectObjects(MaterialStream12.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream12 to CapeOpenUO4
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream6
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(MaterialStream13.GraphicObject, Valve4.GraphicObject, -1, -1)  # MaterialStream13 to Valve4
sim.ConnectObjects(MaterialStream5.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream5 to CapeOpenUO1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream10
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream14
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream11
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Valve2 to MaterialStream5
# sim.ConnectObjects(MaterialStream8.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream8 to CapeOpenUO2
sim.ConnectObjects(Valve4.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Valve4 to MaterialStream15
sim.ConnectObjects(MaterialStream10.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream10 to Valve3
sim.ConnectObjects(MaterialStream2.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream2 to Recycle1
sim.ConnectObjects(MaterialStream15.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream15 to Recycle2
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream13
sim.ConnectObjects(MaterialStream16.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream16 to CapeOpenUO3
# sim.ConnectObjects(MaterialStream9.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream9 to CapeOpenUO3
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Valve1 to MaterialStream2
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Recycle2 to MaterialStream16
sim.ConnectObjects(MaterialStream3.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream3 to Valve1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_53.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_53.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

