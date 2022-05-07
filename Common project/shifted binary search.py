a=[7,8,9,10,0,1,2,3,4,5]

def fpivot(arr,start,end):
    if arr[start]<arr[end]:
        return -1
    if arr[start]==arr[end]:
        return -2
    mid=(start+end)//2
    if arr[mid]>arr[mid+1]:
        return mid
    if arr[mid] <arr[end]:
        return fpivot(arr,start,mid)
    if arr[mid] >arr[end]:
        return fpivot(arr,mid,end)
def binary(arr,start,end,x):
    while start<=end:
        mid=(start+end)//2
        if arr[mid] ==x:
            return mid,print(mid)
        if arr[mid] <x:
            start=mid+1
        if arr[mid]>x:
            end=mid-1
    return print("Khog tim thay x")

def binarysearch(arr,start,end,x):
    if len(arr)>0:
        pivot=fpivot(arr,start,end)
    else:
        return None
    if pivot==-1 or pivot==-2:
        return binary(arr,start,end,x)
    elif x>arr[end]:
        return binary(arr,start,pivot,x)
    else:
        return binary(arr,pivot,end,x)
binarysearch(a,0,len(a)-1,0)