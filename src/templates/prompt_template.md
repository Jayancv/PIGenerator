You aim to design a DWSIM diagram with Python DWSIM library for a given process described in the text prompt. 
Please ensure your designed process diagram works properly and achieves the requested requirements in the description. 

Here is an example:

## Question 
A process for gas liquefaction, particularly nitrogen liquefaction, which combines the use of a nitrogen 
auto-refrigeration cooling cycle with one or more closed-loop refrigeration cycles using two or more refrigerant 
components. The closed-loop refrigeration cycle provide refrigeration in a temperature range having a lowest 
temperature between about -125◦F. and about -250◦F. A nitrogen expander cycle provides additional refrigeration, 
a portion of which is provided at temperatures below the lowest temperature of the closed-loop or recirculating 
refrigeration cycle or cycles. The lowest temperature of the nitrogen expander cycle refrigeration range is between 
about -220◦F. and about -320◦F. The combined use of the two different refrigerant systems allows each system to operate 
most efficiently in the optimum temperature range, thereby reducing the power consumption required for liquefaction.
Gaseous nitrogen at 80◦F, 1 atm is compressed to 25 atm pressure. Adiabatic compressor is employed for this purpose 
with 50% efficiency which also results in increasing the temperature of N2 stream to 1577◦F. The stream is further 
cooled to -306◦F with the help of a series of cooler and heat exchanger. Cooled N2 is further expanded by reducing the 
pressure to 1 atm using an isenthalpic valve to obtain liquefied N2.


## Answer

### Task 1

#### Components Needed
- **Compressor**: C1
- **Expansion valve**: V1
- **Heat exchanger**: HE-009
- **Cooler**: Col1, Col2

#### Stage 1: Flow

### Task 2

```python
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
print(errors)

```


As you have seen, the output of your designed topology should consist of two tasks:
1. Give a detailed design plan about all devices and their interconnectivity nodes and properties.
2. Write a complete DWSIM Python code and run the calculation. 


Please make sure your Python code is compatible with DWSIM. 
Please give the runnable code without any placeholders based one some configs in above code.




