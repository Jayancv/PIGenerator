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
formaldehyde = sim.AvailableCompounds["Formaldehyde"]
sim.SelectedCompounds.Add(formaldehyde.Name, formaldehyde)
methanol = sim.AvailableCompounds["Methanol"]
sim.SelectedCompounds.Add(methanol.Name, methanol)
hydrogen = sim.AvailableCompounds["Hydrogen"]
sim.SelectedCompounds.Add(hydrogen.Name, hydrogen)
water = sim.AvailableCompounds["Water"]
sim.SelectedCompounds.Add(water.Name, water)
oxygen = sim.AvailableCompounds["Oxygen"]
sim.SelectedCompounds.Add(oxygen.Name, oxygen)

# Adding Simulation Objects
# Adding MaterialStream: MAT_e3834fe5_8816_46f1_ab00_a966470935ec
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 2440, 982, "15")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(297.600400891073)  # Temperature in K
MaterialStream1.SetPressure(150000)  # Pressure in Pa
MaterialStream1.SetMassFlow(1.07957536264995)  # Mass Flow in kg/s

# Adding EnergyStream: EN_18720d2f_ff89_4680_8990_97fc379db2e5
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 2453, 907, "REBOILER DUTY")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding EnergyStream: EN_9a268161_5169_4000_9045_3b3325e3473b
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 2453, 752, "CONDENSER DUTY")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding MaterialStream: MAT_10dc1ef0_7672_4862_b0da_9a173d5f9731
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 2061, 666, "18")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(249.764985774193)  # Temperature in K
MaterialStream2.SetPressure(158675)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.18034663649532)  # Mass Flow in kg/s

# Adding OT_Recycle: REC_dfd03741_db52_4159_b1a0_4e5e43914818
Recycle1 = sim.AddObject(ObjectType.OT_Recycle, 2336, 667, "REC-047")
Recycle1 = Recycle1.GetAsObject()

# Adding MaterialStream: MAT_293a3693_4585_4b99_9c70_08c07dd1ab18
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 2513, 697, "14")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(249.764985774193)  # Temperature in K
MaterialStream3.SetPressure(158675)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.18034663649532)  # Mass Flow in kg/s

# Adding EnergyStream: EN_435c886d_98e7_42ae_ac1d_6ab0340af332
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 2606, 847, "ESTR-005")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding EnergyStream: EN_3dc7e2cc_3931_4b87_84bb_00f194b6cd21
EnergyStream4 = sim.AddObject(ObjectType.EnergyStream, 2570, 1009, "ESTR-006")
EnergyStream4 = EnergyStream4.GetAsObject()

# Adding Pump: BB_ac5a297b_71a7_4aba_9d4a_0fc51a2450e8
Pump1 = sim.AddObject(ObjectType.Pump, 2567, 789, "PUMP-002")
Pump1 = Pump1.GetAsObject()

# Adding MaterialStream: MAT_97311a5a_2a3f_4a0d_8e68_b15c9bbcffb7
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 2635, 950, "FORLMALIN")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(297.688246345396)  # Temperature in K
MaterialStream4.SetPressure(350000)  # Pressure in Pa
MaterialStream4.SetMassFlow(1.07957536264995)  # Mass Flow in kg/s

# Adding Pump: BB_79e579bb_5190_48fb_9bd1_695cef07544f
Pump2 = sim.AddObject(ObjectType.Pump, 2527, 954, "PUMP-003")
Pump2 = Pump2.GetAsObject()

# Adding MaterialStream: MAT_d387867f_8657_438e_abc2_57753a4a1de4
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 2486, 800, "MSTR-009")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(249.75199477096)  # Temperature in K
MaterialStream5.SetPressure(130000)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.18034663649532)  # Mass Flow in kg/s

# Adding ComponentSeparator: CS_c58544fa_99b9_4605_bcae_b1c3c0274952
ComponentSeparator1 = sim.AddObject(ObjectType.ComponentSeparator, 2095, 779, "compound separator")
ComponentSeparator1 = ComponentSeparator1.GetAsObject()

