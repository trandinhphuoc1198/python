import socket,time
from sqlite3 import connect
ip=socket.gethostbyname(socket.gethostname())
port=9999
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    conn.connect((ip,port))