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
isopentane = sim.AvailableCompounds["Isopentane"]
sim.SelectedCompounds.Add(isopentane.Name, isopentane)
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
n_butane = sim.AvailableCompounds["N-butane"]
sim.SelectedCompounds.Add(n_butane.Name, n_butane)
n_pentane = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(n_pentane.Name, n_pentane)
isobutane = sim.AvailableCompounds["Isobutane"]
sim.SelectedCompounds.Add(isobutane.Name, isobutane)
n_hexane = sim.AvailableCompounds["N-hexane"]
sim.SelectedCompounds.Add(n_hexane.Name, n_hexane)
n_heptane = sim.AvailableCompounds["N-heptane"]
sim.SelectedCompounds.Add(n_heptane.Name, n_heptane)
ethane = sim.AvailableCompounds["Ethane"]
sim.SelectedCompounds.Add(ethane.Name, ethane)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_60d0a6f8_2ca9_4529_b810_217fb8d01195
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 4949, 1673, "n-Butane")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(339.599808083843)  # Temperature in K
MaterialStream1.SetPressure(749805)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.699365882130734)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dbf9e203_d764_4409_a378_977d2cfaddbb
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 4949, 1356, "i-Butane")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(322.391280335766)  # Temperature in K
MaterialStream2.SetPressure(668745)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.590858453225031)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7c0ba09a_7960_4d47_9bf7_08282c2e6998
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 4703, 1492, "S-33")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(331.773211987209)  # Temperature in K
MaterialStream3.SetPressure(719407.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(1.29022433535635)  # Mass Flow in kg/s

# Adding Valve: VALV_f8b0fa17_f3c1_4045_ae40_c5dc9da1a5ab
Valve1 = sim.AddObject(ObjectType.Valve, 4612, 1488, "VALV-05")
Valve1 = Valve1.GetAsObject()

# Adding CapeOpenUO: COUO_c6f4457f_4d2e_4e44_b38a_d4cb34406ccd
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 4747, 1401, "De-isobutanizer")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_3021e796_daa7_4d6f_b0d6_e1635ecc31f2
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 4530, 1890, "Stabilized Condensate")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(391.494413844052)  # Temperature in K
MaterialStream4.SetPressure(749805)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.36961865446786)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4fcac360_e418_490c_915c_271e4848f87c
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 4530, 1488, "S-32")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(331.773211987209)  # Temperature in K
MaterialStream5.SetPressure(719407.5)  # Pressure in Pa
MaterialStream5.SetMassFlow(1.29022433535635)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_1d906e4a_75aa_45a0_a10d_62e56b3f4a1f
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 4384, 1627, "De-butanizer")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_14f67966_0872_4a5e_885c_391bfb2d2cda
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 4316, 1720, "S-30")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(359.708204553335)  # Temperature in K
MaterialStream6.SetPressure(739672.5)  # Pressure in Pa
MaterialStream6.SetMassFlow(2.659842989889)  # Mass Flow in kg/s

# Adding Valve: VALV_9e1aae24_629a_480e_8ea6_41ed8f33974d
Valve2 = sim.AddObject(ObjectType.Valve, 4237, 1719, "VALV-04")
Valve2 = Valve2.GetAsObject()

# Adding MaterialStream: MAT_95b85ca2_c557_4531_8acc_fb06c6eec195
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 3842, 1619, "S-28")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(354.397559832966)  # Temperature in K
MaterialStream7.SetPressure(1763055)  # Pressure in Pa
MaterialStream7.SetMassFlow(4.44576711681945)  # Mass Flow in kg/s

# Adding Valve: VALV_6387560e_00a6_46ed_a892_ba25f3bc1e29
Valve3 = sim.AddObject(ObjectType.Valve, 3749, 1617, "VALV-03")
Valve3 = Valve3.GetAsObject()

