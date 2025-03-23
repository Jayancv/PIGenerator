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
isobutane = sim.AvailableCompounds["Isobutane"]
sim.SelectedCompounds.Add(isobutane.Name, isobutane)
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
n_pentane = sim.AvailableCompounds["N-pentane"]
sim.SelectedCompounds.Add(n_pentane.Name, n_pentane)
ethane = sim.AvailableCompounds["Ethane"]
sim.SelectedCompounds.Add(ethane.Name, ethane)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)
isopentane = sim.AvailableCompounds["Isopentane"]
sim.SelectedCompounds.Add(isopentane.Name, isopentane)
n_hexane = sim.AvailableCompounds["N-hexane"]
sim.SelectedCompounds.Add(n_hexane.Name, n_hexane)
n_heptane = sim.AvailableCompounds["N-heptane"]
sim.SelectedCompounds.Add(n_heptane.Name, n_heptane)
n_butane = sim.AvailableCompounds["N-butane"]
sim.SelectedCompounds.Add(n_butane.Name, n_butane)

# Adding Simulation Objects
# Adding MaterialStream: MAT_bad3edf8_0aa2_4795_a92d_662f79a72317
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2108, 978, "MSTR-026")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(281.956578872337)  # Temperature in K
MaterialStream1.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream1.SetMassFlow(505.743554383025)  # Mass Flow in kg/s

# Adding NodeIn: MIST_ac3f62dd_b8e1_4d2e_9ab0_c8fbd946f334
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2040, 979, "LEF pre-mixer")
Mixer1 = Mixer1.GetAsObject()

# Adding EnergyStream: EN_3f5431ec_6896_4f48_b5bf_95d90e45c4c4
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1837, 951, "ESTR-024")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_26d7282d_2b3e_4f74_8b80_ffdb3192792f
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1912, 973, "MSTR-023")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(289.15)  # Temperature in K
MaterialStream2.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream2.SetMassFlow(207.899708741935)  # Mass Flow in kg/s

# Adding Heater: AQ_642b427a_e071_4fa4_8f53_ad3eb8fc53b1
Heater1 = sim.AddObject(ObjectType.Heater, 1871, 890, "Chiller-3")
Heater1 = Heater1.GetAsObject()

# Adding EnergyStream: EN_5299fb40_6556_40d4_b283_d45a1868cd00
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 1612, 987, "ESTR-021")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_562e83eb_f179_4692_a472_42f35ffedfed
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1837, 992, "MSTR-020")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(291.15)  # Temperature in K
MaterialStream3.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream3.SetMassFlow(297.84384564109)  # Mass Flow in kg/s

# Adding Heater: AQ_d27706a8_7a85_4c5c_a0b6_bc3fd6a4e935
Heater2 = sim.AddObject(ObjectType.Heater, 1635, 901, "Chiller-2")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_7c79a0bf_5bdc_4564_a7b7_a1b3acf8a71f
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1818, 894, "MSTR-018")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(198.432713979534)  # Temperature in K
MaterialStream4.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream4.SetMassFlow(207.899708741935)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_d161a4b4_ebbc_470b_a157_51c9336fb50a
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1822, 734, "MSTR-017")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(198.432713979534)  # Temperature in K
MaterialStream5.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream5.SetMassFlow(1804.65146723467)  # Mass Flow in kg/s

# Adding Vessel: SEP_b029bcc5_61d5_4408_96f5_5e1419532722
Vessel1 = sim.AddObject(ObjectType.Vessel, 1755, 789, "LP Separator")
Vessel1 = Vessel1.GetAsObject()

# Adding EnergyStream: EN_52b983ea_80e7_47ef_8ef3_e33025180910
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1694, 861, "Compressor1")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_b695a39d_ca3f_4886_a2bb_05aa7969ab4e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1722, 791, "MSTR-014")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(198.432713979534)  # Temperature in K
MaterialStream6.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream6.SetMassFlow(2012.55121531724)  # Mass Flow in kg/s

# Adding Expander: TURB_e7c242a9_c8e2_4cf0_9a4b_77b99d0df106
Expander1 = sim.AddObject(ObjectType.Expander, 1670, 788, "Expander-1")
Expander1 = Expander1.GetAsObject()

# Adding MaterialStream: MAT_0911b69e_f626_4c3d_bca7_d06676646e3e
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1590, 903, "MSTR-012")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(243.149891076408)  # Temperature in K
MaterialStream7.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream7.SetMassFlow(297.84384564109)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_8c549cd3_bf54_44cf_b347_b2fd53f5e76d
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1600, 731, "MSTR-011")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(243.15)  # Temperature in K
MaterialStream8.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream8.SetMassFlow(2012.55121531724)  # Mass Flow in kg/s

