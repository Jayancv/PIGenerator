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
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
carbon_monoxide = sim.AvailableCompounds["Carbon monoxide"]
sim.SelectedCompounds.Add(carbon_monoxide.Name, carbon_monoxide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)

# Adding Simulation Objects
# Adding EnergyStream: EN_ebda2888_dcb8_44b2_b2ef_df5baf435f8f
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1707, 929, "ESTR-057")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding OT_Recycle: REC_dfba94c9_2380_4480_be89_209d2db8f765
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1644, 1092, "REC-055")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_0ae4b8dc_fb27_4101_8023_2ac8e29e9ea1
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1670, 1020, "MSTR-056")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(315.228336484004)  # Temperature in K
MaterialStream1.SetPressure(100000)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.00701497668008111)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_12924ae8_da5a_441a_991e_a1f6249a950e
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1733, 1233, "METHANOL")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(314.55702637861)  # Temperature in K
MaterialStream2.SetPressure(100000)  # Pressure in Pa
MaterialStream2.SetMassFlow(29.5565396684064)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_856cf597_fe49_45b0_8b1b_a690a5498cfc
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1597, 1378, "WATER")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(383.410265961542)  # Temperature in K
MaterialStream3.SetPressure(140000)  # Pressure in Pa
MaterialStream3.SetMassFlow(3.56233127656083)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_a50ae530_5b89_43f2_9f8e_d1635cc4442d
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1596, 1164, "SIDESTREAM")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(315.228336484004)  # Temperature in K
MaterialStream4.SetPressure(100000)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.00701497668008111)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_45b2fe15_71a4_4c9b_82fb_6b1f33759174
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 1519, 1247, "METHANOL COLUMN")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_5f624f4f_a17b_425a_b76c_713c984e9ea2
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1876, 968, "MSTR-050")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(318.705958823594)  # Temperature in K
MaterialStream5.SetPressure(11000000)  # Pressure in Pa
MaterialStream5.SetMassFlow(125.837422714316)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_9099e5c7_e590_41f8_9fd7_70766193c433
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1799, 983, "REC-049")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_5620a2da_9f6a_4fbd_b43c_9ffeb3adb5a1
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1781, 1128, "MSTR-048")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(318.705958823594)  # Temperature in K
MaterialStream6.SetPressure(11000000)  # Pressure in Pa
MaterialStream6.SetMassFlow(125.837422714316)  # Mass Flow in kg/s

# Adding NodeIn: MIST_27512d2f_5bc5_4f7b_97f7_c39a53a21bd4
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1865, 1140, "MIX-047")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_85ab521f_a808_41d9_8561_606def2240c6
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2199, 1123, "ESTR-046")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_6c61e63f_2159_48a6_8c2c_4c61ff13b2f8
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1979, 1135, "MSTR-045")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(314.602376616891)  # Temperature in K
MaterialStream7.SetPressure(11000000)  # Pressure in Pa
MaterialStream7.SetMassFlow(123.687279963362)  # Mass Flow in kg/s

# Adding Compressor: COMP_4911b13c_db32_43d2_a367_90f886e76bc0
Compressor1 = sim.AddObject(ObjectType.Compressor, 2156, 1093, "COMP-044")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_142a76dd_6de7_493a_aca4_6cacfcbe908d
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2278, 1098, "MSTR-043")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(311.15)  # Temperature in K
MaterialStream8.SetPressure(10650000)  # Pressure in Pa
MaterialStream8.SetMassFlow(123.687279963362)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_442642ad_58e1_4420_8dfb_6148d90a7916
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2629, 1089, "VENT")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(311.15)  # Temperature in K
MaterialStream9.SetPressure(10650000)  # Pressure in Pa
MaterialStream9.SetMassFlow(2.78116265349612)  # Mass Flow in kg/s

# Adding NodeOut: DIV_4bcf7333_6ebd_4fb4_8abb_797b7fb9be99
Splitter1 = sim.AddObject(ObjectType.NodeOut, 2477, 1102, "SPLT-041")
Splitter1 = Splitter1.GetAsObject()

# Adding EnergyStream: EN_501d311a_41f5_4488_935e_8b7d07bd70a9
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2077, 1240, "ESTR-040")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_7da56799_0c84_43f0_b8ce_b03cebd30d6f
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1968, 1188, "MSTR-039")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(765.967139310292)  # Temperature in K
MaterialStream10.SetPressure(11000000)  # Pressure in Pa
MaterialStream10.SetMassFlow(2.15014275095375)  # Mass Flow in kg/s

