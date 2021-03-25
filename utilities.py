

"""

UTILITIES MODULE

==============================
|Some degree of documentation|
==============================
This is a module used in the development in VoltOS, for small things that are too small to make it a native program,
and too big to be an external file, or just don't fit anywhere.
Current functions:
loadingbar(how many marks in the loading bar , delay between the marks (defaults to 0.3) [optional param] , character to use (defaults to #) [optional param])
playmusic(path to mp3)
test() [returns 'hello world']
"""


def loadingbar(x,y=0.3,z="#"):
 import time
 print("\n")
 for _ in range(x):
     time.sleep(y)
     print(z, end="",flush=True)
 print("\n")
 print("Done loading")
 print("\n")

def test():
 return 'hello world'
 

def playmusic(x):
 import os
 os.system(str("r" + str(x)))
 print("Playing music")


def launchchatserver():
 import socket
 serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print("| Chat Server for VoltOS | 1.1")
 ip = input("Please input the IP to connect to. (Operating on port 6868. See README.md for more info.)")
 serverSocket.setblocking(0)
 serverSocket.settimeout(10)
 serverSocket.bind((ip,6868))
 serverSocket.listen()
 while True:
     (clientConnected, clientAddress) = serverSocket.accept()
     print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
     msg = input("Type 'quit' to end and type anything else to send a message.")
     if(msg == "quit"):
         clientConnected.close()
     else:
         clientConnected.sendall(msg.encode())

     dataFromClient = clientConnected.recv(1024)
     print(dataFromClient.decode())



def launchchatclient():
 import socket
 clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print("| Chat Client for VoltOS | 1.1")
 ip = input("Please input the IP to connect to. (Operating on port 6868. See README.md for more info.)")
 clientSocket.connect((ip,6868))
 while True:
     dataFromServer = clientSocket.recv(1024)
     print(str(dataFromServer.decode()))
     msg = input("Type 'quit' to end and type anything else to send a message.")
     if(msg == "quit"):
         clientSocket.close()
     else:
         clientSocket.sendall(msg)
         
    

if __name__ == "__main__":
    launchchatserver()
    





