import os
import glob
import time
from bluetooth import *
import socket
import bluetooth


wait = 0.001
#F4:42:8F:10:5F:5F
connection = False
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#uuid = "00001101-0000-1000-8000-00805F9B34FB"
advertise_service( server_sock, "raspberrypi",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]  
                    )
while True:        
        if(connection == False):
            print("Waiting for connection on RFCOMM channel %d" % port)
            client_sock, client_info = server_sock.accept()
            connection = True
            print("Accepted connection from ", client_info)
        try:  
            data = client_sock.recv(1024)
            print(data)
            if data == "disconnect":
                print("Client wanted to disconnect")
                client_sock.close()
                connection = False
        except KeyboardInterrupt:
            print("\nDisconnected")
            client_sock.close()
            server_sock.close()
            break
