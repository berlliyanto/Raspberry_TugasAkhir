import serial
import requests
import time

ser = serial.Serial('/dev/ttyUSB1',9600)
ser.flush()
#start_time = time.time()
while True:
    #print (time.time()-start_time, "detik")
    time.sleep(1)
    if ser.in_waiting > 0:
        read_serial=ser.readline().decode('utf-8').rstrip()
        if read_serial.strip()!= 'x':
            #starttime = time.time()
            response = requests.post('https://berli.aplikasipms.com/api/insertPressure', json = {'value' : read_serial})
            #endtime = time.time()
            #elapsedtime = endtime - starttime
            #print("start:{:.2f} - end:{:.2f}, speed response pressure({}) = {:.2f} ".format(starttime,endtime,read_serial,elapsedtime))
        
    
