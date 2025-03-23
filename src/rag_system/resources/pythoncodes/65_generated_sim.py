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
carbon_dioxide = sim.AvailableCompounds["Carbon dioxide"]
sim.SelectedCompounds.Add(carbon_dioxide.Name, carbon_dioxide)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
ethylene = sim.AvailableCompounds["Ethylene"]
sim.SelectedCompounds.Add(ethylene.Name, ethylene)
ethylene_oxide = sim.AvailableCompounds["Ethylene oxide"]
sim.SelectedCompounds.Add(ethylene_oxide.Name, ethylene_oxide)
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)

# Adding Simulation Objects
# Adding MaterialStream: MAT_586d1268_0fde_4b93_813b_19870726d057
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 1567, 981, "MSTR-050")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(132.687659354294)  # Temperature in K
MaterialStream1.SetPressure(3316372.26106262)  # Pressure in Pa
MaterialStream1.SetMassFlow(5)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_15b8e565_77a0_498c_a924_ff486fc4957e
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 1836, 889, "REC-049")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_ff2affc6_625c_41d8_99b3_33b77e3dd4b8
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 1770, 1058, "MSTR-049")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(337.876346760026)  # Temperature in K
MaterialStream2.SetPressure(3316372.26106262)  # Pressure in Pa
MaterialStream2.SetMassFlow(11.6267649395336)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_90f247cb_d35f_4e54_b169_b23691e8729e
Recycle2 = sim.AddObject(ObjectType.OT_Recycle, 1908, 920, "REC-048")
Recycle2 = Recycle2.GetAsObject()

# Adding Tank: TQ_684f0444_a9e1_4a0f_ab5e_250d0ec58216
Tank1 = sim.AddObject(ObjectType.Tank, 3293, 1143, "Bullet storage tank")
Tank1 = Tank1.GetAsObject()

# Adding EnergyStream: EN_120a10e4_be5e_4c4b_81a0_45cda773e143
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 3109, 1254, "R-Duty")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_d9c84294_7467_4f92_9e04_c6cc783ae386
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 3090, 1086, "C-Duty")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_83ba7a45_2b55_434e_9118_a36381cb44d1
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 3065, 1289, "Residue")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(356.528277368616)  # Temperature in K
MaterialStream3.SetPressure(101325)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.050432886344011)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_4b5e09f4_70b1_4c0c_8c0d_dd5d7b330460
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 3418, 1054, "Final Product (EO)")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(281.137943766016)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.925431849075249)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_051fce9f_0598_4bad_b442_d37dfae86491
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 3070, 1139, "Distillate")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(252.41511518547)  # Temperature in K
MaterialStream5.SetPressure(101325)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.925431849075249)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_7a6b6953_319f_4825_8d18_bbdc4b6a9d41
DistillationColumn1 = sim.AddObject(ObjectType.DistillationColumn, 2885, 1094, "Regourous Distillation column-2")
DistillationColumn1 = DistillationColumn1.GetAsObject()

# Adding EnergyStream: EN_6c25a8b5_2906_4c4e_8b07_00607bd2eec8
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2814, 1225, "R-Duty1")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_214eb168_5d1b_40d2_84e8_a5f78510b711
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2794, 1109, "C-Duty1")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding MaterialStream: MAT_e3c1bcd0_2464_414a_a28c_fa1a82f23eeb
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 2802, 1279, "Residue1")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(432.275618123098)  # Temperature in K
MaterialStream6.SetPressure(607950)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.0158889627315867)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b80dabd4_d0e6_4b5d_a3cf_6f60a832c835
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 2819, 1152, "Distillate1")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(252.583070888458)  # Temperature in K
MaterialStream7.SetPressure(101325)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.975869293134374)  # Mass Flow in kg/s

# Adding DistillationColumn: DC_b08a1ed1_517a_4ca8_81fd_9c7f81712194
DistillationColumn2 = sim.AddObject(ObjectType.DistillationColumn, 2596, 1107, "Rigourous Distillation Column")
DistillationColumn2 = DistillationColumn2.GetAsObject()

# Adding Vessel: SEP_0be89fa4_6755_4656_87aa_c5bb6097d5fe
Vessel1 = sim.AddObject(ObjectType.Vessel, 2381, 1231, "Seperator")
Vessel1 = Vessel1.GetAsObject()

