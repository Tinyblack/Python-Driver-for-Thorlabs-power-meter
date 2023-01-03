
1) Two ways of utilising the dynamic link library (*.dll) files provided by Thorlabs:

    _> Copy *.dll file needed to this folder (e.g. Thorlabs.TLPM_64.Interop.dll)

    _> Provide a libraryPath when calling ThorlabsPowerMeter.listDevices() (e.g. ThorlabsPowerMeter.listDevices(libraryPath)).

2) According to the manual provided by Thorlabs, usually the files will be at: 
C:\Program Files\IVI Foundation\VISA\VisaCom64\Primary Interop Assemblies\Thorlabs.TLPM_64.Interop.dll

3) "Thorlabs.TLPMX_64.Interop.dll" is not suitable for this program, please use "Thorlabs.TLPM_64.Interop.dll" only
