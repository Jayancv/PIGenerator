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
maleic_anhydride = sim.AvailableCompounds["Maleic anhydride"]
sim.SelectedCompounds.Add(maleic_anhydride.Name, maleic_anhydride)
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
# dibutyl_phthalate = sim.AvailableCompounds["dibutyl phthalate"]
# sim.SelectedCompounds.Add(dibutyl_phthalate.Name, dibutyl_phthalate)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
sodium_nitrate = sim.AvailableCompounds["Sodium Nitrate"]
sim.SelectedCompounds.Add(sodium_nitrate.Name, sodium_nitrate)
benzene = sim.AvailableCompounds["Benzene"]
sim.SelectedCompounds.Add(benzene.Name, benzene)
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)

# Adding Simulation Objects
# Adding EnergyStream: ES_1c7e8071_fa06_4aa5_9f88_6c5c62e7b126
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 1722, 1177, "ES-coolant")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding HeaterCooler: CL_5beb90aa_3dd3_4608_9d09_78a01add7fd4
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 1747, 1085, "CL-coolant")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MS_9f0c30dd_51de_40ad_831e_5b87c30b4f3b
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1893, 1152, "coolant")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(692)  # Temperature in K
MaterialStream1.SetPressure(98675)  # Pressure in Pa
MaterialStream1.SetMassFlow(108.77514629375)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_ee96ba04_6230_43df_8b6e_4f0bb42f4e01
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1374, 1233, "REC-045")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MS_d9daaa7c_85e8_42cb_ac47_222f8002145a
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1486, 951, "MS-044")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(700.163812148158)  # Temperature in K
MaterialStream2.SetPressure(200000)  # Pressure in Pa
MaterialStream2.SetMassFlow(132.076252)  # Mass Flow in kg/s

# Adding NodeIn: MIX_9c6c738e_b6ea_40f3_9be9_7985ee84bd32
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1412, 934, "MIX-043")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MS_5934dbac_f407_4e1e_83e4_a2664843d983
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 1351, 982, "recycle coolant")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(692.000511590506)  # Temperature in K
MaterialStream3.SetPressure(200000)  # Pressure in Pa
MaterialStream3.SetMassFlow(108.8)  # Mass Flow in kg/s

# Adding MaterialStream: MS_5ecee6df_51cc_460a_9537_e124229d59e5
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2319, 1128, "dibutyl recycle")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(601.735564429047)  # Temperature in K
MaterialStream4.SetPressure(82000)  # Pressure in Pa
MaterialStream4.SetMassFlow(38.6558700080216)  # Mass Flow in kg/s

# Adding MaterialStream: MS_8d640640_19dc_4096_ae61_bcacee57ab72
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1672, 558, "dibutyl_pthalate fresh")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(603.15)  # Temperature in K
MaterialStream5.SetPressure(100000)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.00773172852)  # Mass Flow in kg/s

# Adding EnergyStream: ES_59417e7b_a6f0_446b_a0d9_c7dc66b854c2
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2101, 823, "ES-waste seperator")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MS_88789395_ed77_414a_aab0_b01ce9c7e67e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2155, 673, "waste gases")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(463.403983449729)  # Temperature in K
MaterialStream6.SetPressure(82000)  # Pressure in Pa
MaterialStream6.SetMassFlow(22.3188682195368)  # Mass Flow in kg/s

# Adding MaterialStream: MS_64ba2b5c_081d_4182_915f_03c05cb92cbb
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1604, 1090, " hot coolant outlet")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(849.096212830416)  # Temperature in K
MaterialStream7.SetPressure(98675)  # Pressure in Pa
MaterialStream7.SetMassFlow(108.77514629375)  # Mass Flow in kg/s

# Adding MaterialStream: MS_81ab41e4_7a5d_4b17_ac14_064a40dd3a32
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1235, 963, "lps_vapouriser_CLONE")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(416.762532998383)  # Temperature in K
MaterialStream8.SetPressure(400000)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.233655)  # Mass Flow in kg/s

