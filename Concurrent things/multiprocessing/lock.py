import multiprocessing,os
def plus(num,lock):
    for _ in range(1000):
        lock.acquire()
        num.value+=1
        lock.release()
def minus(num,lock):
    for _ in range(1000):
        
        lock.acquire()
        num.value-=1
        lock.release()
        
def main():
    lock=multiprocessing.Lock()
    num=multiprocessing.Value('i',100)
    p1=multiprocessing.Process(target=plus,args=(num,lock))
    p2=multiprocessing.Process(target=minus,args=(num,lock))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
    print(num.value)
if __name__=='__main__':
    for _ in range(4):
        main()