# Adding Vessel: SEP_aed4c65e_9d00_41b9_b553_945444ea09fd
Vessel2 = sim.AddObject(ObjectType.Vessel, 1523, 791, "HP Separator")
Vessel2 = Vessel2.GetAsObject()

# Adding EnergyStream: EN_157a982f_365b_41fc_a3bd_c0d77b344c45
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1371, 887, "ESTR-009")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_0f190503_a24b_4b8d_b9a9_4be455f09076
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1463, 793, "MSTR-008")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(243.15)  # Temperature in K
MaterialStream9.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream9.SetMassFlow(2310.39518009768)  # Mass Flow in kg/s

# Adding Heater: AQ_30d5d772_5e7c_4262_b103_6879a9bce925
Heater3 = sim.AddObject(ObjectType.Heater, 1399, 792, "Chiller-1")
Heater3 = Heater3.GetAsObject()

# Adding Vessel: SEP_d723d4b1_6342_4460_b05e_caa4ad497055
Vessel3 = sim.AddObject(ObjectType.Vessel, 1236, 794, "KOD")
Vessel3 = Vessel3.GetAsObject()

# Adding MaterialStream: MAT_65967c35_a9e6_4b10_96a8_69b0453a1af8
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1310, 795, "MSTR-005")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(298.15)  # Temperature in K
MaterialStream10.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream10.SetMassFlow(2310.39518009768)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_c839e355_82e0_42cb_a752_7cc77492b2b8
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1305, 900, "Water")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(298.15)  # Temperature in K
MaterialStream11.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream11.SetMassFlow(0)  # Mass Flow in kg/s

# Adding Heater: AQ_c80874f6_aaa8_4e6a_84e1_c98c54299206
Heater4 = sim.AddObject(ObjectType.Heater, 1114, 790, "Pre-Chiller")
Heater4 = Heater4.GetAsObject()

# Adding MaterialStream: MAT_19329edc_52b5_4234_9c61_ed44cf204749
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1177, 793, "MSTR-002")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(298.15)  # Temperature in K
MaterialStream12.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream12.SetMassFlow(2310.39518009768)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ed5056bc_32de_494d_9668_eea0d2cb06b0
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1029, 792, "MSTR-000")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(303.15)  # Temperature in K
MaterialStream13.SetPressure(5218286.5)  # Pressure in Pa
MaterialStream13.SetMassFlow(2310.39518009768)  # Mass Flow in kg/s

# Adding EnergyStream: EN_467d0fb0_9a57_421b_b836_b01e7c80b98c
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1092, 853, "ESTR-003")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding CapeOpenUO: COUO_7047abe2_de1a_42f2_90a4_a6c02f2340ec
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2190, 976, "LEF Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_acb0e57e_fecb_4318_8a99_829c861eb16a
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2285, 897, "MSTR-028")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(172.309796167186)  # Temperature in K
MaterialStream14.SetPressure(1765500)  # Pressure in Pa
MaterialStream14.SetMassFlow(148.21683746354)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_523c32c6_1796_422e_a893_d0bb09f0936c
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2282, 1045, "MSTR-029")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(328.943430895733)  # Temperature in K
MaterialStream15.SetPressure(1765500)  # Pressure in Pa
MaterialStream15.SetMassFlow(357.526716919481)  # Mass Flow in kg/s

# Adding Heater: AQ_5cac4be4_ec6b_452e_9c3f_6fc8a85f8874
Heater5 = sim.AddObject(ObjectType.Heater, 1928, 734, "Condenser")
Heater5 = Heater5.GetAsObject()

# Adding MaterialStream: MAT_6a7ea946_fa8c_4640_a277_17c5dd6c6786
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2285, 863, "MSTR-031")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(293.15)  # Temperature in K
MaterialStream16.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream16.SetMassFlow(1804.65146723467)  # Mass Flow in kg/s

# Adding EnergyStream: EN_99a3aae5_fbb4_46d0_ace5_ab279d1f6864
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1904, 786, "ESTR-032")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding NodeIn: MIST_2e4a86be_dcc8_414a_83fc_ebafca9d5461
Mixer2 = sim.AddObject(ObjectType.NodeIn, 2360, 874, "Lean Gas Mixer")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_63c739b5_ef9a_4541_82b2_1317d9c780d2
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2431, 875, "MSTR-034")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(271.85767465525)  # Temperature in K
MaterialStream17.SetPressure(1765500)  # Pressure in Pa
MaterialStream17.SetMassFlow(1952.86830469821)  # Mass Flow in kg/s

