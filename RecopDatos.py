
import os
import serial

import time


read_command = "$0wn00,70$1"

get_x = "$0wnA4rm$1"

get_y = "$0wnA7rm$1"

get_z = "$0wnAArm$1"

get_all = "$0wnA4mmm$1"

port = '/dev/ttyUSB0'

fo = open("data.txt", "w+")


command = " "
s = serial.Serial(port, 115200, timeout=1)


if s.isOpen() == False:
    s.open()
else:
    s.close()    
    s.open()


    k = 100

#-----------------------------------------------------------

while k > 0:
    #------Get one Measurement command----
    command = read_command
    s.write(command.encode())
    time.sleep(.05)
    #------------ Ends Measurement Command---

    #retrieve data

    command = get_x
    s.write(command.encode())
    respuesta = s.read(6)
    time.sleep(.05)
    x = respuesta.decode('utf-8')
    time.sleep(.05)

    command = get_y
    s.write(command.encode())
    respuesta = s.read(6)
    time.sleep(.05)
    y = respuesta.decode('utf-8')


    time.sleep(.05)
    command = get_z
    s.write(command.encode())
    respuesta = s.read(6)
    time.sleep(.05)
    z = respuesta.decode('utf-8')

    os.system("clear")
    print(  "x= " + x + "  y= " + y + "  z= " + z)
    fo.write("x= " + x + "  y= " + y + "  z= " + z + "\n")
    k = k - 1
    
fo.close()


#-----------------------------------------------------