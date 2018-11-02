def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    
    L = [0]*n1
    R = [0]*n2
    
    for i in range(0,n1):
        while l>=0 and l<r:
            arr[l] = arr[l+i]
    
    for j in range(0,n2):
        while r>=0 and r<m:
            arr[r] = arr[m+1+j]
            

def mergeSort(arr, l, r):
    m = (l + (r-1))/2
    merge(0, l, m, r)
    mergeSort(arr, l, m+1)
    mergeSort(m-1, 0, arr)
    
arr = [15, 9, 60, 44, 12, 1, 4]
mergeSort(arr)

for i in range(len(arr)):
    print("%d" % arr[i])