# Adding MaterialStream: MS_603a9565_4f3b_4d18_9065_dcf8dc327c0d
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1103, 877, "benzene_2")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(303.265039773833)  # Temperature in K
MaterialStream9.SetPressure(280000)  # Pressure in Pa
MaterialStream9.SetMassFlow(0.9178395)  # Mass Flow in kg/s

# Adding HeatExchanger: HX_42e98597_e94d_4e11_8e74_a4bcf845d561
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1191, 867, "HX-028")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding EnergyStream: ES_67046f70_b4a1_4a8d_8c3f_5891b80afc1d
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 939, 967, "ES_pump01")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding MaterialStream: MS_0fe59ff8_4b58_4828_a7b0_e5f64f39d869
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1986, 982, "maleic anhyride_raw")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(463.403983449729)  # Temperature in K
MaterialStream10.SetPressure(82000)  # Pressure in Pa
MaterialStream10.SetMassFlow(39.6458416624)  # Mass Flow in kg/s

# Adding MaterialStream: MS_2924df7a_3d50_4223_8ce3_e61da9746b25
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1108, 707, "air")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(303.151741516512)  # Temperature in K
MaterialStream11.SetPressure(101325)  # Pressure in Pa
MaterialStream11.SetMassFlow(22.3584125)  # Mass Flow in kg/s

# Adding NodeIn: MIX_0afff2b2_9669_4cae_bb1b_d49784d74f8f
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1029, 702, "air pure")
Mixer2 = Mixer2.GetAsObject()

# Adding MaterialStream: MS_df1441ac_5a96_48f6_b757_3d162b81477c
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 947, 768, "nitrogen")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(303.15)  # Temperature in K
MaterialStream12.SetPressure(101325)  # Pressure in Pa
MaterialStream12.SetMassFlow(17.158575)  # Mass Flow in kg/s

# Adding MaterialStream: MS_2ad36d14_f13c_438e_887a_d58e60f26572
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 946, 663, "oxygen")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(303.15)  # Temperature in K
MaterialStream13.SetPressure(101325)  # Pressure in Pa
MaterialStream13.SetMassFlow(5.1998375)  # Mass Flow in kg/s

# Adding Pump: PUMP_fdacf378_d8b9_454f_a079_b83a29d3eb65
Pump1 = sim.AddObject(ObjectType.Pump, 1004, 887, "PUMP-001")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MS_c229021f_5973_473a_8073_758181f89802
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 929, 891, "benzene")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(303.15)  # Temperature in K
MaterialStream14.SetPressure(101325)  # Pressure in Pa
MaterialStream14.SetMassFlow(0.9178395)  # Mass Flow in kg/s

# Adding MaterialStream: MS_9c9fddf4_97c7_40ce_b4f6_beec551924b2
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1289, 740, "benzene_3")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(389.149985775259)  # Temperature in K
MaterialStream15.SetPressure(280000)  # Pressure in Pa
MaterialStream15.SetMassFlow(0.9178395)  # Mass Flow in kg/s

# Adding MaterialStream: MS_28c6916d_d26e_4127_a373_9f2bf2ce940d
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1101, 967, "lps_vapouriser")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(442.15)  # Temperature in K
MaterialStream16.SetPressure(400000)  # Pressure in Pa
MaterialStream16.SetMassFlow(0.233655)  # Mass Flow in kg/s

# Adding NodeIn: MIX_bd249e95_c9ec_49c4_9918_af6205efc0d1
Mixer3 = sim.AddObject(ObjectType.NodeIn, 1417, 537, "MIX-015")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MS_d5029b2f_d648_4dd9_9674_a4bd74dabb05
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1502, 538, "feed")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(422.219871368145)  # Temperature in K
MaterialStream17.SetPressure(280000)  # Pressure in Pa
MaterialStream17.SetMassFlow(23.276252)  # Mass Flow in kg/s