# Adding MaterialStream: MAT_2abfd4a5_ed96_4ffe_b88c_c21afd1f0b71
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 4165, 1720, "S-29")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(398.256329093273)  # Temperature in K
MaterialStream8.SetPressure(1773188)  # Pressure in Pa
MaterialStream8.SetMassFlow(2.659842989889)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_57eea434_fbde_4604_823a_555b1ddf3dab
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 4165, 1344, "Propane")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(322.892931277038)  # Temperature in K
MaterialStream9.SetPressure(1722525)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.7859241269269)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_81525e32_bbfd_48c3_80f8_6692ad133360
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 3976, 1528, "De-propanizer")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_4fc2daf1_a39d_4422_8d0b_2b4b18df6bf5
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 3679, 1616, "S-27")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(363.506798295051)  # Temperature in K
MaterialStream10.SetPressure(2158223)  # Pressure in Pa
MaterialStream10.SetMassFlow(4.44576711681945)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ab0eb6ee_c059_4c66_a199_9e319f6dc9ec
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 3682, 1386, "Ethane")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(269.103840811614)  # Temperature in K
MaterialStream11.SetPressure(2127825)  # Pressure in Pa
MaterialStream11.SetMassFlow(2.3791448680833)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_9b4b9e11_dfed_4209_8fc5_1d1f0e1773e5
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 3496, 1431, "De-ethanizer")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()

# Adding OT_Recycle: REC_8a2edbc9_6352_4e5e_be6d_177e81f72987
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 3179, 1288, "REC-02")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_6af93f6f_6fe5_43bf_bb0f_ce13490593f0
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 3112, 1345, "S-20")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(176.139266804334)  # Temperature in K
MaterialStream12.SetPressure(2700830)  # Pressure in Pa
MaterialStream12.SetMassFlow(8.78741127556436)  # Mass Flow in kg/s

# Adding Valve: VALV_3be7ef33_e3c9_411a_809f_3438f04cc82a
Valve4 = sim.AddObject(ObjectType.Valve, 3047, 1340, "VALV-02")
Valve4 = Valve4.GetAsObject()

# Adding MaterialStream: MAT_28d9bcd4_c945_45f3_9fb8_ad79faa77380
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 3424, 1522, "S-25")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(311.29175318429)  # Temperature in K
MaterialStream13.SetPressure(2543258)  # Pressure in Pa
MaterialStream13.SetMassFlow(6.82491198490335)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d5eb5145_5ceb_4aef_819d_4f31dd7cf05d
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 3338, 1382, "S-24")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(179.049639255892)  # Temperature in K
MaterialStream14.SetPressure(2533125)  # Pressure in Pa
MaterialStream14.SetMassFlow(21.4750238122392)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_0877ee74_b0e8_4ab8_ba33_cea3d19f47f6
CapeOpenUO5 = sim.AddObject(ObjectType.CapeOpenUO, 3227, 1432, "De-methanizer")
CapeOpenUO5 = CapeOpenUO5.GetAsObject()

# Adding EnergyStream: EN_469b8544_091d_48d6_9851_ccdf8ab11f05
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2966, 1567, "E-08")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_fbdf8154_d176_43c8_90b4_f0f80e551c34
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 3094, 1553, "S-22")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(212.750232586933)  # Temperature in K
MaterialStream15.SetPressure(2543257.5)  # Pressure in Pa
MaterialStream15.SetMassFlow(1.53368438725755)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_08941ee6_7a76_45ff_bc6d_2b6d032f661c
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 3098, 1487, "S-21")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(212.750232586933)  # Temperature in K
MaterialStream16.SetPressure(2543257.5)  # Pressure in Pa
MaterialStream16.SetMassFlow(14.7932138207573)  # Mass Flow in kg/s

# Adding Vessel: SEP_81d20285_9cd0_4024_87ec_d90a343d2b4c
Vessel1 = sim.AddObject(ObjectType.Vessel, 3001, 1440, "FLASH-02")
Vessel1 = Vessel1.GetAsObject()

# Adding EnergyStream: EN_820066df_f15b_4a0d_be16_8f2cee60b620
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2922, 1489, "E-07")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_9a7cb600_0f7d_41f9_8f27_21f55a0a85b5
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2938, 1440, "S-19")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(212.750232586933)  # Temperature in K
MaterialStream17.SetPressure(2543257.5)  # Pressure in Pa
MaterialStream17.SetMassFlow(16.3268988419076)  # Mass Flow in kg/s

# Adding Expander: TURB_212133a7_c969_458e_83c4_267b99c5735d
Expander1 = sim.AddObject(ObjectType.Expander, 2847, 1436, "EXP-01")
Expander1 = Expander1.GetAsObject()

