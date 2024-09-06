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
        
def insert(elem,arr):
    size=len(arr)
    if size==0:
        arr.append(elem)
    else:
        arr.append(elem)
        MaxHeap(arr)
def delete(elem,arr):
    arr.remove(elem)
    MaxHeap(arr)
arr=list(map(int,input().split()))
MaxHeap(arr)
print(arr)
