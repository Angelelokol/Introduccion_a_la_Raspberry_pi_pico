import serial

ser = serial.Serial('COM8')

while (True):
    opc = input("1.-Prender Led \n0.-Apagar led\n")
    ser.write((opc + '\n').encode())
    print(ser.readline().decode('utf-8').strip())
