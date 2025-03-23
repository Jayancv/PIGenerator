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
ethane = sim.AvailableCompounds["Ethane"]
sim.SelectedCompounds.Add(ethane.Name, ethane)
methane = sim.AvailableCompounds["Methane"]
sim.SelectedCompounds.Add(methane.Name, methane)
propane = sim.AvailableCompounds["Propane"]
sim.SelectedCompounds.Add(propane.Name, propane)
n_butane = sim.AvailableCompounds["N-butane"]
sim.SelectedCompounds.Add(n_butane.Name, n_butane)

# Adding Simulation Objects
# Adding EnergyStream: EN_01f57d50_5649_4e58_9f89_2671cd08a46c
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2974, 1655, "E1-2")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_6f4a0ec9_3b98_4ffb_aa27_d474addc89b1
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 3095, 1748, "NG-2")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(144.05)  # Temperature in K
MaterialStream1.SetPressure(3000000)  # Pressure in Pa
MaterialStream1.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding Cooler: RESF_ff7e6811_3892_4fa4_b194_3d8eca5a1295
Cooler1 = sim.AddObject(ObjectType.Cooler, 2934, 1746, "COOL-121")
Cooler1 = Cooler1.GetAsObject()

# Adding EnergyStream: EN_ab7a13d8_32bd_47db_b49f_7eac7e2a06ab
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2149, 1093, "E3-3")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding CapeOpenUO: COUO_c658bcc3_0430_4074_8558_e8a7ffec86dd
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2137, 1135, "COUO-076")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_5280af78_54ae_46ed_b86d_ef251f88bc0c
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2126, 1038, "P-5")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(256.694062769504)  # Temperature in K
MaterialStream2.SetPressure(808000)  # Pressure in Pa
MaterialStream2.SetMassFlow(519.169)  # Mass Flow in kg/s

# Adding Valve: VALV_f1fece63_355c_41b6_bcd2_2b04370ee812
Valve1 = sim.AddObject(ObjectType.Valve, 2189, 1046, "VALV-200")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_3c30c904_8425_4e3c_a492_d4a45b6f2c4f
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2276, 1208, "P-4")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(276.265)  # Temperature in K
MaterialStream3.SetPressure(2225000)  # Pressure in Pa
MaterialStream3.SetMassFlow(387.316555555556)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b0a5006c_b0cf_4831_8ac1_8082369f21dd
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2269, 1129, "P-3")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(276.265)  # Temperature in K
MaterialStream4.SetPressure(2225000)  # Pressure in Pa
MaterialStream4.SetMassFlow(519.169)  # Mass Flow in kg/s

# Adding NodeOut: DIV_6713af0d_f913_469f_9f0c_1f5fa6677adf
Splitter1 = sim.AddObject(ObjectType.NodeOut, 2202, 1194, "SPLT-100")
Splitter1 = Splitter1.GetAsObject()

# Adding EnergyStream: EN_3927f861_6f95_461b_828c_6dc84ecf4d2f
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2067, 1224, "E3-2")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_5f59071d_9231_419c_abd5_282373e45779
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2158, 1195, "P-2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(276.265)  # Temperature in K
MaterialStream5.SetPressure(2225000)  # Pressure in Pa
MaterialStream5.SetMassFlow(906.485555555556)  # Mass Flow in kg/s

# Adding Cooler: RESF_dfa1c24c_456d_4768_8711_846f3ac207f1
Cooler2 = sim.AddObject(ObjectType.Cooler, 2024, 1184, "COOL-068")
Cooler2 = Cooler2.GetAsObject()

# Adding MaterialStream: MAT_f3cc0eb0_d20d_4c19_b27c_86b2bcb6a263
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2420, 1449, "L-10")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(218.3022)  # Temperature in K
MaterialStream6.SetPressure(265000)  # Pressure in Pa
MaterialStream6.SetMassFlow(391.267232927784)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_b04452b8_f8f6_43c3_a799_824d70388fa7
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2521, 1528, "REC-066")
Recycle1 = Recycle1.GetAsObject()

# Adding CapeOpenUO: COUO_8a33eb86_00b5_4edc_972b_7b324fe72443
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 3078, 1596, "COUO-119")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding EnergyStream: EN_0198135f_6819_4ce5_b9a8_b869ec51b894
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 3150, 1593, "E1-4")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_a9a5ac87_559e_4067_b339_a76b08bb6812
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2590, 1560, "MSTR-063")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(218.3022)  # Temperature in K
MaterialStream7.SetPressure(265000)  # Pressure in Pa
MaterialStream7.SetMassFlow(391.267232927784)  # Mass Flow in kg/s

# Adding Heater: AQ_3e52bf68_24ed_4238_918e_eef25aebb490
Heater1 = sim.AddObject(ObjectType.Heater, 2930, 1549, "HEAT-062")
Heater1 = Heater1.GetAsObject()

# Adding MaterialStream: MAT_1779c771_805c_4c46_b3e7_1904ac074bc0
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 3086, 1529, "L-9")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(141.937160726512)  # Temperature in K
MaterialStream8.SetPressure(315000)  # Pressure in Pa
MaterialStream8.SetMassFlow(391.267232927784)  # Mass Flow in kg/s

# Adding NodeIn: MIST_04b88a44_c866_46ea_80ab_62ae55f8260e
Mixer1 = sim.AddObject(ObjectType.NodeIn, 3151, 1523, "MIX-100")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_f903a58d_79c7_49bc_91e1_e989e9885a8e
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 3182, 1612, "8")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(145.058597342429)  # Temperature in K
MaterialStream9.SetPressure(315000)  # Pressure in Pa
MaterialStream9.SetMassFlow(245.16998250195)  # Mass Flow in kg/s

# Adding Valve: VALV_2cfa1fa8_1336_4b6d_bc16_8faa38723ff1
Valve2 = sim.AddObject(ObjectType.Valve, 3150, 1650, "VALV-102")
Valve2 = Valve2.GetAsObject()

# Adding EnergyStream: EN_88416063_3703_49c0_aeac_ae4ac3b476a7
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2981, 1805, "E1-1")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_2a56da55_4e34_4504_be03_99e558677e84
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 3080, 1647, "L-8")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(148.35)  # Temperature in K
MaterialStream10.SetPressure(1900000)  # Pressure in Pa
MaterialStream10.SetMassFlow(245.16998250195)  # Mass Flow in kg/s

