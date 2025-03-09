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

# Adding Simulation Objects
# Adding EnergyStream: EN_6a201fda_f096_4d66_9404_0fb5b35433af
EnergyStream1 = sim.AddObject(ObjectType.EnergyStream, 748, 612, "ESTR-001")
EnergyStream1 = EnergyStream1.GetAsObject()

# Adding MaterialStream: MAT_000b4dcd_6aca_4190_b3bb_6bb51b6eb027
MaterialStream1 = sim.AddObject(ObjectType.MaterialStream, 846, 458, "Com N2")
MaterialStream1 = MaterialStream1.GetAsObject()
MaterialStream1.SetTemperature(1131.98201722368)  # Temperature in K
MaterialStream1.SetPressure(2533125)  # Pressure in Pa
MaterialStream1.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding CompressorExpander: COMP_45b1e044_8e2c_4d41_8368_720d4a11aa61
AdiabaticExpanderCompressor1 = sim.AddObject(ObjectType.Compressor, 798, 549, "Compressor")
AdiabaticExpanderCompressor1 = AdiabaticExpanderCompressor1.GetAsObject()

# Adding MaterialStream: MAT_c0907dbf_9c7c_44b2_a651_e1568538cd98
MaterialStream2 = sim.AddObject(ObjectType.MaterialStream, 746, 458, "Mixed N2")
MaterialStream2 = MaterialStream2.GetAsObject()
MaterialStream2.SetTemperature(300)  # Temperature in K
MaterialStream2.SetPressure(101325)  # Pressure in Pa
MaterialStream2.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_9905f77d_baad_43f0_8566_89fd694a4aa0
HeaterCooler1 = sim.AddObject(ObjectType.Heater, 907, 457, "Cooler-001")
HeaterCooler1 = HeaterCooler1.GetAsObject()

# Adding MaterialStream: MAT_abbf3208_85ab_4c5a_8b61_17f97e2006a9
MaterialStream3 = sim.AddObject(ObjectType.MaterialStream, 998, 462, "Cooled-N2-S1")
MaterialStream3 = MaterialStream3.GetAsObject()
MaterialStream3.SetTemperature(300.000000041442)  # Temperature in K
MaterialStream3.SetPressure(2533125)  # Pressure in Pa
MaterialStream3.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding EnergyStream: EN_4d661a5d_ea23_44b7_a14d_6ac8923ca2ba
EnergyStream2 = sim.AddObject(ObjectType.EnergyStream, 940, 550, "ESTR-002")
EnergyStream2 = EnergyStream2.GetAsObject()

# Adding HeatExchanger: HE_25faa348_c84f_48f6_971e_589b9697f800
HeatExchanger1 = sim.AddObject(ObjectType.HeatExchanger, 1068, 455, "HE-009")
HeatExchanger1 = HeatExchanger1.GetAsObject()

# Adding MaterialStream: MAT_442ad76e_b5e7_483c_a8a0_3d843d03affe
MaterialStream4 = sim.AddObject(ObjectType.MaterialStream, 1006, 396, "N2-Cold")
MaterialStream4 = MaterialStream4.GetAsObject()
MaterialStream4.SetTemperature(77.3547226738273)  # Temperature in K
MaterialStream4.SetPressure(101325)  # Pressure in Pa
MaterialStream4.SetMassFlow(0.225)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_41e90e45_1b9f_4d90_a28c_5a4d5c276968
MaterialStream5 = sim.AddObject(ObjectType.MaterialStream, 1143, 460, "Cooled-N2-S2")
MaterialStream5 = MaterialStream5.GetAsObject()
MaterialStream5.SetTemperature(185.421933523528)  # Temperature in K
MaterialStream5.SetPressure(2533125)  # Pressure in Pa
MaterialStream5.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding MaterialStream: MAT_38ae9812_c1a9_4673_b02e_77dcf0eed1f6
MaterialStream6 = sim.AddObject(ObjectType.MaterialStream, 1055, 566, "N2-Hot")
MaterialStream6 = MaterialStream6.GetAsObject()
MaterialStream6.SetTemperature(229.000008569682)  # Temperature in K
MaterialStream6.SetPressure(101325)  # Pressure in Pa
MaterialStream6.SetMassFlow(0.225)  # Mass Flow in kg/s

