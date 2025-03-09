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
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
hydrogen_chloride = sim.AvailableCompounds["Hydrogen chloride"]
sim.SelectedCompounds.Add(hydrogen_chloride.Name, hydrogen_chloride)

# Adding Simulation Objects
# Adding MaterialStream: MAT_0f6df4d5_c4b6_48ca_b638_e74c47b8f9df
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1845, 1103, "hydrogen recyle to reactor")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(317.524777352604)  # Temperature in K
MaterialStream1.SetPressure(2550000)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.0954314394713375)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_62dba67a_d7d5_48ae_b5f8_693ca8d1ba54
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1647, 1080, "REC-056")
Recycle1 = Recycle1.GetAsObject()

# Adding OT_Recycle: REC_6137ca8d_9d02_47af_a325_154d40cc3c98
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1768, 1043, "REC-057")
Recycle2 = Recycle2.GetAsObject()

# Adding NodeOut: DIV_57964907_0c7f_4653_8e1b_f20ed7171561
Splitter1 = sim.AddObject(ObjectType.NodeOut, 1946, 1060, "recycle splitter")
Splitter1 = Splitter1.GetAsObject()

# Adding EnergyStream: EN_8055cd5e_d101_4fc3_a366_f7362c0a8775
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2190, 1152, "ESTR-052")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_c319eeca_6ae6_4e08_a105_575d4f763b59
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2030, 1079, "compressed recycle stream")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(317.524203594938)  # Temperature in K
MaterialStream2.SetPressure(2550000)  # Pressure in Pa
MaterialStream2.SetMassFlow(1.90159133350269)  # Mass Flow in kg/s

# Adding Compressor: COMP_c51d9dcb_f33c_4234_b149_98de7f59a1e9
Compressor1 = sim.AddObject(ObjectType.Compressor, 2148, 1097, "COMP-050")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_00dfbeca_dd10_4da0_b800_0d1f2565679e
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2239, 1099, "recycle stream")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(311.15)  # Temperature in K
MaterialStream3.SetPressure(2400000)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.90159133350269)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d010bcf6_a68a_483f_b16c_be8c44701520
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2513, 1075, "to fuel gas")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(311.15)  # Temperature in K
MaterialStream4.SetPressure(2400000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.703328301432501)  # Mass Flow in kg/s

# Adding NodeOut: DIV_eeb4423d_3190_44c8_a40b_adb9e630473c
Splitter2 = sim.AddObject(ObjectType.NodeOut, 2337, 1098, "SPLT-047")
Splitter2 = Splitter2.GetAsObject()

# Adding MaterialStream: MAT_afb5338e_ed13_4b41_9804_75fca862b596
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1716, 1346, "MSTR-057")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(480.305719835146)  # Temperature in K
MaterialStream5.SetPressure(1100000)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.918849804380045)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_246de78c_c56c_403d_8e00_366c0c0f8565
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1698, 1249, "hydrogen recycle")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(317.524777352604)  # Temperature in K
MaterialStream6.SetPressure(2550000)  # Pressure in Pa
MaterialStream6.SetMassFlow(1.80669717660689)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_bede03da_ce52_428b_ae55_12d5436a3ca4
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2039, 1242, "reactor input")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(855.738376171669)  # Temperature in K
MaterialStream7.SetPressure(2550000)  # Pressure in Pa
MaterialStream7.SetMassFlow(5.81867842045827)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c195e5b5_7f14_457f_aa52_15139a038ad2
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1492, 1143, "toluene feed (low pressure)")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(351.514994994616)  # Temperature in K
MaterialStream8.SetPressure(1100000)  # Pressure in Pa
MaterialStream8.SetMassFlow(3.68884980438005)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_d406156e_83dc_4680_8554_eaeae2e36a96
Recycle3 = sim.AddObject(ObjectType.OT_Recycle, 1883, 1357, "toluene recycle block")
Recycle3 = Recycle3.GetAsObject()

