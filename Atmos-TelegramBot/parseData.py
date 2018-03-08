import serial, time, serial.tools.list_ports
from multiprocessing import Process



def readT(data):
    tok=""
    temp=""
    tempStart=False
    for char in data:
        tok+=char
        if tok == "TEMP = ":
            tempStart=True
            tok=""
        elif tempStart==True:
            if char in list("0123456789"):
                temp+=char
            elif char=="º" or char=="C":
                tempStart=False
            tok=""
    return temp

def readH(data):
    tok=""
    hum=""
    humStart=False
    for char in data:
        tok+=char
        if tok == "HUM = ":
            humStart=True
            tok=""
        elif humStart==True:
            if char in list("0123456789"):
                hum+=char
            elif char=="%":
                humStart=False
            tok=""
    return hum

def readW(data):
    tok=""
    wat=""
    watStart=False
    for char in data:
        tok+=char
        if tok == "WATER = ":
            watStart=True
            tok=""
        elif watStart==True:
            if char in list("0123456789"):
                wat+=char
            elif char=="%":
                watStart=False
            tok=""
    return wat

def readL(data):
    tok=""
    light=""
    lightStart=False
    for char in data:
        tok+=char
        if tok == "LIGHT = ":
            lightStart=True
            tok=""
        elif lightStart==True:
            if char in list("0123456789"):
                light+=char
            elif char=="%":
                lightStart=False
            tok=""
    return light


def readTHWL(data):
    print(data)
    t=readT(data[0])
    h=readH(data[1])
    w=readW(data[2])
    l=readL(data[3])
    return t,h,w,l

arduino = serial.Serial(serial.tools.list_ports.comports()[0].device, 9600)
data=[]

def readArduino(data):
    rawString = arduino.readline()
    data=rawString.decode('unicode_escape')
    data=data[:-2]
    data=data.split(";")
    return data
    
        
p=Process(target=readArduino)
p.start()