# Adding OT_Recycle: REC_2440a3a0_0fa9_4a9a_9e2f_479fe5a90318
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 2608, 1264, "REC-01")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_c973baaf_116c_4f19_b544_2c7983820695
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2896, 1385, "S-16")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(243.98632)  # Temperature in K
MaterialStream18.SetPressure(2513125)  # Pressure in Pa
MaterialStream18.SetMassFlow(21.4750693988583)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_458d8f9b_1afa_448d_8963_352a569f00ba
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2960, 1290, "S-18")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(179.05599)  # Temperature in K
MaterialStream19.SetPressure(2533125)  # Pressure in Pa
MaterialStream19.SetMassFlow(21.4750693988583)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_520e218d_4570_487f_a8e3_63c3270a7da3
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2970, 1337, "S-17")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(181.605922848092)  # Temperature in K
MaterialStream20.SetPressure(6100830)  # Pressure in Pa
MaterialStream20.SetMassFlow(8.78741127556436)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_89e2d2e5_b88a_48cf_8e85_bee37c211dc5
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 2813, 1311, "HEX-02")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_75aeb8ed_95c5_4f85_8427_7d4853298115
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 3113, 1613, "S-23")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(237.578685745206)  # Temperature in K
MaterialStream21.SetPressure(2641330)  # Pressure in Pa
MaterialStream21.SetMassFlow(3.18562631354853)  # Mass Flow in kg/s

# Adding Valve: VALV_6c5f1b29_5288_44c2_917c_14dff1e45634
Valve5 = sim.AddObject(ObjectType.Valve, 2741, 1616, "VALV-01")
Valve5 = Valve5.GetAsObject()

# Adding MaterialStream: MAT_4a7f5f96_3f28_4056_bd22_98e0afe57d66
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 2799, 1438, "S-14")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(251.4)  # Temperature in K
MaterialStream22.SetPressure(6120830)  # Pressure in Pa
MaterialStream22.SetMassFlow(16.3268988419076)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6f66a1b4_7957_4b58_809c_3a5cfdaa989a
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2755, 1316, "S-15")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(251.4)  # Temperature in K
MaterialStream23.SetPressure(6120830)  # Pressure in Pa
MaterialStream23.SetMassFlow(8.78741127556436)  # Mass Flow in kg/s

# Adding NodeOut: DIV_ee235978_0645_4279_82e4_b59380a29b1a
Splitter1 = sim.AddObject(ObjectType.NodeOut, 2668, 1325, "SPLIT-02")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_379c2cd2_06f0_46af_8419_39d906fab8af
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 2619, 1617, "S-13")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(251.399841974423)  # Temperature in K
MaterialStream24.SetPressure(6120830)  # Pressure in Pa
MaterialStream24.SetMassFlow(3.18562631354853)  # Mass Flow in kg/s

# Adding EnergyStream: EN_8cc8484c_a157_4072_b42a_03388ebe1a7a
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2469, 1442, "E-05")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_ddfb79db_0a57_4571_a5db_7ab5cd4829f4
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 2609, 1327, "S-12")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(251.4)  # Temperature in K
MaterialStream25.SetPressure(6120830)  # Pressure in Pa
MaterialStream25.SetMassFlow(25.1143101174719)  # Mass Flow in kg/s

# Adding Vessel: SEP_ee0114f8_0ef6_4237_9f8f_c4c737e74e9a
Vessel2 = sim.AddObject(ObjectType.Vessel, 2530, 1327, "FLASH-01")
Vessel2 = Vessel2.GetAsObject()

# Adding EnergyStream: EN_dd610bfd_e723_4eab_99fe_b1a221d16c54
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2438, 1381, "E-04")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_2159d83b_0180_434f_9d33_48cce0676a7c
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 2477, 1328, "S-11")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(251.4)  # Temperature in K
MaterialStream26.SetPressure(6120830)  # Pressure in Pa
MaterialStream26.SetMassFlow(28.299937634934)  # Mass Flow in kg/s

