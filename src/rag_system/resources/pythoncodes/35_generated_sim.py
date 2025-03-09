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
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)
argon = sim.AvailableCompounds["Argon"]
sim.SelectedCompounds.Add(argon.Name, argon)

# Adding Simulation Objects
# Adding OT_Recycle: REC_da8aa827_0e07_41bf_aba6_993fc15dac02
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2951, 1268, "REC-001")
Recycle1 = Recycle1.GetAsObject()

# Adding EnergyStream: EN_c4263cef_0d3f_4f91_919e_1d5cf0d4d3f8
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 3046, 941, "E-14")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_53ac14c9_084c_4d51_ac3c_768c8b083542
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 3053, 895, "Gas N2")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(298.149997135738)  # Temperature in K
MaterialStream1.SetPressure(110000)  # Pressure in Pa
MaterialStream1.SetMassFlow(13.5024856160804)  # Mass Flow in kg/s

# Adding EnergyStream: EN_2843490d_9b5d_499b_9ef1_c725adf4150c
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 3011, 1373, "E-15")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_a85bbc9d_90ba_485f_9286_c254c8e9dadb
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 3096, 1315, "Gas O2")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(298.15)  # Temperature in K
MaterialStream2.SetPressure(110000)  # Pressure in Pa
MaterialStream2.SetMassFlow(18.0203633545815)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3960fb7c_d23e_46fa_ae10_e65a41118492
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2859, 852, "E-13")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MAT_df4f58b0_b879_499a_afbc_99a67195fae3
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2902, 792, "Waste Gases")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(298.15)  # Temperature in K
MaterialStream3.SetPressure(111956.52173913)  # Pressure in Pa
MaterialStream3.SetMassFlow(68.0802071949841)  # Mass Flow in kg/s

# Adding Cooler: RESF_84acd5b2_536b_483f_96f8_743ec04b2d9f
Cooler1 = sim.AddObject(ObjectType.Cooler, 2988, 1313, "COOL-009")
Cooler1 = Cooler1.GetAsObject()

# Adding Cooler: RESF_c9804401_7fa6_4d22_aa09_4e05bd6758e6
Cooler2 = sim.AddObject(ObjectType.Cooler, 2833, 789, "COOL-007")
Cooler2 = Cooler2.GetAsObject()

# Adding Cooler: RESF_fbeb31ee_5578_4e8b_ae15_7338fad2f206
Cooler3 = sim.AddObject(ObjectType.Cooler, 2959, 893, "COOL-008")
Cooler3 = Cooler3.GetAsObject()

# Adding EnergyStream: EN_322e76dc_5116_4f19_af82_1c562dded643
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 3066, 1197, "E-12")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_cb4e2c31_eb95_47a4_b13a_e85d9a938d7a
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 3060, 1269, "S-28")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(92.1838170332623)  # Temperature in K
MaterialStream4.SetPressure(180000)  # Pressure in Pa
MaterialStream4.SetMassFlow(7.07675760384183)  # Mass Flow in kg/s

# Adding Pump: BB_622b4efc_dce4_430f_a0f9_9032b3e28bcd
Pump1 = sim.AddObject(ObjectType.Pump, 3130, 1239, "PUMP-001")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_9ed88ccb_d02a_4aab_bd4c_fcffa3bac39e
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 3205, 1241, "S-27")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(91.9867693461733)  # Temperature in K
MaterialStream5.SetPressure(130000)  # Pressure in Pa
MaterialStream5.SetMassFlow(7.07675760384183)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_0161b04d_47c0_49b1_a03d_ab8775a7897e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 3256, 973, "Liquid Argon")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(88.9308959816541)  # Temperature in K
MaterialStream6.SetPressure(120000)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.390159466501653)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_2fdd54b0_71a9_4ca1_a8a0_6a3ee677219f
CapeOpenUO1 = sim.AddObject(ObjectType.CapeOpenUO, 2848, 997, "Argon Recovery Column")
CapeOpenUO1 = CapeOpenUO1.GetAsObject()

