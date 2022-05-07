a=[0,1,2,3,4]
def bubble_sort(a):
   for idx in range(len(a)):
      for idx2 in range(idx,len(a)):
         if a[idx]<a[idx2]:
            a[idx],a[idx2]=a[idx2],a[idx]
bubble_sort(a)
print(a)