# Adding MaterialStream: MAT_79824050_e651_453d_9c2f_c5e1c6d4ec83
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1186, 981, "Ethylene")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(298.15)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(3.71148176816083)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_7a2b6341_fe50_4e82_86cf_1309729236f8
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 1190, 1137, "Oxygen")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(298.15)  # Temperature in K
MaterialStream9.SetPressure(101325)  # Pressure in Pa
MaterialStream9.SetMassFlow(4.23339648889208)  # Mass Flow in kg/s

# Adding Compressor: COMP_6528e623_b2d7_4c7d_b791_43ee9c471c72
Compressor1 = sim.AddObject(ObjectType.Compressor, 1310, 981, "COMPRESSOR")
Compressor1 = Compressor1.GetAsObject()

# Adding Compressor: COMP_9bddc9d8_b06c_42d8_8d5d_6d911e2328fe
Compressor2 = sim.AddObject(ObjectType.Compressor, 1314, 1136, "COMPRESSOR1")
Compressor2 = Compressor2.GetAsObject()

# Adding MaterialStream: MAT_69a84998_aa4e_4134_80ea_2bdbdfc708fb
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 1412, 990, "Compressed Ethylene")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(563.079933626606)  # Temperature in K
MaterialStream10.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream10.SetMassFlow(3.71148176816083)  # Mass Flow in kg/s

# Adding EnergyStream: EN_0eb272ae_bbcf_4d69_a980_8e9a76ae823f
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 1274, 1049, "ESTR-005")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_e5b4e17b_423c_4d14_a937_e8bd0e255bd6
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1407, 1153, "Compressed Oxygen")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(855.876585705542)  # Temperature in K
MaterialStream11.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream11.SetMassFlow(4.23339648889208)  # Mass Flow in kg/s

# Adding EnergyStream: EN_6175c261_d30a_43a0_86b1_7f4bce7a4dd6
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1239, 1211, "ESTR-007")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding NodeIn: MIST_aa3060bd_efa2_460d_be09_ddef4588a592
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1521, 1092, "MIXER")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_c979d431_7e43_4416_a146_6f3115c95244
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1580, 1091, "Reactor Inlet")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(406.45761930092)  # Temperature in K
MaterialStream12.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream12.SetMassFlow(12.9448782570529)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_31f3f885_83ec_48cc_820e_9b100ec21608
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1702, 1093, "Conversion Reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_6e100ab1_70dc_4f37_9b2c_6eeac57082e2
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 1836, 1109, "Reactor Product")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(406.45761930092)  # Temperature in K
MaterialStream13.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream13.SetMassFlow(12.9448782570529)  # Mass Flow in kg/s

# Adding EnergyStream: EN_53cdd241_8c1e_4405_a0aa_569ee57a3a8f
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 1639, 1164, "ESTR-012")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_c62e215f_8f6a_45bd_b265_04ca15bad448
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1741, 1266, "Empty Stream")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(406.45761930092)  # Temperature in K
MaterialStream14.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream14.SetMassFlow(0)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_b6c5bd2e_7ded_481b_ac67_1bfaedac2db5
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1846, 1207, "Heat Exchanger")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_8bb7debc_d7b4_471c_901c_8ea393866309
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1937, 1089, "MSTR-015")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(468.083138580818)  # Temperature in K
MaterialStream15.SetPressure(3316372.26106262)  # Pressure in Pa
MaterialStream15.SetMassFlow(11.6267649395336)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b5d4bff0_d9c6_448b_a0b7_5cde7287b54c
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 2027, 1178, "Absorber Feed")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(313.15)  # Temperature in K
MaterialStream16.SetPressure(2746466.6)  # Pressure in Pa
MaterialStream16.SetMassFlow(12.9448782570529)  # Mass Flow in kg/s

# Adding AbsorptionColumn: ABS_b0f018b2_4571_436a_aae4_bb8c7de14190
AbsorptionColumn1 = sim.AddObject(ObjectType.AbsorptionColumn, 2105, 1014, "Absorption Column")
AbsorptionColumn1 = AbsorptionColumn1.GetAsObject()