# Adding MaterialStream: MAT_5b53bdb7_5a03_40ad_96b5_bcfab41119c8
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2917, 1319, "S-24")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(92.8262165653112)  # Temperature in K
MaterialStream7.SetPressure(135000)  # Pressure in Pa
MaterialStream7.SetMassFlow(18.0203633545815)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_03e51f27_ace7_4edb_9be3_f62d53e85c19
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 2899, 898, "S-29")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(78.8188150815445)  # Temperature in K
MaterialStream8.SetPressure(120000)  # Pressure in Pa
MaterialStream8.SetMassFlow(13.5024856160804)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_71a14932_5ed9_47cc_9e8e_eb41cf78fde0
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2748, 789, "S-23")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(80.6615034064793)  # Temperature in K
MaterialStream9.SetPressure(121956.52173913)  # Pressure in Pa
MaterialStream9.SetMassFlow(68.0802071949841)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6462bf61_50ea_43b5_a40e_ebdd9d65f7a9
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2708, 987, "S-22")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(92.1341356915563)  # Temperature in K
MaterialStream10.SetPressure(131739.13043478)  # Pressure in Pa
MaterialStream10.SetMassFlow(7.46691707034348)  # Mass Flow in kg/s

# Adding CapeOpenUO: COUO_ec531ced_658c_4693_9fd0_0b2b06edd875
CapeOpenUO2 = sim.AddObject(ObjectType.CapeOpenUO, 2599, 1045, "Low Pressure Column")
CapeOpenUO2 = CapeOpenUO2.GetAsObject()

# Adding EnergyStream: EN_508d81e8_69a6_488a_90fe_59cceac71cc2
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2329, 1166, "E-11")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_d4520229_6206_4c01_a0ce_edafbc47f8bc
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 2445, 1087, "S-21")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(82.3175692604637)  # Temperature in K
MaterialStream11.SetPressure(132000)  # Pressure in Pa
MaterialStream11.SetMassFlow(51.5175646856764)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_bf0da0cb_2279_4b89_b876_0f997b532054
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 2439, 1037, "S-20")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(82.3179562849539)  # Temperature in K
MaterialStream12.SetPressure(132000)  # Pressure in Pa
MaterialStream12.SetMassFlow(10.2324533962759)  # Mass Flow in kg/s

# Adding Vessel: SEP_db45136f_37ed_4ad2_93dc_ba8464da86db
Vessel1 = sim.AddObject(ObjectType.Vessel, 2346, 1036, "SEP-001")
Vessel1 = Vessel1.GetAsObject()

# Adding MaterialStream: MAT_b15dd2f9_1e74_42ae_9ec4_4315589e5abd
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2285, 1066, "S-19")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(82.3175692604637)  # Temperature in K
MaterialStream13.SetPressure(132000)  # Pressure in Pa
MaterialStream13.SetMassFlow(61.7500308546634)  # Mass Flow in kg/s

# Adding Valve: VALV_806c4b2c_92b1_4674_81d1_4ada1d32d57d
Valve1 = sim.AddObject(ObjectType.Valve, 2183, 1066, "VALV-001")
Valve1 = Valve1.GetAsObject()

# Adding EnergyStream: EN_cdda73d9_1171_456e_b704_5bd831e7493f
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 2155, 1187, "E-09")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_12066148_f41b_412b_8437_fd45fe31f27e
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 2515, 1202, "S-18")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(98.6736642927617)  # Temperature in K
MaterialStream14.SetPressure(130000)  # Pressure in Pa
MaterialStream14.SetMassFlow(15)  # Mass Flow in kg/s

# Adding Expander: TURB_729029d6_5b4d_4ac9_9bb5_0412133f3a03
Expander1 = sim.AddObject(ObjectType.Expander, 2055, 1127, "EXP-001")
Expander1 = Expander1.GetAsObject()

# Adding MaterialStream: MAT_dabd6406_8c25_4df6_9f65_3c135e09cd09
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 2517, 934, "S-17")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(79.5326172949669)  # Temperature in K
MaterialStream15.SetPressure(130000)  # Pressure in Pa
MaterialStream15.SetMassFlow(23.2499691441316)  # Mass Flow in kg/s

