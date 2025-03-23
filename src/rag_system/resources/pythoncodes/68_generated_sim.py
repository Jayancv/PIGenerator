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
dichloroethane_1_2 = sim.AvailableCompounds["1,2-dichloroethane"]
sim.SelectedCompounds.Add(dichloroethane_1_2.Name, dichloroethane_1_2)
vinyl_chloride = sim.AvailableCompounds["Vinyl chloride"]
sim.SelectedCompounds.Add(vinyl_chloride.Name, vinyl_chloride)
ethylene = sim.AvailableCompounds["Ethylene"]
sim.SelectedCompounds.Add(ethylene.Name, ethylene)
chlorine = sim.AvailableCompounds["Chlorine"]
sim.SelectedCompounds.Add(chlorine.Name, chlorine)
hydrogen_chloride = sim.AvailableCompounds["Hydrogen chloride"]
sim.SelectedCompounds.Add(hydrogen_chloride.Name, hydrogen_chloride)

# Adding Simulation Objects
# Adding MaterialStream: MAT_9945d6b1_299e_4427_a14c_4434dde8ac9b
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2496, 973, "11-HCL")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(248.831385165609)  # Temperature in K
MaterialStream1.SetPressure(1215900)  # Pressure in Pa
MaterialStream1.SetMassFlow(7.34951021095641)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_abc910da_6341_4842_9952_ec35e8f97c85
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2487, 1143, "12")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(364.17634398363)  # Temperature in K
MaterialStream2.SetPressure(1215900)  # Pressure in Pa
MaterialStream2.SetMassFlow(25.9043516718402)  # Mass Flow in kg/s

# Adding EnergyStream: EN_56db8ef9_ee32_4632_8049_d25ae5622588
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2480, 1068, "E-105")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_19bf4740_2a16_4cbf_8a77_9a9a6a968ec8
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2481, 934, "E--104")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding DistillationColumn: DC_ab57655c_6e3d_45ea_afc5_61df60109f7a
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2297, 929, "HCL Column")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding MaterialStream: MAT_72e52d34_1848_4b91_891f_bc2457327685
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2212, 1019, "10")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(279.15000296716)  # Temperature in K
MaterialStream3.SetPressure(1215900)  # Pressure in Pa
MaterialStream3.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding Valve: VALV_39f765fe_9528_422c_95d1_20c8f86caf51
Valve1 = sim.AddObject(ObjectType.Valve, 2141, 1019, "Valve")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_e2455ac1_53e0_4986_b597_9d9852c55d51
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2056, 1020, "9")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(279.15)  # Temperature in K
MaterialStream4.SetPressure(2634450)  # Pressure in Pa
MaterialStream4.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding EnergyStream: EN_19461c26_555b_4ab5_b91c_f81e538d9250
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2328, 783, "E-103")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding Cooler: RESF_947b4321_f8f6_4e6d_ba91_43071cd4bf7b
Cooler1 = sim.AddObject(ObjectType.Cooler, 2341, 706, "Condenser")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_87107fbb_cf9a_40d1_9bdc_5c6594f7b1de
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2280, 709, "8")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(443.15)  # Temperature in K
MaterialStream5.SetPressure(2634450)  # Pressure in Pa
MaterialStream5.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding EnergyStream: EN_9295ae32_25f3_46cb_89c9_206371bc9923
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2258, 767, "V-100")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding Cooler: RESF_813ee146_7dc8_4dc5_a58a_a75e21105270
Cooler2 = sim.AddObject(ObjectType.Cooler, 2219, 706, "Quench ")
Cooler2 = Cooler2.GetAsObject()

