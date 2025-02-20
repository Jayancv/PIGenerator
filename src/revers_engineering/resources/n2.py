import clr

# Adding references for necessary DWSIM libraries
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

# Create automation manager and a new flowsheet
interf = Automation3()
sim = interf.CreateFlowsheet()

# Select nitrogen as the main component
nitrogen = sim.AvailableCompounds["Nitrogen"]
sim.SelectedCompounds.Add(nitrogen.Name, nitrogen)

# Add material streams and unit operations
# Inlet stream
m1 = sim.AddObject(ObjectType.MaterialStream, 50, 50, "inlet")
m1 = m1.GetAsObject()
m1.SetTemperature(80 + 273.15)  # 80°F to K
m1.SetPressure(1 * 101325)      # 1 atm to Pa
m1.SetMassFlow(1.0)             # Mass flow rate in kg/s (adjust as necessary)

# Compressed stream after compressor
m2 = sim.AddObject(ObjectType.MaterialStream, 150, 50, "compressed")
m2 = m2.GetAsObject()

# Cooled stream after cooler
m3 = sim.AddObject(ObjectType.MaterialStream, 200, 50, "cooled")
m3 = m3.GetAsObject()

# Outlet stream (liquefied nitrogen)
m4 = sim.AddObject(ObjectType.MaterialStream, 250, 50, "outlet")
m4 = m4.GetAsObject()

# Energy stream for compressor
e1 = sim.AddObject(ObjectType.EnergyStream, 100, 150, "power")
e1 = e1.GetAsObject()

# Compressor setup (adiabatic)
compressor = sim.AddObject(ObjectType.Compressor, 100, 100, "compressor")
compressor = compressor.GetAsObject()
compressor.Efficiency = 0.50  # 50% efficiency
compressor.OutletPressure = 25 * 101325  # 25 atm to Pa
compressor.CalcMode = UnitOperations.Compressor.CalculationMode.OutletPressure

# Heat exchanger (cooler)
cooler = sim.AddObject(ObjectType.HeatExchanger, 100, 200, "cooler")
cooler = cooler.GetAsObject()
cooler.HeatTransferArea = 100  # Example area for heat exchanger

# Expansion valve (for isenthalpic expansion)
expansion_valve = sim.AddObject(ObjectType.Expander, 100, 300, "expansion valve")
expansion_valve = expansion_valve.GetAsObject()
expansion_valve.OutletPressure = 1 * 101325  # 1 atm to Pa

# Connect objects in sequence
sim.ConnectObjects(m1.GraphicObject, compressor.GraphicObject, -1, -1)  # Inlet to compressor
sim.ConnectObjects(compressor.GraphicObject, m2.GraphicObject, -1, -1)  # Compressor to compressed stream
sim.ConnectObjects(m2.GraphicObject, cooler.GraphicObject, -1, -1)      # Compressed stream to cooler
sim.ConnectObjects(cooler.GraphicObject, m3.GraphicObject, -1, -1)      # Cooler to cooled stream
sim.ConnectObjects(m3.GraphicObject, expansion_valve.GraphicObject, -1, -1)  # Cooled stream to expansion valve
sim.ConnectObjects(expansion_valve.GraphicObject, m4.GraphicObject, -1, -1)  # Expansion valve to outlet

# Automatically arrange layout
sim.AutoLayout()

# Property Package for Nitrogen (Peng-Robinson suitable for nitrogen liquefaction)
nitrogen_pp = PropertyPackages.PengRobinsonPropertyPackage()
sim.AddPropertyPackage(nitrogen_pp)

# Set calculation mode and execute flowsheet calculations
Settings.SolverMode = 0
errors = interf.CalculateFlowsheet2(sim)

# Save the flowsheet to a file
fileNameToSave = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "taskName.xml")
interf.SaveFlowsheet(sim, fileNameToSave, False)

# Export PFD image
clr.AddReference(dwsimpath + "SkiaSharp.dll")
clr.AddReference("System.Drawing")

from SkiaSharp import SKBitmap, SKImage, SKCanvas, SKEncodedImageFormat
from System.IO import MemoryStream
from System.Drawing import Image
from System.Drawing.Imaging import ImageFormat

# Render PFD to image
PFDSurface = sim.GetSurface()
bmp = SKBitmap(1024, 768)
canvas = SKCanvas(bmp)
PFDSurface.UpdateCanvas(canvas)
d = SKImage.FromBitmap(bmp).Encode(SKEncodedImageFormat.Png, 100)
str = MemoryStream()
d.SaveTo(str)
image = Image.FromStream(str)
imgPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "taskName1.png")
image.Save(imgPath, ImageFormat.Png)
str.Dispose()
canvas.Dispose()
bmp.Dispose()

# Show the PFD image
from PIL import Image as PILImage
im = PILImage.open(imgPath)
im.show()