# Adding Cooler: RESF_e3325298_3aec_4d54_9fbb_01e09a6da136
Cooler3 = sim.AddObject(ObjectType.Cooler, 2935, 1616, "COOL-055")
Cooler3 = Cooler3.GetAsObject()

# Adding EnergyStream: EN_b2be5c1d_e327_4a21_89b5_64fec00f357e
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 3379, 1643, "E2-2")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding CapeOpenUO: COUO_c3654dc1_5af9_4143_94f3_3c20c120e085
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 3384, 1703, "COUO-053")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_ae0851e4_7548_491e_97a0_8c550d210f1e
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 3221, 1560, "L-7")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(134.456)  # Temperature in K
MaterialStream11.SetPressure(315000)  # Pressure in Pa
MaterialStream11.SetMassFlow(146.097250425834)  # Mass Flow in kg/s

# Adding Heater: AQ_344cc183_7f47_44c1_be9b_4a538fd459e7
Heater2 = sim.AddObject(ObjectType.Heater, 3262, 1623, "HEAT-051")
Heater2 = Heater2.GetAsObject()

# Adding MaterialStream: MAT_4ffe339b_0665_4764_b3c7_a22eb25f8082
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 3644, 1596, "L-6")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(106.010689647287)  # Temperature in K
MaterialStream12.SetPressure(325000)  # Pressure in Pa
MaterialStream12.SetMassFlow(146.097250425834)  # Mass Flow in kg/s

# Adding Valve: VALV_ebb60c73_0f61_4563_b639_c67564934d77
Valve3 = sim.AddObject(ObjectType.Valve, 3580, 1667, "VALV-101")
Valve3 = Valve3.GetAsObject()

# Adding EnergyStream: EN_61a92234_e367_4483_b0b2_afd015c3983e
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 3230, 1719, "E2-3")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_1ebc807a_a7ec_4f09_b3db_f64ea83df1ba
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 3454, 1661, "L-5")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(108.65)  # Temperature in K
MaterialStream13.SetPressure(1400000)  # Pressure in Pa
MaterialStream13.SetMassFlow(146.097250425834)  # Mass Flow in kg/s

# Adding Cooler: RESF_2aa8b799_cf10_42f4_b6a0_4c1a1b5e1d7d
Cooler4 = sim.AddObject(ObjectType.Cooler, 3256, 1680, "COOL-046")
Cooler4 = Cooler4.GetAsObject()

# Adding EnergyStream: EN_27f50096_b571_4b17_8a30_a4f8f9824d4f
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2980, 1720, "E1-3")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding MaterialStream: MAT_480cd763_ce5b_4749_8172_6c5ec985fe78
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 3117, 1688, "L-4")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(155.95)  # Temperature in K
MaterialStream14.SetPressure(1900000)  # Pressure in Pa
MaterialStream14.SetMassFlow(146.097250425834)  # Mass Flow in kg/s

# Adding Cooler: RESF_2bb8bbd8_05e6_4fe4_bfcb_5435bea52155
Cooler5 = sim.AddObject(ObjectType.Cooler, 2935, 1675, "COOL-043")
Cooler5 = Cooler5.GetAsObject()

# Adding MaterialStream: MAT_18c57284_edd4_45c6_9734_b47030d3270f
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2733, 1608, "L-3")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(211.24)  # Temperature in K
MaterialStream15.SetPressure(2400000)  # Pressure in Pa
MaterialStream15.SetMassFlow(245.16998250195)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_580c29d6_1cdd_4215_ae7b_700b2902de7b
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2817, 1357, "L-2")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(211.24)  # Temperature in K
MaterialStream16.SetPressure(2400000)  # Pressure in Pa
MaterialStream16.SetMassFlow(146.097250425834)  # Mass Flow in kg/s

# Adding Vessel: SEP_c67c85c2_3fac_43a6_a538_33721bfc01ef
Vessel1 = sim.AddObject(ObjectType.Vessel, 2733, 1428, "SEP-100")
Vessel1 = Vessel1.GetAsObject()

# Adding EnergyStream: EN_197c365d_d6d0_4053_9e39_c9c2c1a0cccf
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 2947, 1314, "E5-1")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding MaterialStream: MAT_47157eb3_22ce_48e8_a793_7bdb1ac67d42
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 3225, 1366, "L-1")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(211.24)  # Temperature in K
MaterialStream17.SetPressure(2400000)  # Pressure in Pa
MaterialStream17.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Cooler: RESF_dc888f3c_74d9_487c_b7a3_078ed06b3e18
Cooler6 = sim.AddObject(ObjectType.Cooler, 2903, 1265, "COOL-037")
Cooler6 = Cooler6.GetAsObject()

# Adding EnergyStream: EN_5ccbcb23_8377_4315_92dd_f64e317dd585
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 2411, 1303, "E4-1")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding MaterialStream: MAT_94e47fa3_25f6_4fca_b0e0_8ab225047859
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2702, 1275, "L-17")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(235.35)  # Temperature in K
MaterialStream18.SetPressure(2705000)  # Pressure in Pa
MaterialStream18.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Cooler: RESF_966c8c7f_8f1c_4777_9f72_86ec89e07c9a
Cooler7 = sim.AddObject(ObjectType.Cooler, 2397, 1263, "COOL-034")
Cooler7 = Cooler7.GetAsObject()

# Adding EnergyStream: EN_7ee5bdb2_cec2_468a_804e_9984c641d700
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 2058, 1299, "E3-1")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding MaterialStream: MAT_127cd7aa_fde0_497c_94c4_22491ad7cc63
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2203, 1248, "L-16")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(275.11)  # Temperature in K
MaterialStream19.SetPressure(3005000)  # Pressure in Pa
MaterialStream19.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Cooler: RESF_f02c7ba3_2bbb_4d2f_a54a_7601a54be88d
Cooler8 = sim.AddObject(ObjectType.Cooler, 2024, 1247, "COOL-031")
Cooler8 = Cooler8.GetAsObject()

# Adding EnergyStream: EN_f48832ea_c417_4fdc_bd94_2019891b0d3c
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 1813, 1518, "ESTR-030")
EnergyStream12 = EnergyStream12.GetAsObject()