# Adding EnergyStream: EN_86e34e3a_eadc_44c0_b5a4_68e6461b8c50
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 1795, 1185, "E-08")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_5c8dfc7f_f92a_4595_adf3_78f7331fee14
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1840, 1133, "S-16")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(105)  # Temperature in K
MaterialStream16.SetPressure(590000)  # Pressure in Pa
MaterialStream16.SetMassFlow(15)  # Mass Flow in kg/s

# Adding Cooler: RESF_30b20b5f_9ff9_41a3_9fd3_2787f52ee8f4
Cooler4 = sim.AddObject(ObjectType.Cooler, 1750, 1130, "COOL-005")
Cooler4 = Cooler4.GetAsObject()

# Adding CapeOpenUO: COUO_6c0a5a9c_afa3_4a3a_9ab0_d3b676bbcf81
CapeOpenUO3 = sim.AddObject(ObjectType.CapeOpenUO, 1896, 899, "High Pressure Column")
CapeOpenUO3 = CapeOpenUO3.GetAsObject()

# Adding MaterialStream: MAT_13f5d677_550b_4293_b1ec_4816d4515a7f
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1132, 749, "Air")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(303.15)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(100)  # Mass Flow in kg/s

# Adding Compressor: COMP_37b5deeb_b9bd_4d84_9e29_b251e766ab74
Compressor1 = sim.AddObject(ObjectType.Compressor, 1199, 747, "COMP-001")
Compressor1 = Compressor1.GetAsObject()

# Adding MaterialStream: MAT_925b2a25_934f_436a_98e9_ff963eee84f3
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1280, 750, "S-02")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(465.744736273632)  # Temperature in K
MaterialStream18.SetPressure(198000)  # Pressure in Pa
MaterialStream18.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_bdaf75e8_7cfb_40d3_9f70_4d0d90dabc2a
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 1131, 791, "E-01")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding Cooler: RESF_0b72fc1f_45ad_40ae_8de8_fb36db04beec
Cooler5 = sim.AddObject(ObjectType.Cooler, 1350, 747, "COOL-001")
Cooler5 = Cooler5.GetAsObject()

# Adding MaterialStream: MAT_d474c780_f581_478d_ad4b_8563010ae267
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1488, 809, "S-03")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(313.15)  # Temperature in K
MaterialStream19.SetPressure(178000)  # Pressure in Pa
MaterialStream19.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_340ce1d9_afd9_4a88_8ef4_123306b94f29
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 1398, 799, "E-02")
EnergyStream9 = EnergyStream9.GetAsObject()

# Adding Compressor: COMP_63a8cf66_b4b1_423a_b4ff_bbd208be075a
Compressor2 = sim.AddObject(ObjectType.Compressor, 1486, 896, "COMP-002")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_af92f465_cd65_4455_bf7a_ae76d18381d3
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1395, 958, "S-04")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(477.006758104021)  # Temperature in K
MaterialStream20.SetPressure(346000)  # Pressure in Pa
MaterialStream20.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_cf62b275_a81a_4898_9c92_6c3eb3104720
EnergyStream10 = sim.AddObject(ObjectType.EnergyStream, 1412, 897, "E-03")
EnergyStream10 = EnergyStream10.GetAsObject()

# Adding Cooler: RESF_c326e409_efe3_4503_884c_ae687b22d7b0
Cooler6 = sim.AddObject(ObjectType.Cooler, 1254, 956, "COOL-002")
Cooler6 = Cooler6.GetAsObject()

# Adding MaterialStream: MAT_6bf8b310_6610_42f8_94dc_3c51f98007cf
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1138, 1009, "S-05")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(313.15)  # Temperature in K
MaterialStream21.SetPressure(326000)  # Pressure in Pa
MaterialStream21.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_5d82e5e4_cd78_4d71_a33d_cb7a46460506
EnergyStream11 = sim.AddObject(ObjectType.EnergyStream, 1345, 896, "E-04")
EnergyStream11 = EnergyStream11.GetAsObject()

# Adding Compressor: COMP_f989825d_d34a_4941_ba56_1d859ba3cfba
Compressor3 = sim.AddObject(ObjectType.Compressor, 1224, 1071, "COMP-003")
Compressor3 = Compressor3.GetAsObject()