# Adding MaterialStream: MAT_c3616db5_6e18_4020_9492_eeebf125e554
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 2010, 1015, "Water")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(333.15)  # Temperature in K
MaterialStream17.SetPressure(101325)  # Pressure in Pa
MaterialStream17.SetMassFlow(11.2357665001313)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_fda8516c_c97d_4150_adff_1ef9f1b96f1d
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 2315, 970, "MSTR-023")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(337.876346760062)  # Temperature in K
MaterialStream18.SetPressure(3316372.26106262)  # Pressure in Pa
MaterialStream18.SetMassFlow(11.6267649395342)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_98660593_aaef_44ad_a860_c8f695ecd615
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 2274, 1253, "MSTR-024")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(332.843165079709)  # Temperature in K
MaterialStream19.SetPressure(3330161.75071361)  # Pressure in Pa
MaterialStream19.SetMassFlow(12.553879833696)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b93db594_32a8_48b6_9ab6_e585f8514007
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 2452, 1128, "MSTR-026")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(332.843165079709)  # Temperature in K
MaterialStream20.SetPressure(3330161.75071361)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.991774025250916)  # Mass Flow in kg/s

# Adding EnergyStream: EN_fca3849f_25b5_4623_8b44_20825e74d309
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 2514, 1206, "ESTR-030")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding Cooler: RESF_a9f9f8db_f59f_4f2f_bda9_32f25b7b9435
Cooler1 = sim.AddObject(ObjectType.Cooler, 2496, 1056, "COOL-036")
Cooler1 = Cooler1.GetAsObject()

# Adding MaterialStream: MAT_a6d13d68_dd0b_469f_986d_d3fc06200352
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 2548, 1344, "MSTR-039")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(332.843165079709)  # Temperature in K
MaterialStream21.SetPressure(3330161.75071361)  # Pressure in Pa
MaterialStream21.SetMassFlow(11.5621053361423)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_ae5a67f7_6f68_4f0e_9160_4c4c5101e2be
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 2423, 1346, "MSTR-036")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(332.843165079709)  # Temperature in K
MaterialStream22.SetPressure(3330161.75071361)  # Pressure in Pa
MaterialStream22.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_15f7b63b_0c76_490f_abd0_1a2cee881005
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 2548, 1139, "MSTR-037")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(298.15)  # Temperature in K
MaterialStream23.SetPressure(3330161.75071361)  # Pressure in Pa
MaterialStream23.SetMassFlow(0.991774025250916)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_8e9866db_8dd9_4051_8381_420c50cfe037
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 3167, 1164, "HEAT EXCHANGER")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_f582d4bf_20b2_41a0_a75e_78e31e672308
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 3239, 1107, "MSTR-045")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(277.999984577374)  # Temperature in K
MaterialStream24.SetPressure(101325)  # Pressure in Pa
MaterialStream24.SetMassFlow(1)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_b45bad68_30a0_4b46_bbc6_663d2fa73738
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 3075, 1190, "MSTR-046")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(303.15)  # Temperature in K
MaterialStream25.SetPressure(101325)  # Pressure in Pa
MaterialStream25.SetMassFlow(1)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_f75c0ee1_c190_459c_b538_3878e5152a20
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 3211, 1247, "MSTR-047")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(281.137943766016)  # Temperature in K
MaterialStream26.SetPressure(101325)  # Pressure in Pa
MaterialStream26.SetMassFlow(0.925431849075249)  # Mass Flow in kg/s