# Adding EnergyStream: EN_3cac4e36_ac9b_43d6_8110_34a1b2f1eedd
EnergyStream5 = sim.AddObject(ObjectType.EnergyStream, 2077, 874, "ESTR-004")
EnergyStream5 = EnergyStream5.GetAsObject()

# Adding MaterialStream: MAT_137190eb_7168_4642_9ec1_062d9a8b7e4e
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1975, 804, "MSTR-008")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(354.28034664163)  # Temperature in K
MaterialStream6.SetPressure(202425)  # Pressure in Pa
MaterialStream6.SetMassFlow(2.07318830243154)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_5cb34509_7654_45f6_80fb_8c63092edbc8
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1300, 966, "air(1)")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(298.15)  # Temperature in K
MaterialStream7.SetPressure(101300)  # Pressure in Pa
MaterialStream7.SetMassFlow(1.16959483413)  # Mass Flow in kg/s

# Adding NodeIn: MIST_1dcd1ab4_2961_4568_b1db_bc6670ab9cd7
Mixer1 = sim.AddObject(ObjectType.NodeIn, 1236, 964, "MIXER-002")
Mixer1 = Mixer1.GetAsObject()

# Adding MaterialStream: MAT_75fa50b0_70c6_4c18_bf43_d83ecc0289e2
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1173, 995, "nitrogen")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(298.15)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.8970699108)  # Mass Flow in kg/s

# Adding ShortcutColumn: SC_1305f7f4_e104_4a72_adbc_18b430a677ee
ShortcutColumn1 = sim.AddObject(ObjectType.ShortcutColumn, 2274, 826, "distillation column")
ShortcutColumn1 = ShortcutColumn1.GetAsObject()

# Adding MaterialStream: MAT_64394ba3_4200_4dc4_9565_dd858b8a19c0
MaterialStream9 = sim.AddObject(ObjectType.MaterialStream, 2205, 696, "off-gases-(12)")
MaterialStream9 = MaterialStream9.GetAsObject()
MaterialStream9.SetTemperature(354.28034664163)  # Temperature in K
MaterialStream9.SetPressure(202425)  # Pressure in Pa
MaterialStream9.SetMassFlow(1.02929344845299)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_116b5907_d360_4ef7_a4f9_b114fbb08a06
MaterialStream10 = sim.AddObject(ObjectType.MaterialStream, 2189, 881, "13")
MaterialStream10 = MaterialStream10.GetAsObject()
MaterialStream10.SetTemperature(354.28034664163)  # Temperature in K
MaterialStream10.SetPressure(202425)  # Pressure in Pa
MaterialStream10.SetMassFlow(1.2599398854)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_52532fd5_5587_4700_8ebf_8376499b6979
MaterialStream11 = sim.AddObject(ObjectType.MaterialStream, 1941, 1064, "MSTR-007")
MaterialStream11 = MaterialStream11.GetAsObject()
MaterialStream11.SetTemperature(373.534480545585)  # Temperature in K
MaterialStream11.SetPressure(1960000)  # Pressure in Pa
MaterialStream11.SetMassFlow(3)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_bdbec50c_9806_4e27_84b6_f9b961a0d04d
MaterialStream12 = sim.AddObject(ObjectType.MaterialStream, 1934, 925, "MSTR-006")
MaterialStream12 = MaterialStream12.GetAsObject()
MaterialStream12.SetTemperature(350)  # Temperature in K
MaterialStream12.SetPressure(2000000)  # Pressure in Pa
MaterialStream12.SetMassFlow(3)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_6f31aa93_f305_4336_9efd_f5cc25798fc0
MaterialStream13 = sim.AddObject(ObjectType.MaterialStream, 2001, 994, "10")
MaterialStream13 = MaterialStream13.GetAsObject()
MaterialStream13.SetTemperature(359.869694352956)  # Temperature in K
MaterialStream13.SetPressure(254850)  # Pressure in Pa
MaterialStream13.SetMassFlow(2.03346610243154)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_d516cf6f_fd89_4ca9_a0e0_82f30ba96743
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1942, 987, "HE-003")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding NodeIn: MIST_8add102b_debf_48ae_863d_e60c207c650d
Mixer2 = sim.AddObject(ObjectType.NodeIn, 1904, 811, "MIXER-004")
Mixer2 = Mixer2.GetAsObject()

