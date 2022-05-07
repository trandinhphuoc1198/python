from audioop import mul
import multiprocessing
array=[]
lists=[1,2,3,4]
def add_list(lists):
    lists.append(5)
def cube(num,array1):
    for x,y in enumerate(num):
        array1.append(y*y)
        
if __name__=='__main__':
    with multiprocessing.Manager() as manager:
        lists=manager.list(lists)
        array1=manager.list(array)
        p2=multiprocessing.Process(target=add_list,args=(lists,))
        p2.start()
        p2.join()
        p1=multiprocessing.Process(target=cube,args=(lists,array1))
        p1.start()
        p1.join()
        print(array1)