# Adding MaterialStream: MAT_e0598df0_e395_45cd_964d_7645f8c3a0c7
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1501, 826, "Ethylene 1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(298.15)  # Temperature in K
MaterialStream6.SetPressure(7020026.98680818)  # Pressure in Pa
MaterialStream6.SetMassFlow(5.65559126576889)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_47193a0c_a48a_4bd8_b30b_9f4bf375785f
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1504, 892, "Chlorine 2")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(248.890622031729)  # Temperature in K
MaterialStream7.SetPressure(151987.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(14.2942075532667)  # Mass Flow in kg/s

# Adding NodeIn: MIST_d6026a40_7f23_428e_9e19_568c4965d45f
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1591, 853, "Mix-1")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_534a7f66_f7de_4968_b64e_124ef05b978b
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1646, 853, "Rin")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(276.412199935477)  # Temperature in K
MaterialStream8.SetPressure(151987.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(19.9497988190356)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_893190c1_b2a7_4d6c_8bd2_851845a3e3e2
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1698, 838, "Direct Chlorination Reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_2912571c_3ce9_4265_903d_e1cb78f1a3a9
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1804, 791, "Zero Outlet")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(363.15)  # Temperature in K
MaterialStream9.SetPressure(151987.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6d4f6918_cc67_4e6f_b39f_08fecf50a91c
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1739, 971, "3")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(363.15)  # Temperature in K
MaterialStream10.SetPressure(151987.5)  # Pressure in Pa
MaterialStream10.SetMassFlow(19.9497988190356)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ad799f18_2590_4d25_be29_5b4d910c36a9
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1668, 908, "E-100")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_491de525_0652_458f_8c6a_ca0bf6067d1b
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1782, 1198, "16")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(363.15)  # Temperature in K
MaterialStream11.SetPressure(151987.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(13.3024646122405)  # Mass Flow in kg/s

# Adding NodeIn: MIST_e55afae7_7273_4a2b_9ea9_ecdac52c6519
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1781, 1012, "Mix-2")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_eab2ac54_3656_4601_b386_532a05b9a2c9
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1837, 1022, "4")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(363.15)  # Temperature in K
MaterialStream12.SetPressure(151987.5)  # Pressure in Pa
MaterialStream12.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding Pump: BB_eba8b050_b93c_4a4c_8015_71ccb0eddc8c
Pump1 = sim.AddObject(ObjectType.Pump, 1905, 1049, "Reactor Pump")
Pump1 = Pump1.GetAsObject()

# Adding EnergyStream: EN_48ece4e0_c58e_4d3f_9a02_c7e998969aec
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1947, 1104, "P-100")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_3c24acc3_b1e3_4d14_8e73_b596575a81b6
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1962, 956, "5")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(364.64828554777)  # Temperature in K
MaterialStream13.SetPressure(2634450)  # Pressure in Pa
MaterialStream13.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding Heater: AQ_bcc7e42c_b76a_4c18_a774_3d84749b910d
Heater1 = sim.AddObject(ObjectType.Heater, 1957, 872, "Evaporator")
Heater1 = Heater1.GetAsObject()

# Adding MaterialStream: MAT_77cecab6_ff99_4c9e_9cf7_4fc4fda7d982
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1991, 725, "6")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(515.15)  # Temperature in K
MaterialStream14.SetPressure(2634450)  # Pressure in Pa
MaterialStream14.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding EnergyStream: EN_c22ab71f_20ee_4d7b_81c3_faa1250638f6
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2007, 874, "E-101")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding RCT_Conversion: RC_3d8d4c11_9ea8_4d28_90ea_ec660566c8bc
Reactor_Conversion2 = sim.AddObject(ObjectType.RCT_Conversion, 2027, 711, "Pyrolysis Furnace")
Reactor_Conversion2 = Reactor_Conversion2.GetAsObject()

# Adding MaterialStream: MAT_d209f435_3e05_4c6f_bbc3_343f8f1e488d
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2131, 799, "No Outlet")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(773.15)  # Temperature in K
MaterialStream15.SetPressure(2634450)  # Pressure in Pa
MaterialStream15.SetMassFlow(-7.38348569646078E-15)  # Mass Flow in kg/s

# Adding EnergyStream: EN_10a87a9f_4048_44bc_81c7_a5dfa1b27e4d
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2002, 785, "F-100")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding MaterialStream: MAT_85af5598_f32c_4789_a45b_0f66175355ce
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2162, 710, "7")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(773.15)  # Temperature in K
MaterialStream16.SetPressure(2634450)  # Pressure in Pa
MaterialStream16.SetMassFlow(33.2522634312761)  # Mass Flow in kg/s

