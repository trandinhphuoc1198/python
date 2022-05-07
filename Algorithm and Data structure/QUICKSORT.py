def quicksort(arr,start,end):
    pivot=start
    print(f'start: {start} end: {end} array {arr[start:end+1]} ')
    vecx,vecy=0,1
    while start!=end:
        print(f'start {start} pivot {pivot} end {end} arr{arr} ')
        if arr[end]<arr[pivot] and vecy==1:
            arr[end],arr[pivot],pivot=arr[pivot],arr[end],end
            vecx,vecy=vecy,vecx
            continue
        elif arr[start]>arr[pivot] and vecx==1:
            arr[start],arr[pivot],pivot=arr[pivot],arr[start],start
            vecx,vecy=vecy,vecx
            continue
        start,end=start+vecx,end-vecy
    print(f'pivot {pivot}')
    return pivot
def partition(arr,start,end):
    
    if start<end:
        
        
        c=quicksort(arr,start,end)
        partition(arr,start,c-1)
        partition(arr,c+1,end)
        

a=[3,7,2,1,9,0,5]
partition(a,0,len(a)-1)
print(a)