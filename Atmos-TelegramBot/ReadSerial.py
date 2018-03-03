import serial, time
port = input("What is the Arduino port?")
baud = input("What is the baud rate? (Default is 9600)")
arduino = serial.Serial(port, baud)
while True:
    time.sleep(2)
    rawString = arduino.readline()
#    bonicastring=str(rawString).split("'")[1]
    bonicastring=rawString.decode('unicode_escape')
    bonicastring=bonicastring[:-1]
    print(str(bonicastring))
arduino.close()