# Adding MaterialStream: MAT_b7076611_ca56_438e_a6f7_ec3349b18633
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1314, 1074, "S-06")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(477.483816154077)  # Temperature in K
MaterialStream22.SetPressure(635000)  # Pressure in Pa
MaterialStream22.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_2750fc20_a54f_43c8_bf9b_05ed3aa3a428
EnergyStream12 = sim.AddObject(ObjectType.EnergyStream, 1161, 1120, "E-05")
EnergyStream12 = EnergyStream12.GetAsObject()

# Adding Cooler: RESF_b4c2a2ec_89ab_49db_8075_1ec89f30b320
Cooler7 = sim.AddObject(ObjectType.Cooler, 1397, 1073, "COOL-003")
Cooler7 = Cooler7.GetAsObject()

# Adding MaterialStream: MAT_663df466_43e8_4eb7_a45f_b640e5335ba3
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 1484, 1076, "S-07")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(303.15)  # Temperature in K
MaterialStream23.SetPressure(610000)  # Pressure in Pa
MaterialStream23.SetMassFlow(100)  # Mass Flow in kg/s

# Adding EnergyStream: EN_88a9aca2_0139_4c0c_80b7_464f5e08b559
EnergyStream13 = sim.AddObject(ObjectType.EnergyStream, 1439, 1128, "E-06")
EnergyStream13 = EnergyStream13.GetAsObject()

# Adding NodeOut: DIV_4d804967_410d_42c8_963c_917e12a3bca3
Splitter1 = sim.AddObject(ObjectType.NodeOut, 1561, 1076, "SPLT-01")
Splitter1 = Splitter1.GetAsObject()

# Adding MaterialStream: MAT_41e00eaa_b1d3_4e85_8be2_dc49537c9ec4
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 1691, 1014, "S-08")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(303.15)  # Temperature in K
MaterialStream24.SetPressure(610000)  # Pressure in Pa
MaterialStream24.SetMassFlow(85)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_52b3b5fd_cb67_45a1_b5b3_6e54ab380af6
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 1691, 1133, "S-09")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(303.15)  # Temperature in K
MaterialStream25.SetPressure(610000)  # Pressure in Pa
MaterialStream25.SetMassFlow(15)  # Mass Flow in kg/s

# Adding Cooler: RESF_7e94aace_59d0_4767_914a_a5e01c257f31
Cooler8 = sim.AddObject(ObjectType.Cooler, 1751, 1012, "COOL-004")
Cooler8 = Cooler8.GetAsObject()

# Adding MaterialStream: MAT_e97e70ba_5c5f_40e8_b0f2_2f83b1181872
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 1837, 1015, "S-10")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(99.35)  # Temperature in K
MaterialStream26.SetPressure(570000)  # Pressure in Pa
MaterialStream26.SetMassFlow(85)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3c89673c_b657_4234_a60d_29c10d7bb01f
EnergyStream14 = sim.AddObject(ObjectType.EnergyStream, 1788, 1072, "E-07")
EnergyStream14 = EnergyStream14.GetAsObject()

# Adding MaterialStream: MAT_cb07fd0f_935d_4d9f_941d_4193961f931a
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 2028, 824, "S-11")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(95.4678342311272)  # Temperature in K
MaterialStream27.SetPressure(560000)  # Pressure in Pa
MaterialStream27.SetMassFlow(22.5925028220003)  # Mass Flow in kg/s

# Adding Valve: VALV_9411ccc3_2ed2_4afa_a9f4_5e1abeb5e8d8
Valve2 = sim.AddObject(ObjectType.Valve, 2288, 934, "VALV-01")
Valve2 = Valve2.GetAsObject()