# Adding Heater: AQ_4e835ed9_46b0_4a16_9e2c_0f62ecd39a1e
Heater6 = sim.AddObject(ObjectType.Heater, 2500, 870, "Chiller-4")
Heater6 = Heater6.GetAsObject()

# Adding MaterialStream: MAT_67294603_05f9_421b_9381_8b15d2179edb
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2555, 882, "MSTR-036")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(303.15)  # Temperature in K
MaterialStream18.SetPressure(1765500)  # Pressure in Pa
MaterialStream18.SetMassFlow(1952.86830469821)  # Mass Flow in kg/s

# Adding EnergyStream: EN_11690195_1c33_434f_afca_443addf3c41c
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2465, 944, "ESTR-037")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding Compressor: COMP_b7965304_5e28_41df_a81b_20a9421a16d9
Compressor1 = sim.AddObject(ObjectType.Compressor, 2657, 877, "Compressor-1")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_ec1bad8f_6516_4097_add8_388fd34e6d14
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2747, 881, "MSTR-039")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(303.164183357185)  # Temperature in K
MaterialStream19.SetPressure(1765775.82106668)  # Pressure in Pa
MaterialStream19.SetMassFlow(1952.86830469821)  # Mass Flow in kg/s

# Adding EnergyStream: EN_35bc3088_2ef7_4a82_9a0d_91a69eb7241a
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2609, 943, "Expander1")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding Compressor: COMP_06c4eecd_8a0b_42b4_8c76_57ac5ddd5018
Compressor2 = sim.AddObject(ObjectType.Compressor, 2843, 878, "Compressor")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_37af0226_4681_429b_a1c0_ce58329b40cc
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2898, 890, "Lean Gas")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(352.352625666603)  # Temperature in K
MaterialStream20.SetPressure(3000000)  # Pressure in Pa
MaterialStream20.SetMassFlow(1952.86830469821)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3c38be0d_b1a4_4bc8_995c_60eae56107a6
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2810, 947, "ESTR-043")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding CapeOpenUO: COUO_3638b9c9_be8d_4681_a65b_9b1973e660dd
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 2362, 1036, "LPG Column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding MaterialStream: MAT_b341ded4_f48a_4981_a26d_e6933c88f69d
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 2448, 992, "LPG")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(316.87538765742)  # Temperature in K
MaterialStream21.SetPressure(1765500)  # Pressure in Pa
MaterialStream21.SetMassFlow(256.069231213361)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_708ac01f_7223_403f_af69_86355fbdcef0
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 2446, 1084, "MSTR-046")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(385.175933682029)  # Temperature in K
MaterialStream22.SetPressure(1029698)  # Pressure in Pa
MaterialStream22.SetMassFlow(101.457485706185)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_eb6a221c_2459_451e_9478_aa484c53531f
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 2568, 1021, "Heaviers Column")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_239a4244_c8f0_44cf_84b8_627e3ccbcf2d
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2663, 971, "Pentane")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(366.970129715037)  # Temperature in K
MaterialStream23.SetPressure(1029698)  # Pressure in Pa
MaterialStream23.SetMassFlow(45.5465172472805)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b99db877_6136_4d4f_9eb0_e2cf67154a02
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 2661, 1072, "Naphtha")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(291.090923785846)  # Temperature in K
MaterialStream24.SetPressure(49033.3)  # Pressure in Pa
MaterialStream24.SetMassFlow(55.9109684587687)  # Mass Flow in kg/s

# Adding EnergyStream: EN_e90e9ceb_c5c5_4001_bf76_548ea2c069f3
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 1505, 921, "ESTR-050")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding EnergyStream: EN_4db3f7a8_a682_4844_bfee_6d2b05ef3d5e
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 1700, 1022, "ESTR-051")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding Heater: AQ_753235a3_a172_41ff_b261_17d6a452e811
Heater7 = sim.AddObject(ObjectType.Heater, 2069, 1063, "HEAT-052")
Heater7 = Heater7.GetAsObject()

# Adding MaterialStream: MAT_aa2a0c2f_f42f_48fe_be5d_99e2881bf71d
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 2140, 1055, "MSTR-053")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(291.15)  # Temperature in K
MaterialStream25.SetPressure(1765585.7)  # Pressure in Pa
MaterialStream25.SetMassFlow(505.743554383025)  # Mass Flow in kg/s

# Adding EnergyStream: EN_8fcb3fe8_5cd6_44b3_9850_0aaaabff7018
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 2111, 1118, "ESTR-054")
EnergyStream12 = EnergyStream12.GetAsObject()

sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream23
sim.ConnectObjects(EnergyStream4.GraphicObject, Heater3.GraphicObject, -1, -1)  # EnergyStream4 to Heater3
sim.ConnectObjects(MaterialStream12.GraphicObject, Vessel3.GraphicObject, -1, -1)  # MaterialStream12 to Vessel3
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Vessel2 to MaterialStream8
sim.ConnectObjects(EnergyStream9.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream9 to Compressor2
sim.ConnectObjects(MaterialStream19.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream19 to Compressor2
sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream2 to Mixer1
sim.ConnectObjects(MaterialStream25.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream25 to CapeOpenUO1
sim.ConnectObjects(MaterialStream7.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream7 to Heater2
sim.ConnectObjects(MaterialStream8.GraphicObject, Expander1.GraphicObject, -1, -1)  # MaterialStream8 to Expander1
sim.ConnectObjects(Expander1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Expander1 to MaterialStream6
sim.ConnectObjects(EnergyStream7.GraphicObject, Heater6.GraphicObject, -1, -1)  # EnergyStream7 to Heater6
sim.ConnectObjects(MaterialStream22.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream22 to CapeOpenUO3
sim.ConnectObjects(MaterialStream18.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream18 to Compressor1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Vessel1 to MaterialStream5
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream22
sim.ConnectObjects(EnergyStream6.GraphicObject, Heater5.GraphicObject, -1, -1)  # EnergyStream6 to Heater5
sim.ConnectObjects(MaterialStream16.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream16 to Mixer2
sim.ConnectObjects(Heater7.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Heater7 to MaterialStream25
sim.ConnectObjects(EnergyStream1.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream1 to Heater1
sim.ConnectObjects(EnergyStream11.GraphicObject, Vessel1.GraphicObject, -1, -1)  # EnergyStream11 to Vessel1
sim.ConnectObjects(EnergyStream2.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream2 to Heater2
sim.ConnectObjects(MaterialStream13.GraphicObject, Heater4.GraphicObject, -1, -1)  # MaterialStream13 to Heater4
sim.ConnectObjects(MaterialStream5.GraphicObject, Heater5.GraphicObject, -1, -1)  # MaterialStream5 to Heater5
sim.ConnectObjects(Heater5.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Heater5 to MaterialStream16
sim.ConnectObjects(Vessel3.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Vessel3 to MaterialStream10
sim.ConnectObjects(MaterialStream15.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream15 to CapeOpenUO2
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream21
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Mixer2 to MaterialStream17
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Compressor2 to MaterialStream20
sim.ConnectObjects(MaterialStream4.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream4 to Heater1
sim.ConnectObjects(EnergyStream8.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream8 to Compressor1
sim.ConnectObjects(EnergyStream10.GraphicObject, Vessel2.GraphicObject, -1, -1)  # EnergyStream10 to Vessel2
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Mixer1 to MaterialStream1
sim.ConnectObjects(Heater3.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Heater3 to MaterialStream9
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Heater2 to MaterialStream3
sim.ConnectObjects(EnergyStream12.GraphicObject, Heater7.GraphicObject, -1, -1)  # EnergyStream12 to Heater7
sim.ConnectObjects(Expander1.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # Expander1 to EnergyStream3
sim.ConnectObjects(Vessel3.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Vessel3 to MaterialStream11
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Heater1 to MaterialStream2
sim.ConnectObjects(MaterialStream17.GraphicObject, Heater6.GraphicObject, -1, -1)  # MaterialStream17 to Heater6
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream24
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Vessel1 to MaterialStream4
sim.ConnectObjects(MaterialStream10.GraphicObject, Heater3.GraphicObject, -1, -1)  # MaterialStream10 to Heater3
sim.ConnectObjects(EnergyStream5.GraphicObject, Heater4.GraphicObject, -1, -1)  # EnergyStream5 to Heater4
sim.ConnectObjects(MaterialStream9.GraphicObject, Vessel2.GraphicObject, -1, -1)  # MaterialStream9 to Vessel2
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream15
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Compressor1 to MaterialStream19
sim.ConnectObjects(MaterialStream14.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream14 to Mixer2
sim.ConnectObjects(Heater4.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Heater4 to MaterialStream12
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream14
sim.ConnectObjects(Heater6.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Heater6 to MaterialStream18
sim.ConnectObjects(MaterialStream1.GraphicObject, Heater7.GraphicObject, -1, -1)  # MaterialStream1 to Heater7
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Vessel2 to MaterialStream7
sim.ConnectObjects(MaterialStream6.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream6 to Vessel1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_51.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_51.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

