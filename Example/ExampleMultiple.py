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