# Adding NodeIn: MIST_a61718b1_7b6c_44ca_92a4_7a46e51161b8
Mixer1 = sim.AddObject(ObjectType.NodeIn, 2166, 834, "MIX-001")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_d29ccf18_9c60_4e88_b621_0c7709f60e08
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 2082, 1066, "S-12")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(98.8210217344594)  # Temperature in K
MaterialStream28.SetPressure(570000)  # Pressure in Pa
MaterialStream28.SetMassFlow(61.7500308546634)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f741692a_8c25_4cdd_a10e_70c490923889
MaterialStream29 = sim.AddObject(ObjectType.MaterialStream, 2223, 940, "S-14")
MaterialStream29 = MaterialStream29.GetAsObject()
MaterialStream29.SetTemperature(95.467837413226)  # Temperature in K
MaterialStream29.SetPressure(560000)  # Pressure in Pa
MaterialStream29.SetMassFlow(23.2499691441316)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6c4a8ddc_05b9_4efd_875c_e4bf080a5009
MaterialStream30 = sim.AddObject(ObjectType.MaterialStream, 2063, 958, "S-13")
MaterialStream30 = MaterialStream30.GetAsObject()
MaterialStream30.SetTemperature(95.4678392792828)  # Temperature in K
MaterialStream30.SetPressure(560000)  # Pressure in Pa
MaterialStream30.SetMassFlow(0.65746632213124)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_16e22b81_5e74_4387_8caf_a44f3501c5b1
MaterialStream31 = sim.AddObject(ObjectType.MaterialStream, 2830, 1268, "S-25")
MaterialStream31 = MaterialStream31.GetAsObject()
MaterialStream31.SetTemperature(92.1234552765867)  # Temperature in K
MaterialStream31.SetPressure(180000)  # Pressure in Pa
MaterialStream31.SetMassFlow(7.06998592616458)  # Mass Flow in kg/s