# Adding Valve: VALV_269a1fda_e0b0_4ecc_aa67_dfa35a435ef9
Valve2 = sim.AddObject(ObjectType.Valve, 2553, 1075, "Valve1")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_a8b320da_dd8a_4d18_b649_0c8df4208883
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2593, 997, "13")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(331.356198721357)  # Temperature in K
MaterialStream17.SetPressure(486360)  # Pressure in Pa
MaterialStream17.SetMassFlow(25.9043516718402)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_eb14a5f4_1d1d_49dd_8a73_9249f9ea540e
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2644, 931, "VC Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_2c8f5b5d_9fd8_4f18_9455_17168ce0c7da
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2926, 895, "14- VC")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(305.327980787364)  # Temperature in K
MaterialStream18.SetPressure(486360)  # Pressure in Pa
MaterialStream18.SetMassFlow(12.6018870575743)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fbae61c0_2007_412b_88c8_78f83d7b81e9
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2810, 1197, "15")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(416.750034167641)  # Temperature in K
MaterialStream19.SetPressure(486360)  # Pressure in Pa
MaterialStream19.SetMassFlow(13.3024646122405)  # Mass Flow in kg/s

# Adding Cooler: RESF_92c6f43c_5092_4052_86c3_7b64272c4946
Cooler3 = sim.AddObject(ObjectType.Cooler, 2642, 1195, "Recycle Cooler")
Cooler3 = Cooler3.GetAsObject()

# Adding EnergyStream: EN_753a5d5b_f8e1_4872_89f6_fee53ac93dc7
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2688, 1159, "E-108")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_d96d458d_0595_451a_a3c6_3df0d95bd3c6
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2316, 1198, "Recycle")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(363.15)  # Temperature in K
MaterialStream20.SetPressure(151987.5)  # Pressure in Pa
MaterialStream20.SetMassFlow(13.3024646122405)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_2dce2f54_a4b4_42ce_896e_81f4c0a60848
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2133, 1198, "REC-042")
Recycle1 = Recycle1.GetAsObject()

# Adding Valve: VALV_957afcc7_aff5_4237_945b_97825b9e37f5
Valve3 = sim.AddObject(ObjectType.Valve, 2449, 1198, "Valve2")
Valve3 = Valve3.GetAsObject()

# Adding MaterialStream: MAT_78f07eb8_e24b_425d_a2dd_d4d900f577ac
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 2541, 1198, "MSTR-044")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(363.15)  # Temperature in K
MaterialStream21.SetPressure(486360)  # Pressure in Pa
MaterialStream21.SetMassFlow(13.3024646122405)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream1)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream2)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream2)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream1)  # ConnectReboilerDuty 
sim.ConnectObjects(MaterialStream16.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream16 to Cooler2
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(MaterialStream17.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream17 to CapeOpenUO1
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream11 to Mixer2
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream6 to Mixer1
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream15
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream9
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream10
sim.ConnectObjects(MaterialStream8.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream8 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream7 to Mixer1
sim.ConnectObjects(MaterialStream19.GraphicObject, Cooler3.GraphicObject, -1, -1)  # MaterialStream19 to Cooler3
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # Cooler2 to EnergyStream4
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream18
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream19
sim.ConnectObjects(MaterialStream3.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream3 to DistillationColumn1
sim.ConnectObjects(Cooler3.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Cooler3 to MaterialStream21
sim.ConnectObjects(Reactor_Conversion2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Reactor_Conversion2 to MaterialStream16
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Heater1 to MaterialStream14
sim.ConnectObjects(Cooler3.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # Cooler3 to EnergyStream9
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Pump1 to MaterialStream13
sim.ConnectObjects(EnergyStream6.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream6 to Pump1
sim.ConnectObjects(MaterialStream14.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # MaterialStream14 to Reactor_Conversion2
sim.ConnectObjects(MaterialStream13.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream13 to Heater1
sim.ConnectObjects(MaterialStream12.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream12 to Pump1
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream10 to Mixer2
sim.ConnectObjects(MaterialStream5.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream5 to Cooler1
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Valve3 to MaterialStream20
sim.ConnectObjects(MaterialStream2.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream2 to Valve2
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Mixer1 to MaterialStream8
sim.ConnectObjects(EnergyStream5.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream5 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream21.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream21 to Valve3
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Recycle1 to MaterialStream11
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # Cooler1 to EnergyStream3
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Cooler1 to MaterialStream4
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Mixer2 to MaterialStream12
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Valve2 to MaterialStream17
sim.ConnectObjects(EnergyStream8.GraphicObject, Reactor_Conversion2.GraphicObject, -1, -1)  # EnergyStream8 to Reactor_Conversion2
sim.ConnectObjects(MaterialStream20.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream20 to Recycle1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Valve1 to MaterialStream3
sim.ConnectObjects(EnergyStream7.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream7 to Heater1
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Cooler2 to MaterialStream5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_68.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_68.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