# Adding Compressor: COMP_d6bfa12d_4db6_4d79_a962_49063f664b44
Compressor2 = sim.AddObject(ObjectType.Compressor, 2035, 1210, "COMP-038")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_ca1a62f2_858b_4293_932f_150f68e918a9
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1893, 1519, "MSTR-037")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(309.741599189202)  # Temperature in K
MaterialStream11.SetPressure(200000)  # Pressure in Pa
MaterialStream11.SetMassFlow(33.1258859430588)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d5a7159a_a38f_4a0b_902a_69e68a557f32
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2109, 1221, "MSTR-036")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(309.741599189202)  # Temperature in K
MaterialStream12.SetPressure(200000)  # Pressure in Pa
MaterialStream12.SetMassFlow(2.15014275095375)  # Mass Flow in kg/s

# Adding Vessel: SEP_af302566_f51f_4a47_a679_77ca6246ef14
Vessel1 = sim.AddObject(ObjectType.Vessel, 2160, 1275, "SEP-035")
Vessel1 = Vessel1.GetAsObject()

# Adding MaterialStream: MAT_af7adb61_e216_420e_80b4_ca4647b1c08c
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1324, 664, "SYN GAS")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(323.15)  # Temperature in K
MaterialStream13.SetPressure(5120000)  # Pressure in Pa
MaterialStream13.SetMassFlow(35.9008379600738)  # Mass Flow in kg/s

# Adding Compressor: COMP_399ee9c2_8619_46eb_9722_b7eb5cb06ade
Compressor3 = sim.AddObject(ObjectType.Compressor, 1436, 662, "COMP-001")
Compressor3 = Compressor3.GetAsObject()

# Adding MaterialStream: MAT_fbc0c5c1_5c08_49ff_aace_ad3d1739e0cb
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1524, 671, "MSTR-002")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(370.850178148603)  # Temperature in K
MaterialStream14.SetPressure(7500000)  # Pressure in Pa
MaterialStream14.SetMassFlow(35.9008379600738)  # Mass Flow in kg/s

# Adding EnergyStream: EN_639bc8c7_45d2_4484_8a7f_e06c235e130d
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1479, 717, "ESTR-003")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding Heater: AQ_3378fd8f_f634_476b_903e_b93a61d734d1
Heater1 = sim.AddObject(ObjectType.Heater, 1595, 662, "HEAT-004")
Heater1 = Heater1.GetAsObject()

# Adding MaterialStream: MAT_4fa93cd2_305b_43ac_8379_199dfbed7516
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1685, 672, "MSTR-005")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(311.15)  # Temperature in K
MaterialStream15.SetPressure(7500000)  # Pressure in Pa
MaterialStream15.SetMassFlow(35.9008379600738)  # Mass Flow in kg/s

# Adding EnergyStream: EN_a2400a74_684c_4cf1_8497_9f8f5cf7f7cf
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1637, 717, "ESTR-006")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding Compressor: COMP_c6e62431_abc4_4a92_8f69_fc5e38bf37de
Compressor4 = sim.AddObject(ObjectType.Compressor, 1771, 671, "COMP-007")
Compressor4 = Compressor4.GetAsObject()

# Adding MaterialStream: MAT_b2a3aa26_a8b9_451e_9d5a_3741b7289c2f
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1898, 706, "MSTR-008")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(357.344563100796)  # Temperature in K
MaterialStream16.SetPressure(11000000)  # Pressure in Pa
MaterialStream16.SetMassFlow(35.9008379600738)  # Mass Flow in kg/s

# Adding EnergyStream: EN_bc5035a6_9080_497e_9333_712c3b599b3b
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1813, 726, "ESTR-009")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_44455e67_659b_41df_9d12_65b4d2954f86
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1729, 817, "MSTR-056")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(810.358483868066)  # Temperature in K
MaterialStream17.SetPressure(11000000)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.007014974928673)  # Mass Flow in kg/s

# Adding NodeIn: MIST_796e756c_1b53_490c_8fa9_47a6b5ae550b
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1991, 713, "MIX-012")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_611ac215_bdf6_4ba5_845a_0c211a15ee2e
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2072, 722, "MSTR-013")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(326.659084499734)  # Temperature in K
MaterialStream18.SetPressure(11000000)  # Pressure in Pa
MaterialStream18.SetMassFlow(161.745369538667)  # Mass Flow in kg/s

# Adding Compressor: COMP_9781c3f5_cae2_4d9b_93c1_16384839944a
Compressor5 = sim.AddObject(ObjectType.Compressor, 1664, 874, "COMP-055")
Compressor5 = Compressor5.GetAsObject()