# Adding Compressor: COMP_6312d329_cee3_4e7b_bd23_f142e83b1e73
Compressor1 = sim.AddObject(ObjectType.Compressor, 1779, 1596, "COM-01")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_a036f9e6_f585_4a2e_b5f1_e555fce72a12
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 1723, 1227, "NG-Feed")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(310)  # Temperature in K
MaterialStream27.SetPressure(5978180)  # Pressure in Pa
MaterialStream27.SetMassFlow(28.299937634934)  # Mass Flow in kg/s

# Adding Cooler: RESF_8992735f_1665_42a4_b257_614dbc9d8deb
Cooler1 = sim.AddObject(ObjectType.Cooler, 2398, 1325, "COOL-03")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_6948cf5f_2de2_4bf0_8836_5f87acea05c8
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 1833, 1599, "S-02")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(312.734133497719)  # Temperature in K
MaterialStream28.SetPressure(6180830)  # Pressure in Pa
MaterialStream28.SetMassFlow(28.299937634934)  # Mass Flow in kg/s

# Adding EnergyStream: EN_f50babbf_9938_487b_adbb_53ce8cdc8580
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1745, 1685, "E-1")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding NodeOut: DIV_195ee640_883b_4fa5_859a_7b5ee0d4a401
Splitter2 = sim.AddObject(ObjectType.NodeOut, 1877, 1599, "SPLIT-01")
Splitter2 = Splitter2.GetAsObject()

# Adding MaterialStream: MAT_cae3dbbd_f07b_43ef_b49c_bd9b63bfd1d5
MaterialStream29 = sim.AddObject(ObjectType.MaterialStream, 1926, 1320, "S-03")
MaterialStream29 = MaterialStream29.GetAsObject()
MaterialStream29.SetTemperature(312.734133497719)  # Temperature in K
MaterialStream29.SetPressure(6180830)  # Pressure in Pa
MaterialStream29.SetMassFlow(0.30614808764302)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_e7cbcb50_9d3b_4af0_be31_a78c6dbea5d5
MaterialStream30 = sim.AddObject(ObjectType.MaterialStream, 1969, 1599, "S-04")
MaterialStream30 = MaterialStream30.GetAsObject()
MaterialStream30.SetTemperature(312.734133497719)  # Temperature in K
MaterialStream30.SetPressure(6180830)  # Pressure in Pa
MaterialStream30.SetMassFlow(27.993789547291)  # Mass Flow in kg/s

# Adding Cooler: RESF_65e71c57_389c_4e14_b6f3_92aa8e45e961
Cooler2 = sim.AddObject(ObjectType.Cooler, 2025, 1563, "COOL-01")
Cooler2 = Cooler2.GetAsObject()

# Adding MaterialStream: MAT_bdccce41_0263_4e52_9ce5_679f381ff93c
MaterialStream31 = sim.AddObject(ObjectType.MaterialStream, 2029, 1500, "S-05")
MaterialStream31 = MaterialStream31.GetAsObject()
MaterialStream31.SetTemperature(305.279628825585)  # Temperature in K
MaterialStream31.SetPressure(6160830)  # Pressure in Pa
MaterialStream31.SetMassFlow(27.993789547291)  # Mass Flow in kg/s

# Adding EnergyStream: EN_652f669a_a653_422e_8f81_ff629e0f0711
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2270, 1565, "E-02")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding Cooler: RESF_4a3a6499_3aee_4cfc_aa93_896998b87094
Cooler3 = sim.AddObject(ObjectType.Cooler, 2030, 1444, "COOL-02")
Cooler3 = Cooler3.GetAsObject()

# Adding MaterialStream: MAT_52b4be3a_62ef_48c6_be70_a47882a54518
MaterialStream32 = sim.AddObject(ObjectType.MaterialStream, 2033, 1396, "S-06")
MaterialStream32 = MaterialStream32.GetAsObject()
MaterialStream32.SetTemperature(289.691547175373)  # Temperature in K
MaterialStream32.SetPressure(6140830)  # Pressure in Pa
MaterialStream32.SetMassFlow(27.993789547291)  # Mass Flow in kg/s