# Adding MaterialStream: MAT_7d3c0f6e_7744_4e49_9433_4415ba78ac70
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1770, 1274, "L-15")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(358.15)  # Temperature in K
MaterialStream20.SetPressure(3485000)  # Pressure in Pa
MaterialStream20.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Heater: AQ_76318934_5b28_448b_accf_7ad56241f463
Heater3 = sim.AddObject(ObjectType.Heater, 1770, 1463, "E-102")
Heater3 = Heater3.GetAsObject()

# Adding EnergyStream: EN_9d2f6882_1bc8_4e08_a6c9_8e9947ee2230
EnergyStream13 = sim.AddObject(ObjectType.EnergyStream, 1915, 1815, "ESTR-027")
EnergyStream13 = EnergyStream13.GetAsObject()

# Adding MaterialStream: MAT_69ca4547_547e_4ded_a03d_ef998be637bb
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1772, 1544, "L-14")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(310.743299465252)  # Temperature in K
MaterialStream21.SetPressure(3500000)  # Pressure in Pa
MaterialStream21.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Compressor: COMP_05b5c979_529a_4d1e_900a_590e87f2632d
Compressor1 = sim.AddObject(ObjectType.Compressor, 1872, 1785, "K-100")
Compressor1 = Compressor1.GetAsObject()

# Adding EnergyStream: EN_75011227_94ce_4bbf_8d09_42c267c510f2
EnergyStream14 = sim.AddObject(ObjectType.EnergyStream, 2149, 1830, "ESTR-024")
EnergyStream14 = EnergyStream14.GetAsObject()

# Adding MaterialStream: MAT_87adfc03_a6f5_4189_bd1e_970b4209af78
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1971, 1799, "L-13")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(298.15)  # Temperature in K
MaterialStream22.SetPressure(2985000)  # Pressure in Pa
MaterialStream22.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Cooler: RESF_31c024f2_8512_4403_86ce_67b99d5f18e9
Cooler9 = sim.AddObject(ObjectType.Cooler, 2107, 1800, "E-100")
Cooler9 = Cooler9.GetAsObject()

# Adding EnergyStream: EN_0aa6f5a9_880e_47ff_b393_81384ac729ac
EnergyStream15 = sim.AddObject(ObjectType.EnergyStream, 2361, 1826, "ESTR-021")
EnergyStream15 = EnergyStream15.GetAsObject()

# Adding MaterialStream: MAT_0363ceaa_458d_4d0c_946a_5c0abc26b8dd
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2204, 1800, "L-12")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(476.774435973259)  # Temperature in K
MaterialStream23.SetPressure(3000000)  # Pressure in Pa
MaterialStream23.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding Compressor: COMP_1785016e_c678_4341_962d_101168f481b8
Compressor2 = sim.AddObject(ObjectType.Compressor, 2319, 1796, "K-102")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_f1f57237_dacf_42cb_b810_7941637294f7
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 4020, 1782, "LNG")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(109.40189113462)  # Temperature in K
MaterialStream24.SetPressure(110000)  # Pressure in Pa
MaterialStream24.SetMassFlow(169.417319674091)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ed4bbbcc_2dcb_40d6_a24a_073afcc58205
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 4012, 1692, "NG-6")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(109.40189113462)  # Temperature in K
MaterialStream25.SetPressure(110000)  # Pressure in Pa
MaterialStream25.SetMassFlow(11.1129976477038)  # Mass Flow in kg/s

# Adding Vessel: SEP_2ce1fd45_c717_40d6_ad39_77805a08bb19
Vessel2 = sim.AddObject(ObjectType.Vessel, 3902, 1699, "SEP-101")
Vessel2 = Vessel2.GetAsObject()

# Adding MaterialStream: MAT_9c41d5dc_6a44_4734_940d_ae0879dcc292
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 3833, 1724, "NG-5")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(109.40189113462)  # Temperature in K
MaterialStream26.SetPressure(110000)  # Pressure in Pa
MaterialStream26.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding Valve: VALV_32cc2c07_eb8f_468e_a771_60b97413a3b7
Valve4 = sim.AddObject(ObjectType.Valve, 3765, 1728, "VALV-100")
Valve4 = Valve4.GetAsObject()

# Adding EnergyStream: EN_a88efad1_92be_4ac3_8e39_6a7b4b5ff2d0
EnergyStream16 = sim.AddObject(ObjectType.EnergyStream, 3490, 1788, "ESTR-013")
EnergyStream16 = EnergyStream16.GetAsObject()

# Adding MaterialStream: MAT_cb535012_645a_4e58_9141_e143a4816363
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 3650, 1731, "NG-4")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(116.030735794413)  # Temperature in K
MaterialStream27.SetPressure(1300000)  # Pressure in Pa
MaterialStream27.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding Expander: TURB_bfcc0421_64ac_47f1_bbbe_c884a429e49f
Expander1 = sim.AddObject(ObjectType.Expander, 3570, 1737, "EXP-026")
Expander1 = Expander1.GetAsObject()

# Adding EnergyStream: EN_bd652c72_4402_4425_9b6e_2a1f7b186d84
EnergyStream17 = sim.AddObject(ObjectType.EnergyStream, 3232, 1791, "E2-1")
EnergyStream17 = EnergyStream17.GetAsObject()

# Adding MaterialStream: MAT_10bb7977_c030_4798_9a25_b0eed023fea3
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 3450, 1766, "NG-3")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(116.15)  # Temperature in K
MaterialStream28.SetPressure(2500000)  # Pressure in Pa
MaterialStream28.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding Cooler: RESF_b49d1d90_9759_4239_b295_9f03180a5811
Cooler10 = sim.AddObject(ObjectType.Cooler, 3262, 1740, "COOL-008")
Cooler10 = Cooler10.GetAsObject()