# Adding HeatExchanger: HE_f9509009_feba_4fc4_ac31_a2400550afe7
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 2148, 726, "HE-015")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_569a8fe8_a8e0_498d_9069_9177aba9fa88
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2246, 736, "MSTR-016")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(418.15)  # Temperature in K
MaterialStream19.SetPressure(10900000)  # Pressure in Pa
MaterialStream19.SetMassFlow(161.745369538667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_da09fca1_da6f_4af5_9602_df9ceb4ffa41
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2178, 879, "MSTR-017")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(448.384995935098)  # Temperature in K
MaterialStream20.SetPressure(10700000)  # Pressure in Pa
MaterialStream20.SetMassFlow(161.74448098319)  # Mass Flow in kg/s

# Adding Heater: AQ_4ec152b9_d986_4377_b0e8_8b5e9144154e
Heater2 = sim.AddObject(ObjectType.Heater, 2335, 738, "HEAT-018")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_eb58b87a_4639_4f10_9f7c_6b7d14281c29
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 2427, 749, "MSTR-019")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(423.15)  # Temperature in K
MaterialStream21.SetPressure(10850000)  # Pressure in Pa
MaterialStream21.SetMassFlow(161.745369538667)  # Mass Flow in kg/s

# Adding EnergyStream: EN_ccaf488a_9efb_472f_9840_720ca677151b
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2377, 793, "ESTR-020")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding RCT_Conversion: RC_214a7045_897b_4062_aab4_7a36d7fab6a1
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 2481, 733, "REACTOR")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_248b71a7_67fd_4d50_8f28_821d1855c42b
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 2569, 734, "MSTR-022")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(540.15)  # Temperature in K
MaterialStream22.SetPressure(10750000)  # Pressure in Pa
MaterialStream22.SetMassFlow(161.745369538667)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f8f8c849_f92d_490f_83e1_af0e2b6f31c1
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2555, 774, "MSTR-023")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(540.15)  # Temperature in K
MaterialStream23.SetPressure(10750000)  # Pressure in Pa
MaterialStream23.SetMassFlow(0)  # Mass Flow in kg/s

# Adding EnergyStream: EN_e976b72a_e85b_4a9e_8947_f7f33cd3fbe5
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2457, 798, "ESTR-024")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding OT_Recycle: REC_7c4bfed6_7d2f_4b2f_87e1_e9e4c549d1da
Recycle3 = sim.AddObject(ObjectType.OT_Recycle, 2448, 584, "REC-025")
Recycle3 = Recycle3.GetAsObject()

# Adding MaterialStream: MAT_ec38a038_1de2_4117_bc27_4ba4d8a95192
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 2293, 553, "MSTR-026")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(540.15)  # Temperature in K
MaterialStream24.SetPressure(10750000)  # Pressure in Pa
MaterialStream24.SetMassFlow(161.745369538667)  # Mass Flow in kg/s

# Adding Heater: AQ_4960ce3c_17d2_4d7f_a01b_06c032a0f78c
Heater3 = sim.AddObject(ObjectType.Heater, 2259, 873, "HEAT-027")
Heater3 = Heater3.GetAsObject()

# Adding MaterialStream: MAT_40bed6b5_d24e_48ee_b89f_b63197344825
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 2426, 895, "MSTR-028")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(311.15)  # Temperature in K
MaterialStream25.SetPressure(10650000)  # Pressure in Pa
MaterialStream25.SetMassFlow(161.74448098319)  # Mass Flow in kg/s

# Adding EnergyStream: EN_0b695a5f_5c62_4425_b8e3_934200655a27
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2301, 928, "ESTR-029")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding Vessel: SEP_0846bfb4_1edf_4155_ad68_7036bfdd81a4
Vessel2 = sim.AddObject(ObjectType.Vessel, 2427, 1192, "HP SEPARATOR")
Vessel2 = Vessel2.GetAsObject()

# Adding MaterialStream: MAT_5b91e723_7abe_479a_872d_20e71ff7318d
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 2476, 1158, "MSTR-031")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(311.15)  # Temperature in K
MaterialStream26.SetPressure(10650000)  # Pressure in Pa
MaterialStream26.SetMassFlow(126.468442616858)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ef494a0a_89bd_4621_b859_5b76bc1f971c
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 2422, 1297, "MSTR-032")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(311.15)  # Temperature in K
MaterialStream27.SetPressure(10650000)  # Pressure in Pa
MaterialStream27.SetMassFlow(35.276028756761)  # Mass Flow in kg/s

