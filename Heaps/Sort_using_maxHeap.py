def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[i]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def MaxHeap(arr):
    size=len(arr)
    for i in range(size//2-1,-1,-1):
        heapify(arr,size,i)
def sort(arr):
    #for ascending order
    size=len(arr)
    res=[]
    for i in range(size):
        MaxHeap(arr)
        res.append(arr[0])
        arr.pop(0)
    print(res)
    
    #for ascending order
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    print(arr)
    
    #for descending order
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(1,n):
        heapify(arr[i:],n,i)
    print(arr)
arr=list(map(int,input().split()))
sort(arr)
