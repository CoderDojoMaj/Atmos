import serial, time
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
    t=readT(data[0])
    h=readH(data[1])
    w=readW(data[2])
    l=readL(data[3])
    return t,h,w,l

serial_port = input('Serial port: ')
arduino = serial.Serial(serial_port, 9600)
data=""
while True:
    rawString = arduino.readline()
    
    data=rawString.decode('unicode_escape')
    data=data[:-1]
    data=data.split(";")
arduino.close()
