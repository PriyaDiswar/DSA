#Using builtin methods
queue=[]
def enqueue(elem):
    queue.append(elem)
def dequeue():
    if len(queue)!=0:
        print(queue.pop(0))
    else:
        print("Empty queue")
def peek():
    if len(queue)!=0:
        print(queue[0])
    else:
        print("queue is empty")
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
dequeue()
peek()

Output:
10
20
    


#using deque from collections module
from collections import deque
queue=deque()
def enqueue(elem):
    queue.append(elem)
def dequeue():
    if len(queue)!=0:
        print(queue.popleft())
    else:
        print("Empty queue")
def peek():
    if len(queue)!=0:
        print(queue[0])
    else:
        print("Empty queue")
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
dequeue()
peek()

Output:
10
20
        

#using Queue from queue module

from queue import Queue
n=int(input("Enter size of queue: "))
q=Queue(maxsize=n)
def enqueue(elem):
    if q.full():
        print("Queue is full")
    else:
        q.put(elem)
def dequeue():
    if q.empty():
        print("Queue is empty")
    else:
        print(q.get())
def peek():
    if q.empty():
        print("Queue is empty")
    else:
        front = q.get()
        print(front)
        q.put(front)
        for i in range(q.qsize() - 1):
            q.put(q.get())

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
dequeue()
peek()

Output:
Enter size of queue: 4
10
20


#Using Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Enqueue(self,data):
        NewNode=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
                
            temp.next=NewNode
        else:
            self.head=NewNode
    
    def Dequeue(self):
        if self.head:
            temp=self.head
            if temp.next:
                self.head=temp.next
                
            else:
                self.head=None
            temp=None
        else:
            print("Empty Queue")
            
    def Peek(self):
        if self.head:
            print(self.head.data)
        else:
            print("Empty queue")
    def Print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
list=LinkedList()
list.Enqueue(10)
list.Enqueue(20)
list.Enqueue(30)
list.Enqueue(40)
list.Dequeue()
list.Print()
list.Peek()

Output:
20
30
40
20