# Adding CompressorExpander: C_9e32b4bd_80b8_4577_a32a_c5e546cfd2b2
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1171, 647, "C-017")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding EnergyStream: ES_e910482f_7728_40f9_9e8c_2c3725fb1cfa
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 1109, 760, "ES-compress")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MS_81a17779_c03d_4eda_9d8d_b9b2df7f1e49
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1246, 522, "air_1_CLONE")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(438.924231457448)  # Temperature in K
MaterialStream18.SetPressure(253312.5)  # Pressure in Pa
MaterialStream18.SetMassFlow(22.3584125)  # Mass Flow in kg/s

# Adding HeaterCooler: HT_0dbe2f6f_1310_42a9_bafc_f54d6e4cae49
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 1569, 533, "fired heater")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding MaterialStream: MS_ead2f6dd_457b_425c_acf4_70e7f8d9413c
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1352, 886, "feed_1")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(733)  # Temperature in K
MaterialStream19.SetPressure(250000)  # Pressure in Pa
MaterialStream19.SetMassFlow(23.276252)  # Mass Flow in kg/s

# Adding EnergyStream: ES_e0f8c583_b605_4902_94b1_41c6aaef7e73
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1539, 688, "ES-heater")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding EnergyStream: ES_4d34f36d_0b7e_495d_a861_cef57df18e7e
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1372, 1105, "ES-reactor")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding RCT_Conversion: CR_1e47b960_f5ec_4dfd_bc14_291cfe19d782
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1531, 1020, "reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MS_0fdce5ec_7d2a_4a86_83f5_26be304dcbbc
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1604, 922, "crude product")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(849.096212830416)  # Temperature in K
MaterialStream20.SetPressure(98675)  # Pressure in Pa
MaterialStream20.SetMassFlow(23.30110570625)  # Mass Flow in kg/s

# Adding MaterialStream: MS_41509c6f_270e_4b2e_81ac_f16da1d27b20
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1757, 831, "crude product Cool")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(543)  # Temperature in K
MaterialStream21.SetPressure(98675)  # Pressure in Pa
MaterialStream21.SetMassFlow(23.30110570625)  # Mass Flow in kg/s

# Adding MaterialStream: MS_ba156767_ec8b_430d_8422_e0bcf503d860
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1670, 642, "dibutyl_bottom")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(601.735564427709)  # Temperature in K
MaterialStream22.SetPressure(82000)  # Pressure in Pa
MaterialStream22.SetMassFlow(38.6558724471668)  # Mass Flow in kg/s

# Adding NodeIn: MIX_4c395a5b_947a_4a98_af60_11fa37e11a36
Mixer4 = sim.AddObject(ObjectType.NodeIn, 1809, 691, "MIX-036")
Mixer4 = Mixer4.GetAsObject()

# Adding MaterialStream: MS_cdfd00e0_32d2_487c_a947_d6ebb41270ea
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 1879, 737, "MS-037")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(463.403983449729)  # Temperature in K
MaterialStream23.SetPressure(82000)  # Pressure in Pa
MaterialStream23.SetMassFlow(61.9647098819368)  # Mass Flow in kg/s

# Adding ShortcutColumn: SC_6c7341a5_f609_4c9b_90d9_7c1a113c1a48
ShortcutColumn1 = sim.AddObject(ObjectType.ShortcutColumn, 2063, 967, "dibutyl seperator")
ShortcutColumn1 = ShortcutColumn1.GetAsObject()

# Adding MaterialStream: MS_267cc0ce_9b77_4755_9058_7bdd55105822
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 2391, 921, "maleic_anhydride")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(468.77552230718)  # Temperature in K
MaterialStream24.SetPressure(80000)  # Pressure in Pa
MaterialStream24.SetMassFlow(0.989959026356425)  # Mass Flow in kg/s

# Adding EnergyStream: ES_74927525_2693_4de8_9544_7e596481a588
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 2160, 1165, "ES-reboiler")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding EnergyStream: ES_32169b1d_23b8_4d7a_b78c_7b2124a3c229
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2286, 1034, "ES-condenser")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding OT_Recycle: REC_b56b8d19_f77c_444b_a058_4e2668ea72c7
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1519, 879, "REC-043")
Recycle2 = Recycle2.GetAsObject()