# Adding MaterialStream: MAT_ff051830_7f8d_4342_af4b_67ac85c1cf25
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2369, 1153, "vapor stream from high pressure phase separator")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(311.15)  # Temperature in K
MaterialStream9.SetPressure(2400000)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.60491963493519)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1bfbde9a_95ff_4a15_93c3_9d09fcdc3b44
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 3192, 1156, "fuel gas")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(311.436536661124)  # Temperature in K
MaterialStream10.SetPressure(250000)  # Pressure in Pa
MaterialStream10.SetMassFlow(0.711964347347562)  # Mass Flow in kg/s

# Adding NodeIn: MIST_34558460_7fb3_46b2_9902_c28c88274da7
Mixer1 = sim.AddObject(ObjectType.NodeIn, 3117, 1154, "MIX-037")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_c48a7494_6b6e_42d5_b4d5_79796027615f
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2920, 1369, "ESTR-036")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_198431ea_7f03_4df3_aac6_5d6456ed9a51
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 3042, 1332, "benzene")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(385.15)  # Temperature in K
MaterialStream11.SetPressure(250000)  # Pressure in Pa
MaterialStream11.SetMassFlow(2.28588785824708)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d675b144_afce_4534_b09f_6d62a39d99f7
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 3056, 1283, "vapours (methane and hydrogen)")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(385.15007035199)  # Temperature in K
MaterialStream12.SetPressure(250000)  # Pressure in Pa
MaterialStream12.SetMassFlow(0.00845430276707757)  # Mass Flow in kg/s

# Adding Vessel: SEP_4fecd096_4867_4c81_b7c3_9dec8638baf9
Vessel1 = sim.AddObject(ObjectType.Vessel, 2952, 1282, "SEP-033")
Vessel1 = Vessel1.GetAsObject()

# Adding EnergyStream: EN_4e27e731_8174_4790_94ae_20d453101f46
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2844, 1313, "reboiler duty")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_5b43af30_d9e3_487e_84b5_c8d313c9f9c8
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2895, 1215, "distillate")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(312.413959456978)  # Temperature in K
MaterialStream13.SetPressure(300000)  # Pressure in Pa
MaterialStream13.SetMassFlow(2.29434216101414)  # Mass Flow in kg/s

# Adding EnergyStream: EN_42027774_070b_4eaa_860e_fb464d79368f
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2845, 1199, "Condensor duty")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding ShortcutColumn: SC_ee9edbfa_9c2d_409c_9a70_b4392cde2bb2
ShortcutColumn1 = sim.AddObject(ObjectType.ShortcutColumn, 2659, 1199, "benzene toluene separation column")
ShortcutColumn1 = ShortcutColumn1.GetAsObject()

# Adding EnergyStream: EN_4767ad76_e159_4e80_b0ef_183e1ff0daeb
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2533, 1391, "ESTR-027")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_9425886d_a37e_4eee_8538_64c0356f8971
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2615, 1299, "distillation feed")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(363)  # Temperature in K
MaterialStream14.SetPressure(270000)  # Pressure in Pa
MaterialStream14.SetMassFlow(3.213577119669)  # Mass Flow in kg/s

# Adding Heater: AQ_0c13d708_af9b_4dc5_abeb_cdff953d2155
Heater1 = sim.AddObject(ObjectType.Heater, 2575, 1249, "Distillation feed heater")
Heater1 = Heater1.GetAsObject()

# Adding EnergyStream: EN_0a6b7722_be74_4d09_ba12_e3f419e67369
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2390, 1403, "ESTR-024")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_29f881f4_e28e_4879_9cdb_6f0eed407128
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2526, 1175, "vapor stream")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(311)  # Temperature in K
MaterialStream15.SetPressure(300000)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.000181743147982821)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9f290839_089b_482c_8fcb_425852ed2adb
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2532, 1352, "liquid stream")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(311)  # Temperature in K
MaterialStream16.SetPressure(300000)  # Pressure in Pa
MaterialStream16.SetMassFlow(3.213577119669)  # Mass Flow in kg/s

