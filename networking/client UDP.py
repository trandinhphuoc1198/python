import socket,time
ip=socket.gethostbyname(socket.gethostname())
port=9999
ser=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ser.sendto('hello'.encode('utf-8'),(ip,port))
while True:
    a,b=ser.recvfrom(2048)
    print(a.decode('ascii'))