# Adding MaterialStream: MAT_0566623c_9052_4c9b_8c24_b958d32704dc
MaterialStream29 = sim.AddObject(ObjectType.MaterialStream, 2441, 1797, "L-11")
MaterialStream29 = MaterialStream29.GetAsObject()
MaterialStream29.SetTemperature(271.43753)  # Temperature in K
MaterialStream29.SetPressure(215000)  # Pressure in Pa
MaterialStream29.SetMassFlow(391.267220010816)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4b7a72f4_60c2_44b9_8569_9ff5192fb338
MaterialStream30 = sim.AddObject(ObjectType.MaterialStream, 2511, 1693, "NG-1")
MaterialStream30 = MaterialStream30.GetAsObject()
MaterialStream30.SetTemperature(220.300421179293)  # Temperature in K
MaterialStream30.SetPressure(3500000)  # Pressure in Pa
MaterialStream30.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_9c3ed4d4_3beb_4269_bce9_968c9ddd0691
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 2432, 1639, "LNG-100")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_fa45fc4c_9735_4fcb_a417_ebbb97efa8c8
MaterialStream31 = sim.AddObject(ObjectType.MaterialStream, 1565, 1636, "Natural gas")
MaterialStream31 = MaterialStream31.GetAsObject()
MaterialStream31.SetTemperature(303.15)  # Temperature in K
MaterialStream31.SetPressure(4000000)  # Pressure in Pa
MaterialStream31.SetMassFlow(180.530317555556)  # Mass Flow in kg/s

# Adding EnergyStream: EN_36957e1d_95a5_4d05_bcc2_bace2f058101
EnergyStream18 = sim.AddObject(ObjectType.EnergyStream, 2442, 1238, "E4-2")
EnergyStream18 = EnergyStream18.GetAsObject()

# Adding MaterialStream: MAT_46c90d2e_74be_4299_ac92_e9e4a11bef7b
MaterialStream32 = sim.AddObject(ObjectType.MaterialStream, 2512, 1209, "P-6")
MaterialStream32 = MaterialStream32.GetAsObject()
MaterialStream32.SetTemperature(233.16)  # Temperature in K
MaterialStream32.SetPressure(2200000)  # Pressure in Pa
MaterialStream32.SetMassFlow(387.316555555556)  # Mass Flow in kg/s

# Adding Cooler: RESF_6c55414c_6338_499d_b12e_45dceb5acdf0
Cooler11 = sim.AddObject(ObjectType.Cooler, 2399, 1196, "COOL-080")
Cooler11 = Cooler11.GetAsObject()

# Adding Heater: AQ_ff399acf_40b1_46be_9765_ec5f1ad46491
Heater4 = sim.AddObject(ObjectType.Heater, 2026, 1124, "HEAT-081")
Heater4 = Heater4.GetAsObject()

# Adding MaterialStream: MAT_3acec2a2_9864_481c_8cad_991186db7217
MaterialStream33 = sim.AddObject(ObjectType.MaterialStream, 1958, 1057, "P-18")
MaterialStream33 = MaterialStream33.GetAsObject()
MaterialStream33.SetTemperature(299.7396)  # Temperature in K
MaterialStream33.SetPressure(783000)  # Pressure in Pa
MaterialStream33.SetMassFlow(519.169)  # Mass Flow in kg/s

# Adding NodeOut: DIV_8ebd3c91_9cde_4629_a45d_a0c700f87a98
Splitter2 = sim.AddObject(ObjectType.NodeOut, 2605, 1225, "SPLT-201")
Splitter2 = Splitter2.GetAsObject()

