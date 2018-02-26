import pyserial
ser = serial.Serial('/dev/cu.usbserial-A901HOQC', 19200, timeout=5)
x = ser.read()          # read one byte
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line