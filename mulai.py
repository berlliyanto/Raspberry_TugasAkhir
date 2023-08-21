import serial
import requests
import time

class Komdat:
    def __init__(self, mulai):

        self.mulai = mulai
        self.arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
        # self.pressure = serial.Serial(port='COM4', baudrate=9600)

        self.data = ""
        self.hasil = ""
        self.loopback = ""
        self.result = ""

    def sendtoArduino(self, data):

        self.hasil = self.arduino.write(bytes(data, 'utf-8'))
        # print("nilai yang dikirim adalah {}".format(self.hasil))
        time.sleep(0.05)

        # print("hasil")
        # print("response dari arduino adalah {}".format(self.result))
        # print("response dari arduino adalah aaa {}".format(self.loopback))

    def receiveData(self):
        self.loopback = self.arduino.readline().strip()
        self.result = str(self.loopback.decode('utf-8', 'ignore'))

    @property
    def getSendValue(self):
        pass

    @getSendValue.getter
    def getSendValue(self):
        return self.hasil

    @getSendValue.setter
    def getSendValue(self, reset):
        self.hasil = reset

    @property
    def getResult(self):
        pass

    @getResult.getter
    def getResult(self):
        return self.result

    @getResult.setter
    def getResult(self, reset):
        self.result = reset
        
serin = Komdat('connect')
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flush()
start_time = time.time()
while True:
    
    keyM1 = "lockon1"
    time.sleep(2)
    if keyM1 == "lockon1":
        key1 = '1'
        kirim = serin.sendtoArduino(key1)

    else:
        key1 = '0'
        kirim = serin.sendtoArduino(key1)

    #print("loop")
    #print("halo")
    if ser.in_waiting>0:
        read_serial=ser.readline().decode('utf-8').rstrip()
        if read_serial.strip()== 'on1':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=1', json={'status':1})
            print (read_serial)
        if read_serial.strip()== 'off1':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=1', json={'status':0})
            print (read_serial)
        if read_serial.strip()== 'on2':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=2', json={'status':1})
            print (read_serial)
        if read_serial.strip()== 'off2':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=2', json={'status':0})
            print (read_serial)
        if read_serial.strip()== 'on3':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=3', json={'status':1})
            print (read_serial)
        if read_serial.strip()== 'off3':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=3', json={'status':0})
            print (read_serial)
        if read_serial.strip()== 'on4':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=4', json={'status':1})
            print (read_serial)
        if read_serial.strip()== 'off4':
            response = requests.put('https://berli.aplikasipms.com/api/updateStatusM?machine_id=4', json={'status':0})
            print (read_serial)
        