# Adding MaterialStream: MAT_bfe6c0be_e929_418d_80bf_0f7eb8268bdb
MaterialStream34 = sim.AddObject(ObjectType.MaterialStream, 2710, 1188, "P-7")
MaterialStream34 = MaterialStream34.GetAsObject()
MaterialStream34.SetTemperature(233.16)  # Temperature in K
MaterialStream34.SetPressure(2200000)  # Pressure in Pa
MaterialStream34.SetMassFlow(247.223333333333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f2e2ce16_0232_4345_b632_e492faa2ef5d
MaterialStream35 = sim.AddObject(ObjectType.MaterialStream, 2767, 1221, "P-8")
MaterialStream35 = MaterialStream35.GetAsObject()
MaterialStream35.SetTemperature(233.16)  # Temperature in K
MaterialStream35.SetPressure(2200000)  # Pressure in Pa
MaterialStream35.SetMassFlow(140.093222222222)  # Mass Flow in kg/s

# Adding Valve: VALV_d4790127_e770_4a80_beb9_eb086f2909aa
Valve5 = sim.AddObject(ObjectType.Valve, 2672, 1062, "VALV-201")
Valve5 = Valve5.GetAsObject()

# Adding MaterialStream: MAT_d9838e4f_0ee2_4eb6_b9bb_0198ffa83dc8
MaterialStream36 = sim.AddObject(ObjectType.MaterialStream, 2606, 1062, "P-9")
MaterialStream36 = MaterialStream36.GetAsObject()
MaterialStream36.SetTemperature(231.299262149381)  # Temperature in K
MaterialStream36.SetPressure(400000)  # Pressure in Pa
MaterialStream36.SetMassFlow(247.223333333333)  # Mass Flow in kg/s

# Adding Heater: AQ_8d82b2ec_4833_4038_9861_54e66d716e08
Heater5 = sim.AddObject(ObjectType.Heater, 2399, 1144, "HEAT-088")
Heater5 = Heater5.GetAsObject()

# Adding MaterialStream: MAT_c753df79_dcdf_4736_8c64_201eb5d7230c
MaterialStream37 = sim.AddObject(ObjectType.MaterialStream, 2338, 949, "P-14")
MaterialStream37 = MaterialStream37.GetAsObject()
MaterialStream37.SetTemperature(273.341515)  # Temperature in K
MaterialStream37.SetPressure(375000)  # Pressure in Pa
MaterialStream37.SetMassFlow(247.223333333333)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_ff30e4b9_b1ac_497d_8b45_8ed8f4c5465e
CapeOpenUO4 = sim.AddObject(ObjectType.CapeOpenUO, 2543, 1155, "COUO-090")
CapeOpenUO4 = CapeOpenUO4.GetAsObject()

# Adding EnergyStream: EN_c656a7c6_82ce_467e_bb66_7094341b1894
EnergyStream19 = sim.AddObject(ObjectType.EnergyStream, 2611, 1107, "E4-3")
EnergyStream19 = EnergyStream19.GetAsObject()

# Adding Cooler: RESF_3cf952e3_fe78_43c1_bd74_bf561e7a0473
Cooler12 = sim.AddObject(ObjectType.Cooler, 2903, 1207, "COOL-092")
Cooler12 = Cooler12.GetAsObject()

# Adding MaterialStream: MAT_7dee9efc_000a_48c1_894a_f04fc7d62420
MaterialStream38 = sim.AddObject(ObjectType.MaterialStream, 3281, 1259, "P-10")
MaterialStream38 = MaterialStream38.GetAsObject()
MaterialStream38.SetTemperature(210.16)  # Temperature in K
MaterialStream38.SetPressure(2175000)  # Pressure in Pa
MaterialStream38.SetMassFlow(140.093222222222)  # Mass Flow in kg/s

# Adding EnergyStream: EN_72dec327_6adb_47b7_a9d1_f905ae915495
EnergyStream20 = sim.AddObject(ObjectType.EnergyStream, 2944, 1247, "E5-2")
EnergyStream20 = EnergyStream20.GetAsObject()

# Adding Valve: VALV_37a8ebc0_8489_4eb6_8772_6ecf24b44893
Valve6 = sim.AddObject(ObjectType.Valve, 3371, 1227, "VALV-095")
Valve6 = Valve6.GetAsObject()

# Adding MaterialStream: MAT_c3b0c418_0a83_4a03_8b87_289aa44f1b80
MaterialStream39 = sim.AddObject(ObjectType.MaterialStream, 3214, 1116, "P-11")
MaterialStream39 = MaterialStream39.GetAsObject()
MaterialStream39.SetTemperature(208.576294170564)  # Temperature in K
MaterialStream39.SetPressure(170000)  # Pressure in Pa
MaterialStream39.SetMassFlow(140.093222222222)  # Mass Flow in kg/s

# Adding Heater: AQ_f45efb9d_5d09_4759_926c_89d211dc63b9
Heater6 = sim.AddObject(ObjectType.Heater, 2906, 1157, "HEAT-097")
Heater6 = Heater6.GetAsObject()

# Adding MaterialStream: MAT_c691c84d_d19e_4975_afba_7a537f96b2ba
MaterialStream40 = sim.AddObject(ObjectType.MaterialStream, 2857, 875, "P-12")
MaterialStream40 = MaterialStream40.GetAsObject()
MaterialStream40.SetTemperature(232.2956)  # Temperature in K
MaterialStream40.SetPressure(145000)  # Pressure in Pa
MaterialStream40.SetMassFlow(140.093222222222)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_c70fd6a3_cc31_450d_bec6_d50cc3db8035
CapeOpenUO5 = sim.AddObject(ObjectType.CapeOpenUO, 3197, 1182, "THERMAL ENERGY MIXER")
CapeOpenUO5 = CapeOpenUO5.GetAsObject()

# Adding EnergyStream: EN_b4689774_8244_48be_9377_8f8daa6d38ae
EnergyStream21 = sim.AddObject(ObjectType.EnergyStream, 3092, 1160, "E5-3")
EnergyStream21 = EnergyStream21.GetAsObject()

# Adding Compressor: COMP_7acb562d_c62a_48a4_a96d_24f5dd45d421
Compressor3 = sim.AddObject(ObjectType.Compressor, 2734, 871, "K-201")
Compressor3 = Compressor3.GetAsObject()

# Adding MaterialStream: MAT_9928cd75_a616_4dce_9a78_e09eb8d68689
MaterialStream41 = sim.AddObject(ObjectType.MaterialStream, 2428, 875, "P-13")
MaterialStream41 = MaterialStream41.GetAsObject()
MaterialStream41.SetTemperature(276.220741472124)  # Temperature in K
MaterialStream41.SetPressure(375000)  # Pressure in Pa
MaterialStream41.SetMassFlow(140.093222222222)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5f9d62a0_dbba_4a68_9ff1_e12a98080f78
EnergyStream22 = sim.AddObject(ObjectType.EnergyStream, 2777, 901, "ESTR-103")
EnergyStream22 = EnergyStream22.GetAsObject()

# Adding NodeIn: MIST_90fe77b1_6318_49d0_bd4d_0907f127f489
Mixer2 = sim.AddObject(ObjectType.NodeIn, 2306, 876, "MIX-201")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MAT_abf8de12_ba44_41a5_8e21_bf150b48fb81
MaterialStream42 = sim.AddObject(ObjectType.MaterialStream, 2231, 882, "P-15")
MaterialStream42 = MaterialStream42.GetAsObject()
MaterialStream42.SetTemperature(274.385161425463)  # Temperature in K
MaterialStream42.SetPressure(375000)  # Pressure in Pa
MaterialStream42.SetMassFlow(387.316555555556)  # Mass Flow in kg/s

# Adding Compressor: COMP_47aebd01_76be_443a_9a22_9a25b63fbccd
Compressor4 = sim.AddObject(ObjectType.Compressor, 2130, 883, "K-202")
Compressor4 = Compressor4.GetAsObject()

# Adding MaterialStream: MAT_097f1b91_bf2b_4fc6_9c43_5be3c47ce921
MaterialStream43 = sim.AddObject(ObjectType.MaterialStream, 2057, 889, "P-16")
MaterialStream43 = MaterialStream43.GetAsObject()
MaterialStream43.SetTemperature(311.383078564362)  # Temperature in K
MaterialStream43.SetPressure(793000)  # Pressure in Pa
MaterialStream43.SetMassFlow(387.316555555556)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5f02056b_81ec_40a7_81a8_f3d793cb34ea
EnergyStream23 = sim.AddObject(ObjectType.EnergyStream, 2173, 913, "ESTR-108")
EnergyStream23 = EnergyStream23.GetAsObject()

# Adding Cooler: RESF_8f776ea7_5d7b_46bf_a9af_fb2700bc38f1
Cooler13 = sim.AddObject(ObjectType.Cooler, 1984, 885, "COOL-201")
Cooler13 = Cooler13.GetAsObject()

# Adding MaterialStream: MAT_46819ac2_be4a_45e5_bbb1_5f4fe3b67c38
MaterialStream44 = sim.AddObject(ObjectType.MaterialStream, 1893, 870, "P-17")
MaterialStream44 = MaterialStream44.GetAsObject()
MaterialStream44.SetTemperature(303.15)  # Temperature in K
MaterialStream44.SetPressure(783000)  # Pressure in Pa
MaterialStream44.SetMassFlow(387.316555555556)  # Mass Flow in kg/s

# Adding EnergyStream: EN_048f0a37_491b_46fb_a901_930b65e94c9e
EnergyStream24 = sim.AddObject(ObjectType.EnergyStream, 2027, 915, "ESTR-111")
EnergyStream24 = EnergyStream24.GetAsObject()

# Adding NodeIn: MIST_b607abe0_729f_4c8a_a645_f62fb7e12894
Mixer3 = sim.AddObject(ObjectType.NodeIn, 1797, 885, "MIX-200")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_8b01f5f3_3a92_43d9_a681_9c676a887ddd
MaterialStream45 = sim.AddObject(ObjectType.MaterialStream, 1713, 886, "P-19")
MaterialStream45 = MaterialStream45.GetAsObject()
MaterialStream45.SetTemperature(301.199352598108)  # Temperature in K
MaterialStream45.SetPressure(783000)  # Pressure in Pa
MaterialStream45.SetMassFlow(906.485555555556)  # Mass Flow in kg/s

# Adding Compressor: COMP_2c4857ab_c954_4ec2_aa1e_4f77c699cbad
Compressor5 = sim.AddObject(ObjectType.Compressor, 1620, 912, "K-200")
Compressor5 = Compressor5.GetAsObject()

# Adding MaterialStream: MAT_b64f68dc_8547_4190_beb6_617934340ddf
MaterialStream46 = sim.AddObject(ObjectType.MaterialStream, 1631, 987, "MSTR-115")
MaterialStream46 = MaterialStream46.GetAsObject()
MaterialStream46.SetTemperature(360.653905984716)  # Temperature in K
MaterialStream46.SetPressure(2260000)  # Pressure in Pa
MaterialStream46.SetMassFlow(906.485555555556)  # Mass Flow in kg/s

# Adding EnergyStream: EN_330882bf_c4ed_4fbb_8153_274d969ef8d7
EnergyStream25 = sim.AddObject(ObjectType.EnergyStream, 1607, 853, "ESTR-116")
EnergyStream25 = EnergyStream25.GetAsObject()

# Adding OT_Recycle: REC_0a18a5f9_13f0_492c_ac4d_1bec2b1a26f7
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1631, 1053, "REC-117")
Recycle2 = Recycle2.GetAsObject()

