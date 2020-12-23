import wmi
import time
import datetime

def measure_temp ():
    t = "=53.0*C" # os.popen("vcgencmd measure_temp").readline()
    temp_string = t
    temp_int = int(temp_string.replace("temp", "").split(".")[0][1:])
    temp_far = int((temp_int * 9 / 5) + 32)
    temp_far_str = ''.join(['CPU TEMP (', str(datetime.datetime.now()), '): ', str(temp_far), '.0', u'\u00b0', 'F'])
    return (temp_far_str)

if __name__=='__main__':
    w = wmi.WMI(namespace="root\\wmi")
    t0 = w.get('MSAcpi_ThermalZoneTemperature')
    t = t0.wmi_property('CurrentTemperature')
    print((t / 10) - 273.2)
