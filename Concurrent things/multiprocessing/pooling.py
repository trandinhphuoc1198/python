import multiprocessing,os,time
def square(n):
    print(n,os.getpid())
    return n*n
mylist=[i for i in range(20)]
if __name__=='__main__':
    p=multiprocessing.Pool()
    result=p.map(square,mylist)