# Adding MaterialStream: MAT_1132bc4c_dffd_4286_af04_c9ab172477bf
MaterialStream47 = sim.AddObject(ObjectType.MaterialStream, 1634, 1116, "P-20")
MaterialStream47 = MaterialStream47.GetAsObject()
MaterialStream47.SetTemperature(360.653905984716)  # Temperature in K
MaterialStream47.SetPressure(2260000)  # Pressure in Pa
MaterialStream47.SetMassFlow(906.485555555556)  # Mass Flow in kg/s

# Adding Cooler: RESF_e00f17c1_1d25_4f6e_8e5e_d668aeb4148e
Cooler14 = sim.AddObject(ObjectType.Cooler, 1667, 1165, "COOL-200")
Cooler14 = Cooler14.GetAsObject()

# Adding MaterialStream: MAT_cd469c78_655e_496b_926f_b2c8fc7407e5
MaterialStream48 = sim.AddObject(ObjectType.MaterialStream, 1722, 1177, "P-1")
MaterialStream48 = MaterialStream48.GetAsObject()
MaterialStream48.SetTemperature(303.15)  # Temperature in K
MaterialStream48.SetPressure(2250000)  # Pressure in Pa
MaterialStream48.SetMassFlow(906.485555555556)  # Mass Flow in kg/s

# Adding EnergyStream: EN_94c6619c_cec2_469e_a843_e6b83ec5b141
EnergyStream26 = sim.AddObject(ObjectType.EnergyStream, 1709, 1220, "ESTR-121")
EnergyStream26 = EnergyStream26.GetAsObject()

