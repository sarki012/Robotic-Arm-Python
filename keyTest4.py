import tty, sys, termios

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while 1:
    x=sys.stdin.read(1)[0]
    if x == "A":
        print("Up Arrow") 
    elif x == "B":
        print("Down Arrow")
    elif x == "C":
        print("Right Arrow") 
    elif x == "D":
        print("Left Arrow")       
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)