# Adding ComponentSeparator: CS_830277cd_c824_4232_a629_559f548a0d94
ComponentSeparator1 = sim.AddObject(ObjectType.ComponentSeparator, 1966, 802, "seperator")
ComponentSeparator1 = ComponentSeparator1.GetAsObject()

# Adding HeaterCooler: CL_3395186c_19b2_4819_bec3_e7b67274d258
HeaterCooler3 = sim.AddObject(ObjectType.Heater, 1662, 827, "CL-crude product")
HeaterCooler3 = HeaterCooler3.GetAsObject()

# Adding EnergyStream: ES_7149807e_b653_4215_a5ff_da676582bff8
EnergyStream9 = sim.AddObject(ObjectType.EnergyStream, 1777, 916, "ES-crude cooler")
EnergyStream9 = EnergyStream9.GetAsObject()

sim.ConnectObjects(MaterialStream9.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream9 to HeatExchanger1
sim.ConnectObjects(EnergyStream5.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # EnergyStream5 to HeaterCooler2
sim.ConnectObjects(MaterialStream21.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream21 to Mixer4
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Mixer1 to MaterialStream2
sim.ConnectObjects(HeaterCooler3.GraphicObject, EnergyStream9.GraphicObject, -1, -1)  # HeaterCooler3 to EnergyStream9
sim.ConnectObjects(MaterialStream15.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream15 to Mixer3
sim.ConnectObjects(MaterialStream14.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream14 to Pump1
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Recycle1 to MaterialStream3
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Mixer2 to MaterialStream11
sim.ConnectObjects(MaterialStream7.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream7 to HeaterCooler1
sim.ConnectObjects(Mixer4.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Mixer4 to MaterialStream23
sim.ConnectObjects(MaterialStream1.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream1 to Recycle1
sim.ConnectObjects(MaterialStream2.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream2 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream4.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream4 to Recycle2
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream20
sim.ConnectObjects(HeaterCooler3.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # HeaterCooler3 to MaterialStream21
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream15
sim.ConnectObjects(EnergyStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream3 to Pump1
sim.ConnectObjects(MaterialStream20.GraphicObject, HeaterCooler3.GraphicObject, -1, -1)  # MaterialStream20 to HeaterCooler3
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream1.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream1
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # Mixer3 to MaterialStream17
sim.ConnectObjects(MaterialStream17.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream17 to HeaterCooler2
sim.ConnectObjects(MaterialStream22.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream22 to Mixer4
sim.ConnectObjects(MaterialStream16.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream16 to HeatExchanger1
sim.ConnectObjects(MaterialStream11.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream11 to AdiabaticExpanderCompressor1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream10
sim.ConnectObjects(EnergyStream6.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream6 to Reactor_Conversion1
sim.ConnectObjects(ComponentSeparator1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # ComponentSeparator1 to EnergyStream2
sim.ConnectObjects(MaterialStream23.GraphicObject, ComponentSeparator1.GraphicObject, -1, -1)  # MaterialStream23 to ComponentSeparator1
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream24
sim.ConnectObjects(ShortcutColumn1.GraphicObject, EnergyStream8.GraphicObject, -1, -1)  # ShortcutColumn1 to EnergyStream8
sim.ConnectObjects(MaterialStream18.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream18 to Mixer3
sim.ConnectObjects(MaterialStream12.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream12 to Mixer2
sim.ConnectObjects(MaterialStream10.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # MaterialStream10 to ShortcutColumn1
sim.ConnectObjects(MaterialStream5.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream5 to Mixer4
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream7
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # Pump1 to MaterialStream9
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream6
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(MaterialStream3.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream3 to Mixer1
sim.ConnectObjects(EnergyStream4.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream4 to AdiabaticExpanderCompressor1
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream8
sim.ConnectObjects(MaterialStream19.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream19 to Mixer1
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream4
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream19
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream18
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Recycle2 to MaterialStream22
sim.ConnectObjects(EnergyStream7.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # EnergyStream7 to ShortcutColumn1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_54.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_54.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