# Adding Vessel: SEP_87526961_74ff_4cf5_9464_fb3e70d264cc
Vessel2 = sim.AddObject(ObjectType.Vessel, 2458, 1266, "low pressure phase separator")
Vessel2 = Vessel2.GetAsObject()

# Adding NodeIn: MIST_9ef82b06_3636_49c6_9d63_a79dc5f5bc8a
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1474, 1256, "MIX-044")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_10a679a2_b5da_44af_a6f9_ced99ee94cf0
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2391, 1243, "Liquid stream")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(311.15)  # Temperature in K
MaterialStream17.SetPressure(2400000)  # Pressure in Pa
MaterialStream17.SetMassFlow(3.21375886271338)  # Mass Flow in kg/s

# Adding Vessel: SEP_437713ba_02a2_40fb_afcf_3c08c2331e88
Vessel3 = sim.AddObject(ObjectType.Vessel, 2302, 1265, "High pressure phase separator")
Vessel3 = Vessel3.GetAsObject()

# Adding EnergyStream: EN_733f70c4_e70b_4943_9813_8f0bc15c60be
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2239, 1277, "Heat duty of the cooler")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_b31a8940_bdc2_429b_939d_30dd511057c7
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2277, 1184, "Cooled products")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(311)  # Temperature in K
MaterialStream18.SetPressure(2550000)  # Pressure in Pa
MaterialStream18.SetMassFlow(5.81867842045827)  # Mass Flow in kg/s

# Adding Cooler: RESF_c8cc52f6_9ad4_4903_9b9d_7380e0208a94
Cooler1 = sim.AddObject(ObjectType.Cooler, 2223, 1221, "Product cooler")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_77672c97_5263_46e0_819a_a19c3f5e1fed
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1381, 1283, "toluene")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(298)  # Temperature in K
MaterialStream19.SetPressure(200000)  # Pressure in Pa
MaterialStream19.SetMassFlow(2.77)  # Mass Flow in kg/s

# Adding Pump: BB_f2b03728_7bc0_40d6_8147_f7d86a534d99
Pump1 = sim.AddObject(ObjectType.Pump, 1583, 1134, "PUMP-001")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_6dace042_b948_4eef_966b_982eddfa7e64
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1680, 1128, "high pressure toluene")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(352.764070900041)  # Temperature in K
MaterialStream20.SetPressure(2600000)  # Pressure in Pa
MaterialStream20.SetMassFlow(3.68884980438005)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ec4ec2ea_4dcb_4590_ac77_a6ecb2664c61
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 1552, 1182, "pump utility supply")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding NodeIn: MIST_462749d2_2b39_4e68_a735_835c6f65c37b
Mixer3 = sim.AddObject(ObjectType.NodeIn, 1795, 1215, "MIX-004")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_d7be8f2c_b16b_4def_afed_da6201b68f87
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1424, 1385, "Hydrogen")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(298)  # Temperature in K
MaterialStream21.SetPressure(2550000)  # Pressure in Pa
MaterialStream21.SetMassFlow(0.2277)  # Mass Flow in kg/s