# Adding Valve: VALV_37f3e0a2_a5c6_4c2f_aa7d_8ad646099cfe
Valve1 = sim.AddObject(ObjectType.Valve, 2340, 1308, "VALV-033")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_5dabe6be_7908_4517_a2a0_3d676c7e2c7d
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 2245, 1308, "MSTR-034")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(309.741599189202)  # Temperature in K
MaterialStream28.SetPressure(200000)  # Pressure in Pa
MaterialStream28.SetMassFlow(35.276028756761)  # Mass Flow in kg/s

sim.ConnectObjects(Heater2.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Heater2 to MaterialStream21
sim.ConnectObjects(EnergyStream9.GraphicObject, Heater3.GraphicObject, -1, -1)  # EnergyStream9 to Heater3
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream3
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Vessel1 to MaterialStream11
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream28.GraphicObject, -1, -1)  # Valve1 to MaterialStream28
sim.ConnectObjects(MaterialStream19.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream19 to Heater2
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream5 to Mixer2
sim.ConnectObjects(MaterialStream14.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream14 to Heater1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Splitter1 to MaterialStream9
sim.ConnectObjects(Compressor3.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Compressor3 to MaterialStream14
sim.ConnectObjects(MaterialStream27.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream27 to Valve1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream20
sim.ConnectObjects(MaterialStream8.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream8 to Compressor1
sim.ConnectObjects(EnergyStream2.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream2 to Compressor1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Splitter1 to MaterialStream8
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Compressor1 to MaterialStream7
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Recycle2 to MaterialStream5
sim.ConnectObjects(MaterialStream13.GraphicObject, Compressor3.GraphicObject, -1, -1)  # MaterialStream13 to Compressor3
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Compressor2 to MaterialStream10
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Mixer1 to MaterialStream6
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream23
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream27.GraphicObject, -1, -1)  # Vessel2 to MaterialStream27
sim.ConnectObjects(MaterialStream16.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream16 to Mixer2
sim.ConnectObjects(MaterialStream15.GraphicObject, Compressor4.GraphicObject, -1, -1)  # MaterialStream15 to Compressor4
sim.ConnectObjects(MaterialStream7.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream7 to Mixer1
sim.ConnectObjects(MaterialStream12.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream12 to Compressor2
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream6.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream6 to Recycle2
sim.ConnectObjects(MaterialStream18.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream18 to HeatExchanger1
sim.ConnectObjects(MaterialStream11.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream11 to CapeOpenUO1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream19
sim.ConnectObjects(EnergyStream1.GraphicObject, Compressor5.GraphicObject, -1, -1)  # EnergyStream1 to Compressor5
sim.ConnectObjects(Heater3.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Heater3 to MaterialStream25
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream4
sim.ConnectObjects(MaterialStream21.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream21 to Reactor_Conversion1
sim.ConnectObjects(EnergyStream4.GraphicObject, Compressor3.GraphicObject, -1, -1)  # EnergyStream4 to Compressor3
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Mixer2 to MaterialStream18
sim.ConnectObjects(Recycle3.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # Recycle3 to MaterialStream24
sim.ConnectObjects(EnergyStream5.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream5 to Heater1
sim.ConnectObjects(MaterialStream26.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream26 to Splitter1
sim.ConnectObjects(MaterialStream1.GraphicObject, Compressor5.GraphicObject, -1, -1)  # MaterialStream1 to Compressor5
sim.ConnectObjects(MaterialStream25.GraphicObject, Vessel2.GraphicObject, -1, -1)  # MaterialStream25 to Vessel2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream22
sim.ConnectObjects(Compressor5.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Compressor5 to MaterialStream17
sim.ConnectObjects(EnergyStream6.GraphicObject, Compressor4.GraphicObject, -1, -1)  # EnergyStream6 to Compressor4
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream10 to Mixer1
sim.ConnectObjects(Compressor4.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Compressor4 to MaterialStream16
sim.ConnectObjects(EnergyStream7.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream7 to Heater2
# sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream22.GraphicObject, Recycle3.GraphicObject, -1, -1)  # MaterialStream22 to Recycle3
sim.ConnectObjects(MaterialStream17.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream17 to Mixer2
sim.ConnectObjects(MaterialStream28.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream28 to Vessel1
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(EnergyStream8.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream8 to Reactor_Conversion1
sim.ConnectObjects(EnergyStream3.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream3 to Compressor2
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # Vessel2 to MaterialStream26
sim.ConnectObjects(MaterialStream24.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream24 to HeatExchanger1
sim.ConnectObjects(MaterialStream20.GraphicObject, Heater3.GraphicObject, -1, -1)  # MaterialStream20 to Heater3
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Vessel1 to MaterialStream12
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Heater1 to MaterialStream15
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_45.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_45.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