# Adding EnergyStream: EN_dc6b3b7a_eb20_489a_9887_cec426ec3515
EnergyStream6 = sim.AddObject(ObjectType.EnergyStream, 1777, 961, "ESTR-003")
EnergyStream6 = EnergyStream6.GetAsObject()

# Adding MaterialStream: MAT_7c0bdd6f_6d3a_4411_9655_4b8d363864b9
MaterialStream14 = sim.AddObject(ObjectType.MaterialStream, 1821, 1033, "MSTR-005")
MaterialStream14 = MaterialStream14.GetAsObject()
MaterialStream14.SetTemperature(473.15)  # Temperature in K
MaterialStream14.SetPressure(289850)  # Pressure in Pa
MaterialStream14.SetMassFlow(0)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_04a9a2db_e3b7_4b1e_bf99_c20f9e64bd3c
MaterialStream15 = sim.AddObject(ObjectType.MaterialStream, 1895, 990, "9")
MaterialStream15 = MaterialStream15.GetAsObject()
MaterialStream15.SetTemperature(473.15)  # Temperature in K
MaterialStream15.SetPressure(289850)  # Pressure in Pa
MaterialStream15.SetMassFlow(2.03346610243154)  # Mass Flow in kg/s

# Adding RCT_Conversion: RC_c858102c_886f_4184_922d_4becd2335ed1
Reactor_Conversion1 = sim.AddObject(ObjectType.RCT_Conversion, 1796, 874, "reactor")
Reactor_Conversion1 = Reactor_Conversion1.GetAsObject()

# Adding MaterialStream: MAT_0bdc3823_a43b_48d0_abdb_0b2ac200dcd0
MaterialStream16 = sim.AddObject(ObjectType.MaterialStream, 1754, 891, "8")
MaterialStream16 = MaterialStream16.GetAsObject()
MaterialStream16.SetTemperature(445.768872046834)  # Temperature in K
MaterialStream16.SetPressure(289850)  # Pressure in Pa
MaterialStream16.SetMassFlow(2.03346610243154)  # Mass Flow in kg/s

# Adding NodeIn: MIST_58717e7d_faf9_4407_9a3c_9a09353f8c00
Mixer3 = sim.AddObject(ObjectType.NodeIn, 1697, 896, "MIXER-003")
Mixer3 = Mixer3.GetAsObject()

# Adding MaterialStream: MAT_cbd3c4d1_4f08_4861_80dd_3df4a153180a
MaterialStream17 = sim.AddObject(ObjectType.MaterialStream, 1674, 823, "6")
MaterialStream17 = MaterialStream17.GetAsObject()
MaterialStream17.SetTemperature(423.15)  # Temperature in K
MaterialStream17.SetPressure(314700)  # Pressure in Pa
MaterialStream17.SetMassFlow(0.863871268301535)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_1de7a776_fec8_4f75_af96_d99aa8f6a73c
MaterialStream18 = sim.AddObject(ObjectType.MaterialStream, 1602, 894, "MSTR-002")
MaterialStream18 = MaterialStream18.GetAsObject()
MaterialStream18.SetTemperature(427.482104323546)  # Temperature in K
MaterialStream18.SetPressure(533130)  # Pressure in Pa
MaterialStream18.SetMassFlow(5)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_841c52e9_27e2_426f_b77d_010f31ba51c9
MaterialStream19 = sim.AddObject(ObjectType.MaterialStream, 1598, 731, "MSTR-001")
MaterialStream19 = MaterialStream19.GetAsObject()
MaterialStream19.SetTemperature(497.91035283866)  # Temperature in K
MaterialStream19.SetPressure(2533130)  # Pressure in Pa
MaterialStream19.SetMassFlow(5)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_4bfc161a_e7b2_4f2b_8c63_d504a288ae0d
HeatExchanger2 = sim.AddObject(ObjectType.HeatExchanger, 1588, 822, "HE-001")
HeatExchanger2 = HeatExchanger2.GetAsObject()

