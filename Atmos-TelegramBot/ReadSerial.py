import serial, time
arduino = serial.Serial('COM7', 9600)
while True:
    time.sleep(2)
    rawString = arduino.readline()
#    bonicastring=str(rawString).split("'")[1]
    bonicastring=rawString.decode('unicode_escape')
    bonicastring=bonicastring[:-1]
    print(str(bonicastring))
arduino.close()
