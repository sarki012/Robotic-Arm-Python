from pylibftdi import Device
import threading
from rotateThread import rotateThread
from boomThread import boomThread
import tty, sys, termios

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
#device = Device('FT71VG2G')     #Top USB
device = Device('FT7210GA')     #Bottom USB
device.baudrate = 115200
device.open()
device.write('?\r')             #send an identity query command.
                            #This device needs \r to end command.
x = 0
while 1:
    device.write('E')
    device.write('S')
    device.write('A')
    device.write('R')
    device.write('K')
    x=sys.stdin.read(1)[0]
    if x == "A":
        device.write('u')
        print("Up Arrow") 
    elif x == "B":
        device.write('d')
        print("Down Arrow")
    elif x == "C":
        device.write('r')
        print("Right Arrow") 
    elif x == "D":
        device.write('l')
        print("Left Arrow")       
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)

#if __name__ == "__main__":
# creating thread
#t1 = threading.Thread(target=boomThread, args=(1,))
#t2 = threading.Thread(target=rotateThread, args=(1,))

# starting thread 1
#t1.start()
# starting thread 2
#t2.start()
#device = Device('FTBQ8DAM')
#device.baudrate = 115200
#device.write('?\r')             #send an identity query command.
                            #This device needs \r to end command.
#device.readlines()              #Return data in buffer
#device.close()                  #Close the device

#write an integer
#i = 50
#i.to_bytes