# Adding Heater: AQ_63639d86_19dd_41ce_9a32_4ca045039591
Heater2 = sim.AddObject(ObjectType.Heater, 1902, 1180, "feed heater")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_26525f9f_2582_4327_8353_bc0e9b43578a
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1849, 1146, "feed to heater")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(328.59055838764)  # Temperature in K
MaterialStream22.SetPressure(2550000)  # Pressure in Pa
MaterialStream22.SetMassFlow(5.72324698098693)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3c381582_d0c3_45f4_920e_5eaba086b806
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 1883, 1234, "duty of feed heater")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_54a08657_596c_48f3_a236_ede54db36c9c
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 1955, 1147, "heated feed")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(866.59055838764)  # Temperature in K
MaterialStream23.SetPressure(2550000)  # Pressure in Pa
MaterialStream23.SetMassFlow(5.72324698098693)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_c5b99df3_d21c_49e2_a579_c4b09eaa94ff
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 2100, 1227, "Packed bed catalytic reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding EnergyStream: EN_d02575f4_2423_46ec_a9a3_8bc4df75162f
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 2091, 1365, "Heat removal for isothermal operation")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding MaterialStream: MAT_2a63c581_ab08_4698_b729_cc74d47d166e
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 2166, 1182, "Product stream ")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(855.738376171669)  # Temperature in K
MaterialStream24.SetPressure(2550000)  # Pressure in Pa
MaterialStream24.SetMassFlow(5.81867842045827)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b4f19f0a_1c56_4051_86e8_62a48528c553
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 2187, 1324, "MSTR-014")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(855.738376171669)  # Temperature in K
MaterialStream25.SetPressure(2550000)  # Pressure in Pa
MaterialStream25.SetMassFlow(0)  # Mass Flow in kg/s

# Adding NodeIn: MIST_c7ee5133_6f56_4d4c_86e3_e372f520f093
Mixer4 = sim.AddObject(ObjectType.NodeIn, 2005, 1195, "MIX-045")
Mixer4 = Mixer4.GetAsObject()

# Adding EnergyStream: EN_850d0a52_1f4d_4d3c_9da0_2888ae75f2ee
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 2304, 1397, "ESTR-045")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding MaterialStream: MAT_9e11357e_2218_4063_ba9c_526dbd3b70b7
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 2616, 1438, "bottom product to recycle (toluene)")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(480.305730133582)  # Temperature in K
MaterialStream26.SetPressure(1100000)  # Pressure in Pa
MaterialStream26.SetMassFlow(0.919212858346387)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3a3d7c5d_684a_4f13_9bc7_fb757242a0b9
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 1865, 1033, "MSTR-054")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(317.524203594938)  # Temperature in K
MaterialStream27.SetPressure(2550000)  # Pressure in Pa
MaterialStream27.SetMassFlow(0.0950795666751344)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_207d8c99_c60f_4b56_862d_9808f9b203ec
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 1714, 1093, "MSTR-055")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(317.524203594938)  # Temperature in K
MaterialStream28.SetPressure(2550000)  # Pressure in Pa
MaterialStream28.SetMassFlow(1.80651176682755)  # Mass Flow in kg/s

# Adding Cooler: RESF_3cadf22b_aec9_4ce0_9309_c71d87c0115d
Cooler2 = sim.AddObject(ObjectType.Cooler, 3118, 1329, "benzene cooler")
Cooler2 = Cooler2.GetAsObject()

# Adding MaterialStream: MAT_b0f4c404_efe0_4726_b3bc_7e0d762fcc7c
MaterialStream29 = sim.AddObject(ObjectType.MaterialStream, 3213, 1337, "cooled benzene")
MaterialStream29 = MaterialStream29.GetAsObject()
MaterialStream29.SetTemperature(311.15)  # Temperature in K
MaterialStream29.SetPressure(250000)  # Pressure in Pa
MaterialStream29.SetMassFlow(2.28588785824708)  # Mass Flow in kg/s

# Adding EnergyStream: EN_01d00aba_cee7_482f_a54f_e722e18ef128
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 3146, 1385, "ESTR-060")
EnergyStream12 = EnergyStream12.GetAsObject()