# Adding MaterialStream: MAT_afb7c618_7513_4ec6_b44f_350ea36cf5ab
MaterialStream20 = sim.AddObject(ObjectType.MaterialStream, 1536, 894, "MSTR-003")
MaterialStream20 = MaterialStream20.GetAsObject()
MaterialStream20.SetTemperature(600)  # Temperature in K
MaterialStream20.SetPressure(101325)  # Pressure in Pa
MaterialStream20.SetMassFlow(0.18015)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_dc0fe565_e05c_42c0_8fba_a5730f226498
MaterialStream21 = sim.AddObject(ObjectType.MaterialStream, 1545, 1038, "MSTR-004")
MaterialStream21 = MaterialStream21.GetAsObject()
MaterialStream21.SetTemperature(483.818229934171)  # Temperature in K
MaterialStream21.SetPressure(101325)  # Pressure in Pa
MaterialStream21.SetMassFlow(0.18015)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_de97625b_3751_4510_9561_7b504c3a9694
MaterialStream22 = sim.AddObject(ObjectType.MaterialStream, 1646, 953, "7")
MaterialStream22 = MaterialStream22.GetAsObject()
MaterialStream22.SetTemperature(473.15)  # Temperature in K
MaterialStream22.SetPressure(265000)  # Pressure in Pa
MaterialStream22.SetMassFlow(1.16959483413)  # Mass Flow in kg/s

# Adding HeatExchanger: HE_69f5619e_c780_464d_8cb4_d12792a6ba31
HeatExchanger3 = sim.AddObject(ObjectType.HeatExchanger, 1532, 961, "HE-002")
HeatExchanger3 = HeatExchanger3.GetAsObject()

# Adding EnergyStream: EN_fd15d07e_d63f_42a5_ad23_13df37c9912b
EnergyStream7 = sim.AddObject(ObjectType.EnergyStream, 1339, 1010, "ESTR-002")
EnergyStream7 = EnergyStream7.GetAsObject()

# Adding MaterialStream: MAT_67e638eb_7845_47aa_a571_96fd98664032
MaterialStream23 = sim.AddObject(ObjectType.MaterialStream, 1446, 962, "5")
MaterialStream23 = MaterialStream23.GetAsObject()
MaterialStream23.SetTemperature(438.861627418521)  # Temperature in K
MaterialStream23.SetPressure(300000)  # Pressure in Pa
MaterialStream23.SetMassFlow(1.16959483413)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_58a3e5d4_43c4_4965_bd2f_918a02c0db57
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 1361, 951, "COMPRESSOR-001")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_6f2f5676_a808_402e_a4ea_a235b7db96e8
MaterialStream24 = sim.AddObject(ObjectType.MaterialStream, 1175, 913, "oxygen")
MaterialStream24 = MaterialStream24.GetAsObject()
MaterialStream24.SetTemperature(298.15)  # Temperature in K
MaterialStream24.SetPressure(101300)  # Pressure in Pa
MaterialStream24.SetMassFlow(0.27252492333)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_9f4dded5_d22e_4644_a0c8_c213109c2e69
MaterialStream25 = sim.AddObject(ObjectType.MaterialStream, 1532, 832, "4")
MaterialStream25 = MaterialStream25.GetAsObject()
MaterialStream25.SetTemperature(291.673335350551)  # Temperature in K
MaterialStream25.SetPressure(318700)  # Pressure in Pa
MaterialStream25.SetMassFlow(0.863871268301535)  # Mass Flow in kg/s

# Adding EnergyStream: EN_3ebf7da8_e34e_450b_ad97_2824379265ea
EnergyStream8 = sim.AddObject(ObjectType.EnergyStream, 1450, 894, "ESTR-001")
EnergyStream8 = EnergyStream8.GetAsObject()