# Adding EnergyStream: EN_e7722c9d_cb42_4e8e_b47a_ab6f1b057c3f
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2273, 1446, "E-03")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding HeatExchanger: HE_efd39bd9_0495_468e_88f7_c9af13cef1f7
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 2183, 1323, "HEX-01")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding NodeIn: MIST_29b91695_f160_4701_bc28_4dbc723cf7b9
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2059, 1330, "MIX-01")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_37e978c5_12a5_4566_8d94_37ddce6b822f
MaterialStream33 = sim.AddObject(ObjectType.MaterialStream, 2120, 1328, "S-07")
MaterialStream33 = MaterialStream33.GetAsObject()
MaterialStream33.SetTemperature(289.932878632978)  # Temperature in K
MaterialStream33.SetPressure(6140830)  # Pressure in Pa
MaterialStream33.SetMassFlow(28.299937634934)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f4e8bc94_c85e_40f4_8030_41062a509b36
MaterialStream34 = sim.AddObject(ObjectType.MaterialStream, 2331, 1328, "S-08")
MaterialStream34 = MaterialStream34.GetAsObject()
MaterialStream34.SetTemperature(266.658370607712)  # Temperature in K
MaterialStream34.SetPressure(6120830)  # Pressure in Pa
MaterialStream34.SetMassFlow(28.299937634934)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3af195df_9408_4cba_a696_e4539e33b9a8
MaterialStream35 = sim.AddObject(ObjectType.MaterialStream, 2374, 1264, "S-09")
MaterialStream35 = MaterialStream35.GetAsObject()
MaterialStream35.SetTemperature(243.98632)  # Temperature in K
MaterialStream35.SetPressure(2513124.964875)  # Pressure in Pa
MaterialStream35.SetMassFlow(21.4750693988583)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_3f91294c_96b8_438d_8a9b_adc16c0d3b83
MaterialStream36 = sim.AddObject(ObjectType.MaterialStream, 2295, 1185, "S-10")
MaterialStream36 = MaterialStream36.GetAsObject()
MaterialStream36.SetTemperature(287.4)  # Temperature in K
MaterialStream36.SetPressure(2493124.964875)  # Pressure in Pa
MaterialStream36.SetMassFlow(21.4750693988583)  # Mass Flow in kg/s

# Adding Compressor: COMP_3ed43206_973a_4fa4_9b69_f236290b80d9
Compressor2 = sim.AddObject(ObjectType.Compressor, 2605, 1182, "COM-02")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_0726c148_284e_4b38_9394_5edc1dcd3361
MaterialStream37 = sim.AddObject(ObjectType.MaterialStream, 2968, 1184, "Methane")
MaterialStream37 = MaterialStream37.GetAsObject()
MaterialStream37.SetTemperature(373.356188861498)  # Temperature in K
MaterialStream37.SetPressure(6079500)  # Pressure in Pa
MaterialStream37.SetMassFlow(21.4750693988583)  # Mass Flow in kg/s

# Adding EnergyStream: EN_513bdf94_8d61_4afb_b994_c3800bfd5341
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2508, 1219, "E-06")
EnergyStream8 = EnergyStream8.GetAsObject()

sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream29.GraphicObject, -1, -1)  # Splitter2 to MaterialStream29
sim.ConnectObjects(Expander1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # Expander1 to EnergyStream2
sim.ConnectObjects(MaterialStream28.GraphicObject, Splitter2.GraphicObject, -1, -1)  # MaterialStream28 to Splitter2
sim.ConnectObjects(MaterialStream26.GraphicObject, Vessel2.GraphicObject, -1, -1)  # MaterialStream26 to Vessel2
sim.ConnectObjects(MaterialStream8.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream8 to Valve2
sim.ConnectObjects(MaterialStream24.GraphicObject, Valve5.GraphicObject, -1, -1)  # MaterialStream24 to Valve5
sim.ConnectObjects(MaterialStream7.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream7 to CapeOpenUO3
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream37.GraphicObject, -1, -1)  # Compressor2 to MaterialStream37
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # Cooler1 to EnergyStream4
sim.ConnectObjects(MaterialStream35.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream35 to HeatExchanger2
sim.ConnectObjects(MaterialStream21.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # MaterialStream21 to CapeOpenUO5
sim.ConnectObjects(MaterialStream22.GraphicObject, Expander1.GraphicObject, -1, -1)  # MaterialStream22 to Expander1
sim.ConnectObjects(MaterialStream19.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream19 to HeatExchanger1
sim.ConnectObjects(CapeOpenUO5.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # CapeOpenUO5 to MaterialStream13
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # Cooler1 to MaterialStream26
sim.ConnectObjects(Valve4.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Valve4 to MaterialStream12
sim.ConnectObjects(EnergyStream1.GraphicObject, Vessel1.GraphicObject, -1, -1)  # EnergyStream1 to Vessel1
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Vessel2 to MaterialStream25
sim.ConnectObjects(MaterialStream31.GraphicObject, Cooler3.GraphicObject, -1, -1)  # MaterialStream31 to Cooler3
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream34.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream34
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream18
sim.ConnectObjects(MaterialStream6.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream6 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream4
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream11
sim.ConnectObjects(Cooler3.GraphicObject, MaterialStream32.GraphicObject, -1, -1)  # Cooler3 to MaterialStream32
# sim.ConnectObjects(MaterialStream12.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # MaterialStream12 to CapeOpenUO5
# sim.ConnectObjects(MaterialStream16.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # MaterialStream16 to CapeOpenUO5
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream28.GraphicObject, -1, -1)  # Compressor1 to MaterialStream28
sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream30.GraphicObject, -1, -1)  # Splitter2 to MaterialStream30
sim.ConnectObjects(Cooler3.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # Cooler3 to EnergyStream7
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # Vessel2 to MaterialStream24
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream8
sim.ConnectObjects(MaterialStream32.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream32 to Mixer1
sim.ConnectObjects(MaterialStream30.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream30 to Cooler2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream20
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # Cooler2 to EnergyStream6
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Recycle1 to MaterialStream19
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream31.GraphicObject, -1, -1)  # Cooler2 to MaterialStream31
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream36.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream36
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream35.GraphicObject, -1, -1)  # Recycle2 to MaterialStream35
sim.ConnectObjects(Expander1.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Expander1 to MaterialStream17
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream5
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Vessel1 to MaterialStream15
sim.ConnectObjects(MaterialStream5.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream5 to Valve1
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Valve2 to MaterialStream6
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream33.GraphicObject, -1, -1)  # Mixer1 to MaterialStream33
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream1
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Splitter1 to MaterialStream22
sim.ConnectObjects(MaterialStream34.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream34 to Cooler1
sim.ConnectObjects(MaterialStream14.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream14 to Recycle1
sim.ConnectObjects(EnergyStream3.GraphicObject, Vessel2.GraphicObject, -1, -1)  # EnergyStream3 to Vessel2
sim.ConnectObjects(Valve5.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Valve5 to MaterialStream21
# sim.ConnectObjects(MaterialStream15.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # MaterialStream15 to CapeOpenUO5
sim.ConnectObjects(MaterialStream10.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream10 to Valve3
sim.ConnectObjects(MaterialStream18.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream18 to Recycle2
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Vessel1 to MaterialStream16
sim.ConnectObjects(MaterialStream13.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # MaterialStream13 to CapeOpenUO4
sim.ConnectObjects(EnergyStream5.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream5 to Compressor1
sim.ConnectObjects(CapeOpenUO5.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # CapeOpenUO5 to MaterialStream14
sim.ConnectObjects(MaterialStream17.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream17 to Vessel1
sim.ConnectObjects(MaterialStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream3 to CapeOpenUO1
sim.ConnectObjects(MaterialStream33.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream33 to HeatExchanger2
sim.ConnectObjects(CapeOpenUO4.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO4 to MaterialStream10
sim.ConnectObjects(MaterialStream23.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream23 to HeatExchanger1
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream9
sim.ConnectObjects(MaterialStream36.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream36 to Compressor2
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Splitter1 to MaterialStream23
sim.ConnectObjects(MaterialStream25.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream25 to Splitter1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream2
sim.ConnectObjects(MaterialStream20.GraphicObject, Valve4.GraphicObject, -1, -1)  # MaterialStream20 to Valve4
sim.ConnectObjects(MaterialStream27.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream27 to Compressor1
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Valve3 to MaterialStream7
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Valve1 to MaterialStream3
sim.ConnectObjects(EnergyStream8.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream8 to Compressor2
sim.ConnectObjects(MaterialStream29.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream29 to Mixer1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_27.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_27.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