sim.ConnectObjects(MaterialStream44.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream44 to Mixer3
sim.ConnectObjects(Cooler8.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Cooler8 to MaterialStream19
sim.ConnectObjects(Cooler13.GraphicObject, EnergyStream24.GraphicObject, -1, -1)  # Cooler13 to EnergyStream24
sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream35.GraphicObject, -1, -1)  # Splitter2 to MaterialStream35
# sim.ConnectObjects(EnergyStream9.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # EnergyStream9 to CapeOpenUO5
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Valve1 to MaterialStream2
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # Cooler2 to EnergyStream3
sim.ConnectObjects(MaterialStream29.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream29 to Compressor2
sim.ConnectObjects(MaterialStream20.GraphicObject, Cooler8.GraphicObject, -1, -1)  # MaterialStream20 to Cooler8
sim.ConnectObjects(Cooler3.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler3 to EnergyStream1
sim.ConnectObjects(MaterialStream39.GraphicObject, Heater6.GraphicObject, -1, -1)  # MaterialStream39 to Heater6
sim.ConnectObjects(MaterialStream32.GraphicObject, Splitter2.GraphicObject, -1, -1)  # MaterialStream32 to Splitter2
sim.ConnectObjects(MaterialStream34.GraphicObject, Valve5.GraphicObject, -1, -1)  # MaterialStream34 to Valve5
sim.ConnectObjects(Cooler8.GraphicObject, EnergyStream11.GraphicObject, -1, -1)  # Cooler8 to EnergyStream11
sim.ConnectObjects(MaterialStream4.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream4 to Valve1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream30.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream30
sim.ConnectObjects(Cooler12.GraphicObject, EnergyStream20.GraphicObject, -1, -1)  # Cooler12 to EnergyStream20
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, EnergyStream4.GraphicObject, -1, -1)  # CapeOpenUO2 to EnergyStream4
sim.ConnectObjects(EnergyStream15.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream15 to Compressor2
sim.ConnectObjects(MaterialStream18.GraphicObject, Cooler6.GraphicObject, -1, -1)  # MaterialStream18 to Cooler6
sim.ConnectObjects(Expander1.GraphicObject, MaterialStream27.GraphicObject, -1, -1)  # Expander1 to MaterialStream27
sim.ConnectObjects(Compressor4.GraphicObject, MaterialStream43.GraphicObject, -1, -1)  # Compressor4 to MaterialStream43
sim.ConnectObjects(Cooler3.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Cooler3 to MaterialStream10
sim.ConnectObjects(Cooler7.GraphicObject, EnergyStream10.GraphicObject, -1, -1)  # Cooler7 to EnergyStream10
# sim.ConnectObjects(EnergyStream3.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # EnergyStream3 to CapeOpenUO1
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # Cooler2 to MaterialStream5
sim.ConnectObjects(MaterialStream36.GraphicObject, Heater5.GraphicObject, -1, -1)  # MaterialStream36 to Heater5
# sim.ConnectObjects(EnergyStream10.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # EnergyStream10 to CapeOpenUO4
sim.ConnectObjects(MaterialStream27.GraphicObject, Valve4.GraphicObject, -1, -1)  # MaterialStream27 to Valve4
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # Cooler1 to EnergyStream5
sim.ConnectObjects(EnergyStream6.GraphicObject, Heater2.GraphicObject, -1, -1)  # EnergyStream6 to Heater2
sim.ConnectObjects(MaterialStream14.GraphicObject, Cooler4.GraphicObject, -1, -1)  # MaterialStream14 to Cooler4
sim.ConnectObjects(Valve4.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # Valve4 to MaterialStream26
sim.ConnectObjects(Cooler11.GraphicObject, MaterialStream32.GraphicObject, -1, -1)  # Cooler11 to MaterialStream32
sim.ConnectObjects(Splitter2.GraphicObject, MaterialStream34.GraphicObject, -1, -1)  # Splitter2 to MaterialStream34
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Cooler1 to MaterialStream1
sim.ConnectObjects(MaterialStream12.GraphicObject, Heater2.GraphicObject, -1, -1)  # MaterialStream12 to Heater2
# sim.ConnectObjects(EnergyStream20.GraphicObject, CapeOpenUO5.GraphicObject, -1, -1)  # EnergyStream20 to CapeOpenUO5
sim.ConnectObjects(Valve3.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Valve3 to MaterialStream12
sim.ConnectObjects(Cooler14.GraphicObject, EnergyStream26.GraphicObject, -1, -1)  # Cooler14 to EnergyStream26
sim.ConnectObjects(MaterialStream38.GraphicObject, Valve6.GraphicObject, -1, -1)  # MaterialStream38 to Valve6
sim.ConnectObjects(EnergyStream25.GraphicObject, Compressor5.GraphicObject, -1, -1)  # EnergyStream25 to Compressor5
sim.ConnectObjects(MaterialStream31.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream31 to HeatExchanger1
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream47.GraphicObject, -1, -1)  # Recycle2 to MaterialStream47
sim.ConnectObjects(Heater2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Heater2 to MaterialStream11
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Recycle1 to MaterialStream6
sim.ConnectObjects(Expander1.GraphicObject, EnergyStream16.GraphicObject, -1, -1)  # Expander1 to EnergyStream16
sim.ConnectObjects(MaterialStream17.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream17 to Vessel1
sim.ConnectObjects(Compressor5.GraphicObject, MaterialStream46.GraphicObject, -1, -1)  # Compressor5 to MaterialStream46
sim.ConnectObjects(Cooler6.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # Cooler6 to EnergyStream9
sim.ConnectObjects(MaterialStream3.GraphicObject, Cooler11.GraphicObject, -1, -1)  # MaterialStream3 to Cooler11
# sim.ConnectObjects(CapeOpenUO5.GraphicObject, EnergyStream21.GraphicObject, -1, -1)  # CapeOpenUO5 to EnergyStream21
sim.ConnectObjects(MaterialStream43.GraphicObject, Cooler13.GraphicObject, -1, -1)  # MaterialStream43 to Cooler13
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Vessel2 to MaterialStream25
sim.ConnectObjects(Cooler4.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Cooler4 to MaterialStream13
sim.ConnectObjects(MaterialStream6.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream6 to HeatExchanger1
sim.ConnectObjects(EnergyStream13.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream13 to Compressor1
sim.ConnectObjects(MaterialStream28.GraphicObject, Expander1.GraphicObject, -1, -1)  # MaterialStream28 to Expander1
sim.ConnectObjects(MaterialStream15.GraphicObject, Cooler3.GraphicObject, -1, -1)  # MaterialStream15 to Cooler3
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Vessel1 to MaterialStream15
sim.ConnectObjects(EnergyStream22.GraphicObject, Compressor3.GraphicObject, -1, -1)  # EnergyStream22 to Compressor3
sim.ConnectObjects(Cooler10.GraphicObject, MaterialStream28.GraphicObject, -1, -1)  # Cooler10 to MaterialStream28
# sim.ConnectObjects(EnergyStream8.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # EnergyStream8 to CapeOpenUO2
sim.ConnectObjects(Cooler6.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Cooler6 to MaterialStream17
sim.ConnectObjects(MaterialStream1.GraphicObject, Cooler10.GraphicObject, -1, -1)  # MaterialStream1 to Cooler10
sim.ConnectObjects(MaterialStream19.GraphicObject, Cooler7.GraphicObject, -1, -1)  # MaterialStream19 to Cooler7
sim.ConnectObjects(EnergyStream19.GraphicObject, Heater5.GraphicObject, -1, -1)  # EnergyStream19 to Heater5
sim.ConnectObjects(Cooler5.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Cooler5 to MaterialStream14
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Vessel1 to MaterialStream16
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Splitter1 to MaterialStream4
sim.ConnectObjects(EnergyStream23.GraphicObject, Compressor4.GraphicObject, -1, -1)  # EnergyStream23 to Compressor4
sim.ConnectObjects(MaterialStream40.GraphicObject, Compressor3.GraphicObject, -1, -1)  # MaterialStream40 to Compressor3
sim.ConnectObjects(Cooler14.GraphicObject, MaterialStream48.GraphicObject, -1, -1)  # Cooler14 to MaterialStream48
sim.ConnectObjects(Heater5.GraphicObject, MaterialStream37.GraphicObject, -1, -1)  # Heater5 to MaterialStream37
# sim.ConnectObjects(CapeOpenUO3.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # CapeOpenUO3 to EnergyStream6
sim.ConnectObjects(MaterialStream10.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream10 to Valve2
# sim.ConnectObjects(CapeOpenUO4.GraphicObject, EnergyStream19.GraphicObject, -1, -1)  # CapeOpenUO4 to EnergyStream19
sim.ConnectObjects(EnergyStream4.GraphicObject, Heater1.GraphicObject, -1, -1)  # EnergyStream4 to Heater1
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream11 to Mixer1
sim.ConnectObjects(Cooler13.GraphicObject, MaterialStream44.GraphicObject, -1, -1)  # Cooler13 to MaterialStream44
sim.ConnectObjects(MaterialStream33.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream33 to Mixer3
sim.ConnectObjects(Cooler10.GraphicObject, EnergyStream17.GraphicObject, -1, -1)  # Cooler10 to EnergyStream17
# sim.ConnectObjects(CapeOpenUO1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # CapeOpenUO1 to EnergyStream2
sim.ConnectObjects(MaterialStream46.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream46 to Recycle2
sim.ConnectObjects(MaterialStream21.GraphicObject, Heater3.GraphicObject, -1, -1)  # MaterialStream21 to Heater3
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Splitter1 to MaterialStream3
sim.ConnectObjects(Cooler9.GraphicObject, EnergyStream14.GraphicObject, -1, -1)  # Cooler9 to EnergyStream14
sim.ConnectObjects(Cooler9.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Cooler9 to MaterialStream22
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream42.GraphicObject, -1, -1)  # Mixer2 to MaterialStream42
# sim.ConnectObjects(EnergyStream18.GraphicObject, CapeOpenUO4.GraphicObject, -1, -1)  # EnergyStream18 to CapeOpenUO4
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Valve2 to MaterialStream9
sim.ConnectObjects(Vessel2.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # Vessel2 to MaterialStream24
sim.ConnectObjects(Valve5.GraphicObject, MaterialStream36.GraphicObject, -1, -1)  # Valve5 to MaterialStream36
sim.ConnectObjects(MaterialStream37.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream37 to Mixer2
sim.ConnectObjects(MaterialStream42.GraphicObject, Compressor4.GraphicObject, -1, -1)  # MaterialStream42 to Compressor4
sim.ConnectObjects(Cooler4.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # Cooler4 to EnergyStream7
sim.ConnectObjects(MaterialStream5.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream5 to Splitter1
sim.ConnectObjects(Cooler11.GraphicObject, EnergyStream18.GraphicObject, -1, -1)  # Cooler11 to EnergyStream18
sim.ConnectObjects(Heater6.GraphicObject, MaterialStream40.GraphicObject, -1, -1)  # Heater6 to MaterialStream40
sim.ConnectObjects(MaterialStream23.GraphicObject, Cooler9.GraphicObject, -1, -1)  # MaterialStream23 to Cooler9
sim.ConnectObjects(Heater1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Heater1 to MaterialStream7
# sim.ConnectObjects(EnergyStream11.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # EnergyStream11 to CapeOpenUO1
sim.ConnectObjects(MaterialStream45.GraphicObject, Compressor5.GraphicObject, -1, -1)  # MaterialStream45 to Compressor5
sim.ConnectObjects(Cooler5.GraphicObject, EnergyStream8.GraphicObject, -1, -1)  # Cooler5 to EnergyStream8
sim.ConnectObjects(MaterialStream26.GraphicObject, Vessel2.GraphicObject, -1, -1)  # MaterialStream26 to Vessel2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream29.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream29
sim.ConnectObjects(Heater3.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Heater3 to MaterialStream20
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Compressor2 to MaterialStream23
# sim.ConnectObjects(EnergyStream17.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # EnergyStream17 to CapeOpenUO3
sim.ConnectObjects(EnergyStream2.GraphicObject, Heater4.GraphicObject, -1, -1)  # EnergyStream2 to Heater4
sim.ConnectObjects(Cooler12.GraphicObject, MaterialStream38.GraphicObject, -1, -1)  # Cooler12 to MaterialStream38
sim.ConnectObjects(MaterialStream13.GraphicObject, Valve3.GraphicObject, -1, -1)  # MaterialStream13 to Valve3
sim.ConnectObjects(Cooler7.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Cooler7 to MaterialStream18
sim.ConnectObjects(MaterialStream41.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream41 to Mixer2
sim.ConnectObjects(MaterialStream22.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream22 to Compressor1
sim.ConnectObjects(MaterialStream48.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream48 to Cooler2
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Compressor1 to MaterialStream21
sim.ConnectObjects(MaterialStream47.GraphicObject, Cooler14.GraphicObject, -1, -1)  # MaterialStream47 to Cooler14
# sim.ConnectObjects(EnergyStream7.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # EnergyStream7 to CapeOpenUO3
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream45.GraphicObject, -1, -1)  # Mixer3 to MaterialStream45
sim.ConnectObjects(MaterialStream35.GraphicObject, Cooler12.GraphicObject, -1, -1)  # MaterialStream35 to Cooler12
sim.ConnectObjects(MaterialStream30.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream30 to Cooler1
sim.ConnectObjects(MaterialStream8.GraphicObject, Heater1.GraphicObject, -1, -1)  # MaterialStream8 to Heater1
sim.ConnectObjects(MaterialStream9.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream9 to Mixer1
# sim.ConnectObjects(EnergyStream5.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # EnergyStream5 to CapeOpenUO2
sim.ConnectObjects(EnergyStream12.GraphicObject, Heater3.GraphicObject, -1, -1)  # EnergyStream12 to Heater3
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Mixer1 to MaterialStream8
sim.ConnectObjects(EnergyStream21.GraphicObject, Heater6.GraphicObject, -1, -1)  # EnergyStream21 to Heater6
sim.ConnectObjects(Valve6.GraphicObject, MaterialStream39.GraphicObject, -1, -1)  # Valve6 to MaterialStream39
sim.ConnectObjects(Compressor3.GraphicObject, MaterialStream41.GraphicObject, -1, -1)  # Compressor3 to MaterialStream41
sim.ConnectObjects(MaterialStream2.GraphicObject, Heater4.GraphicObject, -1, -1)  # MaterialStream2 to Heater4
sim.ConnectObjects(Heater4.GraphicObject, MaterialStream33.GraphicObject, -1, -1)  # Heater4 to MaterialStream33
sim.ConnectObjects(MaterialStream7.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream7 to Recycle1
sim.ConnectObjects(MaterialStream16.GraphicObject, Cooler5.GraphicObject, -1, -1)  # MaterialStream16 to Cooler5
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_48.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_48.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