# Adding MaterialStream: MAT_f0241bc4_f9d4_4cbe_b9d9_e49ac57db7cf
MaterialStream26 = sim.AddObject(ObjectType.MaterialStream, 1410, 833, "3")
MaterialStream26 = MaterialStream26.GetAsObject()
MaterialStream26.SetTemperature(291.571781647962)  # Temperature in K
MaterialStream26.SetPressure(120000)  # Pressure in Pa
MaterialStream26.SetMassFlow(0.863871268301535)  # Mass Flow in kg/s

# Adding NodeIn: MIST_0004e5a4_586e_49b6_87a6_f2c3e4941a91
Mixer4 = sim.AddObject(ObjectType.NodeIn, 1345, 824, "MIXER-001")
Mixer4 = Mixer4.GetAsObject()

# Adding Pump: BB_9b9692f5_2423_482b_be45_ff95a9040c72
Pump3 = sim.AddObject(ObjectType.Pump, 1477, 830, "PUMP-001")
Pump3 = Pump3.GetAsObject()

# Adding MaterialStream: MAT_13c8735d_d642_4369_bab7_0f13b84c5ebe
MaterialStream27 = sim.AddObject(ObjectType.MaterialStream, 1187, 834, "METHANOL(2)")
MaterialStream27 = MaterialStream27.GetAsObject()
MaterialStream27.SetTemperature(303.15)  # Temperature in K
MaterialStream27.SetPressure(120000)  # Pressure in Pa
MaterialStream27.SetMassFlow(0.6846318014)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_95110bd2_487f_4c92_bcf8_93e1077ae02c
MaterialStream28 = sim.AddObject(ObjectType.MaterialStream, 1149, 757, "WATER(1)")
MaterialStream28 = MaterialStream28.GetAsObject()
MaterialStream28.SetTemperature(303.15)  # Temperature in K
MaterialStream28.SetPressure(150000)  # Pressure in Pa
MaterialStream28.SetMassFlow(0.0397222)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream2.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream2 to Mixer4
sim.ConnectObjects(ComponentSeparator1.GraphicObject, EnergyStream5.GraphicObject, -1, -1)  # ComponentSeparator1 to EnergyStream5
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream9.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream9
sim.ConnectObjects(EnergyStream8.GraphicObject, Pump3.GraphicObject, -1, -1)  # EnergyStream8 to Pump3
sim.ConnectObjects(MaterialStream5.GraphicObject, Pump1.GraphicObject, -1, -1)  # MaterialStream5 to Pump1
sim.ConnectObjects(MaterialStream15.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream15 to HeatExchanger1
sim.ConnectObjects(Pump1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # Pump1 to MaterialStream3
sim.ConnectObjects(EnergyStream4.GraphicObject, Pump2.GraphicObject, -1, -1)  # EnergyStream4 to Pump2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream11.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream11
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream17.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream17
sim.ConnectObjects(MaterialStream24.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream24 to Mixer1
sim.ConnectObjects(EnergyStream7.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream7 to AdiabaticExpanderCompressor1
sim.ConnectObjects(Mixer4.GraphicObject, MaterialStream26.GraphicObject, -1, -1)  # Mixer4 to MaterialStream26
sim.ConnectObjects(MaterialStream7.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream7 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream23.GraphicObject, HeatExchanger3.GraphicObject, -1, -1)  # MaterialStream23 to HeatExchanger3
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream15.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream15
sim.ConnectObjects(MaterialStream28.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream28 to Mixer2
sim.ConnectObjects(MaterialStream25.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream25 to HeatExchanger2
sim.ConnectObjects(EnergyStream6.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # EnergyStream6 to Reactor_Conversion1
sim.ConnectObjects(Mixer1.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # Mixer1 to MaterialStream7
sim.ConnectObjects(MaterialStream10.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # MaterialStream10 to ShortcutColumn1
sim.ConnectObjects(MaterialStream26.GraphicObject, Pump3.GraphicObject, -1, -1)  # MaterialStream26 to Pump3
sim.ConnectObjects(MaterialStream12.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream12 to HeatExchanger1
sim.ConnectObjects(EnergyStream3.GraphicObject, Pump1.GraphicObject, -1, -1)  # EnergyStream3 to Pump1
sim.ConnectObjects(MaterialStream20.GraphicObject, HeatExchanger3.GraphicObject, -1, -1)  # MaterialStream20 to HeatExchanger3
sim.ConnectObjects(ComponentSeparator1.GraphicObject, MaterialStream10.GraphicObject, -1, -1)  # ComponentSeparator1 to MaterialStream10
sim.ConnectObjects(HeatExchanger3.GraphicObject, MaterialStream22.GraphicObject, -1, -1)  # HeatExchanger3 to MaterialStream22
sim.ConnectObjects(MaterialStream22.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream22 to Mixer3
sim.ConnectObjects(Recycle1.GraphicObject, MaterialStream2.GraphicObject, -1, -1)  # Recycle1 to MaterialStream2
sim.ConnectObjects(Pump2.GraphicObject, MaterialStream4.GraphicObject, -1, -1)  # Pump2 to MaterialStream4
sim.ConnectObjects(MaterialStream27.GraphicObject, Mixer4.GraphicObject, -1, -1)  # MaterialStream27 to Mixer4
sim.ConnectObjects(HeatExchanger3.GraphicObject, MaterialStream21.GraphicObject, -1, -1)  # HeatExchanger3 to MaterialStream21
sim.ConnectObjects(ShortcutColumn1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # ShortcutColumn1 to EnergyStream2
sim.ConnectObjects(EnergyStream1.GraphicObject, ShortcutColumn1.GraphicObject, -1, -1)  # EnergyStream1 to ShortcutColumn1
sim.ConnectObjects(MaterialStream8.GraphicObject, Mixer1.GraphicObject, -1, -1)  # MaterialStream8 to Mixer1
sim.ConnectObjects(MaterialStream19.GraphicObject, HeatExchanger2.GraphicObject, -1, -1)  # MaterialStream19 to HeatExchanger2
sim.ConnectObjects(MaterialStream1.GraphicObject, Pump2.GraphicObject, -1, -1)  # MaterialStream1 to Pump2
sim.ConnectObjects(MaterialStream13.GraphicObject, Mixer2.GraphicObject, -1, -1)  # MaterialStream13 to Mixer2
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream13.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream13
sim.ConnectObjects(Mixer3.GraphicObject, MaterialStream16.GraphicObject, -1, -1)  # Mixer3 to MaterialStream16
sim.ConnectObjects(Mixer2.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # Mixer2 to MaterialStream6
sim.ConnectObjects(MaterialStream16.GraphicObject, Reactor_Conversion1.GraphicObject, -1, -1)  # MaterialStream16 to Reactor_Conversion1
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream23.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream23
sim.ConnectObjects(Pump3.GraphicObject, MaterialStream25.GraphicObject, -1, -1)  # Pump3 to MaterialStream25
sim.ConnectObjects(MaterialStream17.GraphicObject, Mixer3.GraphicObject, -1, -1)  # MaterialStream17 to Mixer3
sim.ConnectObjects(Reactor_Conversion1.GraphicObject, MaterialStream14.GraphicObject, -1, -1)  # Reactor_Conversion1 to MaterialStream14
sim.ConnectObjects(MaterialStream3.GraphicObject, Recycle1.GraphicObject, -1, -1)  # MaterialStream3 to Recycle1
sim.ConnectObjects(MaterialStream6.GraphicObject, ComponentSeparator1.GraphicObject, -1, -1)  # MaterialStream6 to ComponentSeparator1
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream1
sim.ConnectObjects(ShortcutColumn1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # ShortcutColumn1 to MaterialStream5
sim.ConnectObjects(HeatExchanger2.GraphicObject, MaterialStream18.GraphicObject, -1, -1)  # HeatExchanger2 to MaterialStream18
 # sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_39.xml")
 
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
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_39.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