# Adding HeaterCooler: RESF_cbfcb8b7_ed0a_478c_924c_060f815ed8c3
HeaterCooler2 = sim.AddObject(ObjectType.Heater, 1223, 456, "Cooler")
HeaterCooler2 = HeaterCooler2.GetAsObject()

# Adding MaterialStream: MAT_6e1e44b0_7ddc_4d11_9fad_a5526d06267d
MaterialStream7 = sim.AddObject(ObjectType.MaterialStream, 1269, 564, "Cooled-N2-S3")
MaterialStream7 = MaterialStream7.GetAsObject()
MaterialStream7.SetTemperature(84.9999999992714)  # Temperature in K
MaterialStream7.SetPressure(2533125)  # Pressure in Pa
MaterialStream7.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

# Adding EnergyStream: EN_37412dcc_4112_41db_bad7_2eddf4b8179d
EnergyStream3 = sim.AddObject(ObjectType.EnergyStream, 1150, 569, "ESTR-003")
EnergyStream3 = EnergyStream3.GetAsObject()

# Adding Valve: VALV_66b69073_a1b7_4a35_a1c0_655de7a476f6
Valve1 = sim.AddObject(ObjectType.Valve, 1312, 454, "Valve")
Valve1 = Valve1.GetAsObject()

# Adding MaterialStream: MAT_ca61f92a_5afb_4c0c_9849_776ced812743
MaterialStream8 = sim.AddObject(ObjectType.MaterialStream, 1379, 455, "Liquified-N2")
MaterialStream8 = MaterialStream8.GetAsObject()
MaterialStream8.SetTemperature(77.3547221359901)  # Temperature in K
MaterialStream8.SetPressure(101325)  # Pressure in Pa
MaterialStream8.SetMassFlow(0.277777777777778)  # Mass Flow in kg/s

sim.ConnectObjects(MaterialStream1.GraphicObject, HeaterCooler1.GraphicObject, -1, -1)  # MaterialStream1 to HeaterCooler1
sim.ConnectObjects(EnergyStream1.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # EnergyStream1 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream3.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream3 to HeatExchanger1
sim.ConnectObjects(MaterialStream2.GraphicObject, AdiabaticExpanderCompressor1.GraphicObject, -1, -1)  # MaterialStream2 to AdiabaticExpanderCompressor1
sim.ConnectObjects(MaterialStream5.GraphicObject, HeaterCooler2.GraphicObject, -1, -1)  # MaterialStream5 to HeaterCooler2
sim.ConnectObjects(HeaterCooler2.GraphicObject, EnergyStream3.GraphicObject, -1, -1)  # HeaterCooler2 to EnergyStream3
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream6.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream6
sim.ConnectObjects(MaterialStream4.GraphicObject, HeatExchanger1.GraphicObject, -1, -1)  # MaterialStream4 to HeatExchanger1
sim.ConnectObjects(HeaterCooler1.GraphicObject, MaterialStream3.GraphicObject, -1, -1)  # HeaterCooler1 to MaterialStream3
sim.ConnectObjects(MaterialStream7.GraphicObject, Valve1.GraphicObject, -1, -1)  # MaterialStream7 to Valve1
sim.ConnectObjects(Valve1.GraphicObject, MaterialStream8.GraphicObject, -1, -1)  # Valve1 to MaterialStream8
sim.ConnectObjects(AdiabaticExpanderCompressor1.GraphicObject, MaterialStream1.GraphicObject, -1, -1)  # AdiabaticExpanderCompressor1 to MaterialStream1
sim.ConnectObjects(HeaterCooler2.GraphicObject, MaterialStream7.GraphicObject, -1, -1)  # HeaterCooler2 to MaterialStream7
sim.ConnectObjects(HeatExchanger1.GraphicObject, MaterialStream5.GraphicObject, -1, -1)  # HeatExchanger1 to MaterialStream5
sim.ConnectObjects(HeaterCooler1.GraphicObject, EnergyStream2.GraphicObject, -1, -1)  # HeaterCooler1 to EnergyStream2
sim.AutoLayout()  
 # Save the flowsheet 
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "gen_1.xml")
 
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
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "img_1.png")
 
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

