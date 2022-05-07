import socket
from threading import Thread
connections=[]
ip=socket.gethostbyname(socket.gethostname())
port=9999
ser=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ser.bind((ip,port))
while True:
    data,adress=ser.recvfrom(2048)
    print(data.decode('utf-8'))
    for i in range(100):
        ser.sendto(str(i).encode('utf-8'),adress)