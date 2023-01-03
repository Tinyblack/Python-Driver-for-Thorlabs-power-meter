# Python-Driver-for-Thorlabs-power-meter

This is a Python class to control Thorlabs power meters. (Multiple meters are supported)


> For Matlab wrapper, please go the following pages:
>
> * [GitHub Repository](https://github.com/Tinyblack/Matlab-Driver-for-Thorlabs-power-meter)
> 
> * [![View Matlab-Driver-for-Thorlabs-power-meter on File Exchange](https://www.mathworks.com/matlabcentral/images/matlab-file-exchange.svg)](https://uk.mathworks.com/matlabcentral/fileexchange/92803-matlab-driver-for-thorlabs-power-meter)


[Link](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=10562) to a typical Thorlabs Power Meter.

## Package Requirements

* Python
  * Version>=3.10
  * Package required: pythonnet

## User Instructions

1. Download the Optical Power Monitor from the Thorlabs [website](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=OPM). [The latest version is 4.0.4100.700 - Accessed on 01 SEP 2022]
2. Read the manual in the installation folder or the [software help page](https://www.thorlabs.com/software/MUC/OPM/v3.0/TL_OPM_V3.0_web-secured.pdf).
3. Following the instructions in section 9: **Write Your Own Application**. The common path of the *.dll files on Windows is: C:\Program Files\IVI Foundation\VISA\VisaCom64\Primary Interop Assemblies
4. This scripts need only the .net wrapper dll so follow the instruction for C#/.Net.
5. Two ways of utilising the dynamic link library (*.dll) files provided by Thorlabs:

   1. Copy *.dll files needed to ''Thorlabs_DotNet_dll'' folder (e.g. Thorlabs.TLPM_64.Interop.dll).
   2. Provide a libraryPath when calling ThorlabsPowerMeter.listDevices() (e.g. ThorlabsPowerMeter.listDevices(libraryPath)). ["Thorlabs.TLPMX_64.Interop.dll" is not suitable for this program, please use "Thorlabs.TLPM_64.Interop.dll" only]

6. Connect your Power Meter with sensor to the PC USB port and power it on.

7. Please refer to the examples provided (In folder "Example")

## For developers

1. The definition for all the classes can be found in the C# exmple provided by Thorlab. (Shipped together with the software.) [The typical path for x64 system is C:\Program Files (x86)\IVI Foundation\VISA\WinNT\TLPM\Example]

## Example Single Usage

```python
import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from ThorlabsPowerMeter import ThorlabsPowerMeter
import time

if __name__=='__main__':
    _deviceList = ThorlabsPowerMeter.listDevices()
    logger=_deviceList.logger
    deviceA=_deviceList.connect(_deviceList.resourceName[0])
    deviceA.getSensorInfo()
    deviceA.setWaveLength(635);                              
    deviceA.setDispBrightness(0.3);                          
    deviceA.setAttenuation(0);                               
    deviceA.setPowerAutoRange(True);                            
    time.sleep(5)                                                    
    deviceA.setAverageTime(0.001)                           
    deviceA.setTimeoutValue(1000)                               
    #deviceA.darkAdjust() # PM400 ONLY                                   
    #deviceA.getDarkOffset() # PM400 ONLY                                
    for i in range(100):
        deviceA.updatePowerReading(0.1)
        logger.info(f'|{__name__}| {deviceA.meterPowerReading} {deviceA.meterPowerUnit}')
        #deviceA.updateVoltageReading(0.1)  # PM400 ONLY  
        #logger.info(f'|{__name__}| {deviceA.meterVoltageReading} {deviceA.meterVoltageUnit}')  # PM400 ONLY  
    logger.info(f'|{__name__}| Done')                       
    deviceA.disconnect()
```

## Example Multiple Usage

```python
import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from ThorlabsPowerMeter import ThorlabsPowerMeter
import time

if __name__=='__main__':
    _deviceList = ThorlabsPowerMeter.listDevices()
    logger=_deviceList.logger
    deviceA=_deviceList.connect(_deviceList.resourceName[0])
    deviceB=_deviceList.connect(_deviceList.resourceName[1])
    deviceA.getSensorInfo()
    deviceB.getSensorInfo()
    deviceA.setWaveLength(635) 
    deviceB.setWaveLength(780)                            
    deviceA.setDispBrightness(0.3) 
    deviceB.setDispBrightness(0.7)                          
    deviceA.setAttenuation(0)      
    deviceB.setAttenuation(10)                          
    deviceA.setPowerAutoRange(True)
    deviceB.setPowerAutoRange(False)                             
    time.sleep(5)                                                    
    deviceA.setAverageTime(0.001)
    deviceB.setAverageTime(0.01)                           
    deviceA.setTimeoutValue(1000)                             
    deviceB.setTimeoutValue(1000)                               
                             
    for i in range(100):
        deviceA.updatePowerReading(0.1)
        logger.info(f'|{__name__}| A: {deviceA.meterPowerReading} {deviceA.meterPowerUnit}')
        deviceB.updatePowerReading(0.1)
        logger.info(f'|{__name__}| B: {deviceB.meterPowerReading} {deviceB.meterPowerUnit}')
    logger.info(f'|{__name__}| Done')                          
    deviceA.disconnect()
```

## Author Information

* Author: Zimo Zhao
* Dept. Engineering Science, University of Oxford, Oxford OX1 3PJ, UK
* Email: zimo.zhao@eng.ox.ac.uk
* Website: https://eng.ox.ac.uk/smp/
* GitHub: https://github.com/Tinyblack/Python-Driver-for-Thorlabs-power-meter
* Reporting issues and bugs to my GitHub repository is more welcomed.

## Initially Developed On

* Optical Power Monitor
  * Device: PM400
  * Application version: 3.1.3778.562
  * Driver version: TLPM__32 5.1.3754.327
* Python
  * 3.10.5 64-bit

## Latest Test Pass On

* Optical Power Monitor
  * Device: PM400
  * Application version: 4.0.4100.700
  * Driver version: TLPMX__32 5.3.4101.525
* Python
  * 3.10.5 64-bit

## Version History

1.00 ----- 03 Jan 2023 ----- Initial Release