DistillationColumn1.ConnectDistillate(MaterialStream5)  # ConnectDistillate 
DistillationColumn1.ConnectBottoms(MaterialStream3)  # ConnectBottoms 
DistillationColumn1.ConnectCondenserDuty(EnergyStream2)  # ConnectCondenserDuty 
DistillationColumn1.ConnectReboilerDuty(EnergyStream1)  # ConnectReboilerDuty 
DistillationColumn2.ConnectDistillate(MaterialStream7)  # ConnectDistillate 
DistillationColumn2.ConnectBottoms(MaterialStream6)  # ConnectBottoms 
DistillationColumn2.ConnectCondenserDuty(EnergyStream4)  # ConnectCondenserDuty 
DistillationColumn2.ConnectReboilerDuty(EnergyStream3)  # ConnectReboilerDuty 
sim.ConnectObjects(MaterialStream18.GraphicObject, Recycle2.GraphicObject, -1, -1)  # MaterialStream18 to Recycle2
sim.ConnectObjects(MaterialStream2.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream2 to HeatExchanger1
sim.ConnectObjects(MaterialStream12.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream12 to Reactor_Conversion1
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream24.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream24
sim.ConnectObjects(MaterialStream1.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream1 to Mixer1
sim.ConnectObjects(AbsorptionColumn1.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # AbsorptionColumn1 to MaterialStream18
sim.ConnectObjects(Tank1.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Tank1 to MaterialStream4
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream15
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream16
sim.ConnectObjects(Cooler1.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # Cooler1 to MaterialStream23
sim.ConnectObjects(MaterialStream16.GraphicObject, AbsorptionColumn1.GraphicObject, -1, -1)  # MaterialStream16 to AbsorptionColumn1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # Vessel1 to MaterialStream22
sim.ConnectObjects(MaterialStream8.GraphicObject, Compressor1.GraphicObject, -1, -1)  # MaterialStream8 to Compressor1
sim.ConnectObjects(MaterialStream15.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream15 to Recycle1
sim.ConnectObjects(EnergyStream5.GraphicObject, Compressor1.GraphicObject, -1, -1)  # EnergyStream5 to Compressor1
sim.ConnectObjects(AbsorptionColumn1.GraphicObject, MaterialStream19.GraphicObject, -1, -1)  # AbsorptionColumn1 to MaterialStream19
sim.ConnectObjects(Cooler1.GraphicObject, EnergyStream8.GraphicObject, -1, -1)  # Cooler1 to EnergyStream8
sim.ConnectObjects(MaterialStream9.GraphicObject, Compressor2.GraphicObject, -1, -1)  # MaterialStream9 to Compressor2
sim.ConnectObjects(MaterialStream19.GraphicObject, Vessel1.GraphicObject, -1, -1)  # MaterialStream19 to Vessel1
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream26
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream12.GraphicObject, -1, -1)  # Mixer1 to MaterialStream12
sim.ConnectObjects(Recycle2.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle2 to MaterialStream2
sim.ConnectObjects(MaterialStream13.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream13 to HeatExchanger1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # Vessel1 to MaterialStream21
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream14
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # Recycle1 to MaterialStream1
sim.ConnectObjects(MaterialStream7.GraphicObject, DistillationColumn1.GraphicObject, -1, -1)  # MaterialStream7 to DistillationColumn1
sim.ConnectObjects(EnergyStream6.GraphicObject, Compressor2.GraphicObject, -1, -1)  # EnergyStream6 to Compressor2
sim.ConnectObjects(Compressor2.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # Compressor2 to MaterialStream11
sim.ConnectObjects(MaterialStream5.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream5 to HeatExchanger2
sim.ConnectObjects(EnergyStream7.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream7 to Reactor_Conversion1
sim.ConnectObjects(MaterialStream17.GraphicObject, AbsorptionColumn1.GraphicObject, -1, -1)  # MaterialStream17 to AbsorptionColumn1
sim.ConnectObjects(Vessel1.GraphicObject, MaterialStream20.GraphicObject, -1, -1)  # Vessel1 to MaterialStream20
sim.ConnectObjects(MaterialStream23.GraphicObject, DistillationColumn2.GraphicObject, -1, -1)  # MaterialStream23 to DistillationColumn2
sim.ConnectObjects(MaterialStream25.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream25 to HeatExchanger2
sim.ConnectObjects(Compressor1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # Compressor1 to MaterialStream10
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream13
sim.ConnectObjects(MaterialStream10.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream10 to Mixer1
sim.ConnectObjects(MaterialStream26.GraphicObject, Tank1.GraphicObject, -1, -1)  # MaterialStream26 to Tank1
sim.ConnectObjects(MaterialStream11.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream11 to Mixer1
sim.ConnectObjects(MaterialStream20.GraphicObject, Cooler1.GraphicObject, -1, -1)  # MaterialStream20 to Cooler1
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_65.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_65.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

