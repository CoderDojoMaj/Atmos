import serial, serial.tools.list_ports
from multiprocessing import Process
from Utils import sprint


def readT(data):
    tok=""
    temp=""
    tempStart=False
    for char in data:
        sprint(char, tok)
        tok+=char
        if tok == "TEMP = ":
            tempStart=True
            tok=""
        elif tempStart==True:
            if char in list("0123456789."):
                temp+=char
            elif char=="º" or char=="C":
                tempStart=False
            tok=""
    return temp

def readP(data):
    tok=""
    temp=""
    tempStart=False
    for char in data:
        sprint(char, tok)
        tok+=char
        if tok == "PRES = ":
            tempStart=True
            tok=""
        elif tempStart==True:
            if char in list("0123456789."):
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
        sprint(char, tok)
        tok+=char
        if tok == "HUM = ":
            humStart=True
            tok=""
        elif humStart==True:
            if char in list("0123456789."):
                hum+=char
            elif char=="%":
                humStart=False
            tok=""
    return hum

##def readW(data):
##    tok=""
##    wat=""
##    watStart=False
##    for char in data:
##        tok+=char
##        if tok == "WATER = ":
##            watStart=True
##            tok=""
##        elif watStart==True:
##            if char in list("0123456789"):
##                wat+=char
##            elif char=="%":
##                watStart=False
##            tok=""
##    return wat

def readL(data):

    tok=""
    light=""
    lightStart=False
    for char in data:
        sprint(char, tok)
        tok+=char
        if tok == "LIGHT = ":
            lightStart=True
            tok=""
        elif lightStart==True:
            if char in list("0123456789."):
                light+=char
            elif char=="%":
                lightStart=False
            tok=""
    sprint(light)
    return light


def readTHWL(data):
    sprint(data)
    t=readT(data[0])
    h=readH(data[1])
    p=readP(data[2])
    l=readL(data[3])
    return t,h,l,p
i = 0
for port in serial.tools.list_ports.comports():
    sprint(i, port.device)
    i = i + 1
p = input('Select the port number: ')
arduino = serial.Serial(serial.tools.list_ports.comports()[int(p)].device, 9600)
sprint('Serial port open')
data=[]

def readArduino(data=[]):
    rawString = arduino.readline()
    data=rawString.decode('unicode_escape')
    data=data[:-2]
    data=data.split(";")
    return data


p=Process(target=readArduino)
p.start()