sim.ConnectObjects(Cooler8.GraphicObject, EnergyStream14.GraphicObject, -1, -1)  # Cooler8 to EnergyStream14
sim.ConnectObjects(MaterialStream17.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream17 to Compressor1
sim.ConnectObjects(Cooler6.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Cooler6 to MaterialStream21
sim.ConnectObjects(MaterialStream28.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream28 to Valve1
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream6
sim.ConnectObjects(MaterialStream14.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream14 to CapeOpenUO2
sim.ConnectObjects(MaterialStream25.GraphicObject, Cooler4.GraphicObject, -1, -1)  # MaterialStream25 to Cooler4
sim.ConnectObjects(MaterialStream23.GraphicObject, Splitter1.GraphicObject, -1, -1)  # MaterialStream23 to Splitter1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream9
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Vessel1 to MaterialStream11
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream28.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream28
sim.ConnectObjects(Cooler7.GraphicObject, EnergyStream13.GraphicObject, -1, -1)  # Cooler7 to EnergyStream13
sim.ConnectObjects(EnergyStream5.GraphicObject, Vessel1.GraphicObject, -1, -1)  # EnergyStream5 to Vessel1
sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream10
sim.ConnectObjects(MaterialStream18.GraphicObject, Cooler5.GraphicObject, -1, -1)  # MaterialStream18 to Cooler5
sim.ConnectObjects(MaterialStream9.GraphicObject, Cooler2.GraphicObject, -1, -1)  # MaterialStream9 to Cooler2
sim.ConnectObjects(EnergyStream10.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream10 to Compressor2
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # Splitter1 to MaterialStream24
sim.ConnectObjects(MaterialStream30.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream30 to Mixer1
# sim.ConnectObjects(MaterialStream15.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream15 to CapeOpenUO2
sim.ConnectObjects(MaterialStream20.GraphicObject, Cooler6.GraphicObject, -1, -1)  # MaterialStream20 to Cooler6
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # Compressor1 to MaterialStream18
sim.ConnectObjects(Cooler3.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Cooler3 to MaterialStream1
sim.ConnectObjects(Valve2.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Valve2 to MaterialStream15
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream8
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Compressor2 to MaterialStream20
sim.ConnectObjects(MaterialStream10.GraphicObject, CapeOpenUO1.GraphicObject, -1, -1)  # MaterialStream10 to CapeOpenUO1
sim.ConnectObjects(Cooler5.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # Cooler5 to MaterialStream19
sim.ConnectObjects(Cooler5.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # Cooler5 to EnergyStream9
sim.ConnectObjects(EnergyStream8.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream8 to Compressor1
sim.ConnectObjects(Cooler4.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Cooler4 to MaterialStream16
sim.ConnectObjects(Cooler8.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # Cooler8 to MaterialStream26
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream31.GraphicObject, -1, -1)  # Recycle1 to MaterialStream31
# sim.ConnectObjects(MaterialStream11.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream11 to CapeOpenUO2
sim.ConnectObjects(MaterialStream7.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream7 to Cooler1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream29.GraphicObject, -1, -1)  # Mixer1 to MaterialStream29
sim.ConnectObjects(EnergyStream12.GraphicObject, Compressor3.GraphicObject, -1, -1)  # EnergyStream12 to Compressor3
sim.ConnectObjects(MaterialStream24.GraphicObject, Cooler8.GraphicObject, -1, -1)  # MaterialStream24 to Cooler8
sim.ConnectObjects(MaterialStream29.GraphicObject, Valve2.GraphicObject, -1, -1)  # MaterialStream29 to Valve2
sim.ConnectObjects(MaterialStream27.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream27 to Mixer1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Vessel1 to MaterialStream12
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream4 to Recycle1
sim.ConnectObjects(MaterialStream21.GraphicObject, Compressor3.GraphicObject, -1, -1)  # MaterialStream21 to Compressor3
sim.ConnectObjects(MaterialStream16.GraphicObject, Expander1.GraphicObject, -1, -1)  # MaterialStream16 to Expander1
sim.ConnectObjects(MaterialStream22.GraphicObject, Cooler7.GraphicObject, -1, -1)  # MaterialStream22 to Cooler7
sim.ConnectObjects(Expander1.GraphicObject, EnergyStream6.GraphicObject, -1, -1)  # Expander1 to EnergyStream6
sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream27.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream27
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Pump1 to MaterialStream4
sim.ConnectObjects(MaterialStream19.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream19 to Compressor2
sim.ConnectObjects(Cooler2.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # Cooler2 to EnergyStream3
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Valve1 to MaterialStream13
sim.ConnectObjects(Cooler7.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Cooler7 to MaterialStream23
sim.ConnectObjects(Splitter1.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Splitter1 to MaterialStream25
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # Cooler1 to EnergyStream2
sim.ConnectObjects(Cooler6.GraphicObject, EnergyStream11.GraphicObject, -1, -1)  # Cooler6 to EnergyStream11
sim.ConnectObjects(Compressor3.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Compressor3 to MaterialStream22
sim.ConnectObjects(MaterialStream8.GraphicObject, Cooler3.GraphicObject, -1, -1)  # MaterialStream8 to Cooler3
sim.ConnectObjects(Cooler4.GraphicObject, EnergyStream7.GraphicObject, -1, -1)  # Cooler4 to EnergyStream7
sim.ConnectObjects(EnergyStream4.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream4 to Pump1
# sim.ConnectObjects(MaterialStream12.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream12 to CapeOpenUO2
# sim.ConnectObjects(CapeOpenUO2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # CapeOpenUO2 to MaterialStream7
sim.ConnectObjects(Expander1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Expander1 to MaterialStream14
sim.ConnectObjects(CapeOpenUO1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # CapeOpenUO1 to MaterialStream5
sim.ConnectObjects(Cooler3.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # Cooler3 to EnergyStream1
sim.ConnectObjects(MaterialStream5.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream5 to Pump1
# sim.ConnectObjects(CapeOpenUO3.GraphicObject, MaterialStream30.GraphicObject, -1, -1)  # CapeOpenUO3 to MaterialStream30
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Cooler1 to MaterialStream2
# sim.ConnectObjects(MaterialStream31.GraphicObject, CapeOpenUO2.GraphicObject, -1, -1)  # MaterialStream31 to CapeOpenUO2
sim.ConnectObjects(MaterialStream13.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream13 to Vessel1
sim.ConnectObjects(MaterialStream26.GraphicObject, CapeOpenUO3.GraphicObject, -1, -1)  # MaterialStream26 to CapeOpenUO3
sim.ConnectObjects(Cooler2.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Cooler2 to MaterialStream3
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_35.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_35.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