sim.ConnectObjects(EnergyStream9.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream9 to Heater2
sim.ConnectObjects(Mixer4.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer4 to MaterialStream7
sim.ConnectObjects(MaterialStream18.GraphicObject, Vessel3.GraphicObject, -1, -1)  # MaterialStream18 to Vessel3
sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Splitter2 to MaterialStream3
sim.ConnectObjects(MaterialStream22.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream22 to Heater2
sim.ConnectObjects(Recycle3.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle3 to MaterialStream5
sim.ConnectObjects(MaterialStream8.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream8 to Pump1
sim.ConnectObjects(EnergyStream6.GraphicObject, Vessel2.GraphicObject, -1, -1)  # EnergyStream6 to Vessel2
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Heater1 to MaterialStream14
sim.ConnectObjects(MaterialStream9.GraphicObject, Splitter2.GraphicObject, -1, -1)  # MaterialStream9 to Splitter2
sim.ConnectObjects(MaterialStream27.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream27 to Recycle2
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Vessel1 to MaterialStream11
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream28.GraphicObject, -1, -1)  # Splitter1 to MaterialStream28
sim.ConnectObjects(EnergyStream10.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream10 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream12 to Mixer1
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream15 to Mixer1
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Compressor1 to MaterialStream2
sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Splitter2 to MaterialStream4
sim.ConnectObjects(EnergyStream3.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # EnergyStream3 to ShortcutColumn1
sim.ConnectObjects(MaterialStream7.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream7 to Reactor_Conversion1
sim.ConnectObjects(Vessel3.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Vessel3 to MaterialStream17
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Pump1 to MaterialStream20
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream13
sim.ConnectObjects(MaterialStream23.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream23 to Mixer4
sim.ConnectObjects(EnergyStream2.GraphicObject, Vessel1.GraphicObject, -1, -1)  # EnergyStream2 to Vessel1
sim.ConnectObjects(MaterialStream2.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream2 to Splitter1
sim.ConnectObjects(MaterialStream21.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream21 to Mixer3
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream1 to Mixer4
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream27.GraphicObject, -1, -1)  # Splitter1 to MaterialStream27
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle2 to MaterialStream1
sim.ConnectObjects(MaterialStream19.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream19 to Mixer2
sim.ConnectObjects(MaterialStream6.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream6 to Mixer3
sim.ConnectObjects(Vessel3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Vessel3 to MaterialStream9
sim.ConnectObjects(ShortcutColumn1.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # ShortcutColumn1 to EnergyStream4
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Vessel2 to MaterialStream15
sim.ConnectObjects(EnergyStream5.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream5 to Heater1
sim.ConnectObjects(MaterialStream4.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream4 to Mixer1
sim.ConnectObjects(MaterialStream24.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream24 to Cooler1
sim.ConnectObjects(EnergyStream11.GraphicObject, Vessel3.GraphicObject, -1, -1)  # EnergyStream11 to Vessel3
sim.ConnectObjects(EnergyStream1.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream1 to Compressor1
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # Cooler1 to EnergyStream7
sim.ConnectObjects(MaterialStream28.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream28 to Recycle1
sim.ConnectObjects(MaterialStream13.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream13 to Vessel1
sim.ConnectObjects(MaterialStream20.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream20 to Mixer3
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Vessel1 to MaterialStream12
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Recycle1 to MaterialStream6
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Mixer1 to MaterialStream10
sim.ConnectObjects(EnergyStream8.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream8 to Pump1
sim.ConnectObjects(MaterialStream16.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream16 to Heater1
sim.ConnectObjects(MaterialStream11.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream11 to Cooler2
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream29.GraphicObject, -1, -1)  # Cooler2 to MaterialStream29
sim.ConnectObjects(MaterialStream17.GraphicObject, Vessel2.GraphicObject, -1, -1)  # MaterialStream17 to Vessel2
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Vessel2 to MaterialStream16
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Mixer2 to MaterialStream8
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Heater2 to MaterialStream23
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream26
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Cooler1 to MaterialStream18
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream5 to Mixer2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream25
sim.ConnectObjects(MaterialStream3.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream3 to Compressor1
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream12.GraphicObject, -1, -1)  # Cooler2 to EnergyStream12
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Mixer3 to MaterialStream22
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream24
sim.ConnectObjects(MaterialStream26.GraphicObject, Recycle3.GraphicObject, -1, -1)  # MaterialStream26 to Recycle3
sim.ConnectObjects(MaterialStream14.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # MaterialStream14 to ShortcutColumn1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_32.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_32.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

