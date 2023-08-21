import requests
import time
import json
import serial
import threading

connection = serial.Serial(port="/dev/ttyUSB2", baudrate=9600)
connection.flush()

def counting(ids):
    # COUNTING MESIN 
    getParamResponse = requests.get(
        'https://berli.aplikasipms.com/api/latestParamM{}'.format(ids)).json()
    getTipeValue = getParamResponse['data'][0]['tipe_benda']
    getStateValue = getParamResponse['data'][0]['state']
    getResponse = requests.get(
        "https://berli.aplikasipms.com/api/latestAvailability?machine_id={}".format(ids)).json()
    opTime = getResponse['data'][0]['state']

    if (getStateValue == 1 and opTime == 1):
        if (getTipeValue == "A"):
            responseA1 = requests.put(
                'https://berli.aplikasipms.com/api/processed?m_id={}&tipe=A'.format(ids))
            responseA = requests.put(
                'https://berli.aplikasipms.com/api/kurangiStock?m_id={}&A=1'.format(ids))
        elif (getTipeValue == "B"):
            responseB1 = requests.put(
                'https://berli.aplikasipms.com/api/processed?m_id={}&tipe=B'.format(ids))
            responseB = requests.put(
                'https://berli.aplikasipms.com/api/kurangiStock?m_id={}&B=1'.format(ids))
        elif (getTipeValue == "C"):
            responseC1 = requests.put(
                'https://berli.aplikasipms.com/api/processed?m_id={}&tipe=C'.format(ids))
            responseC = requests.put(
                'https://berli.aplikasipms.com/api/kurangiStock?m_id={}&C=1'.format(ids))
        else:
            pass

def pzem(data):
    try:
        dataSend = json.loads(data)
        voltage = dataSend['voltage']
        current = dataSend['current']
        power = dataSend['power']
        energy = dataSend['energy']
        frequency = dataSend['frequency']
        pf = dataSend['pf']
        responsePZEM = requests.post('https://berli.aplikasipms.com/api/insertEnergy', json={
            'voltage': voltage,
            'current': current,
            'power': power,
            'energy': energy,
            'frequency': frequency,
            'pf': pf
        })
    except:
        pass

def processData(data):
    try:
        if data.strip() == 'count1':
            counting(1)
        if data.strip() == 'count2':
            counting(2)
        if data.strip() == 'count3':
            counting(3)
        if data.strip() == 'count4':
            counting(4)
    except:
        pass

while True:
    data = connection.readline().decode("utf-8").rstrip()
    threading.Thread(target = processData, args = (data,)).start()
    threading.Thread(target = pzem, args = (data,)).start()
    



    
# starttime = time.time()
# counting(1)
# endtime = time.time()
# elapsedtime = endtime - starttime
# print("start:{:.2f} - end:{:.2f}, speed response count1 = {:.2f} detik".format(starttime,endtime,elapsedtime))