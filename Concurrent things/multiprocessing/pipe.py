import multiprocessing

def send(conn,msgs):
    for msg in msgs:
        conn.send(msg)
def recv(conn):
    while 1:
        a=conn.recv()
        if a=='end':
            break
        print(a)
if __name__=='__main__':
    parent,child=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=send,args=(parent,['hello','one','end']))
    p2=multiprocessing.Process(target=recv,args=(child,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    