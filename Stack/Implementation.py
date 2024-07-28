# Using Class

class Stack:
    def __init__(self,n):
        self.n=n
        self.l=[0]*(n+1)
        self.top=-1
    def isFull(self):
        if self.top==self.n-1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def push(self,data):
        if self.isFull():
            print("Stack is full")
        else:
            self.top+=1
            self.l[self.top]=data
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.l[self.top])
            self.l[self.top]=0
            self.top-=1
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.l[self.top])
    
s=Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.peek()


# Using builtin methods

stack=[]
def push(data):
    stack.append(data)
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack.pop())
def peek():
    if len(stack)==0:
        print("Empty")
    else:
        print(stack[-1])
push(1)
push(2)
push(3)
pop()
peek()

# Using deque from collections module
from collections import deque

stack=deque()
def push(data):
    stack.append(data)
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack.pop())
def peek():
    if len(stack)==0:
        print("Empty")
    else:
        print(stack[-1])
push(1)
push(2)
push(3)
pop()
peek()

# Using LifoQueue from queue module
from queue import LifoQueue

n=int(input("Enter maxsize="))
stack=LifoQueue(maxsize=n)
def push(data):
    if stack.full():
        print("Stack is full")
    else:
        stack.put(data)
def pop():
    if stack.empty():
        print("Stack is empty")
    else:
        print(stack.get())
def peek():
    if stack.empty():
        print("Stack is empty")
    else:
        top = stack.get()
        print(top)
        stack.put(top)
push(1)
push(2)
push(3)
pop()
peek()


# USing linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        NewNode=Node(data)
        if self.head:
            NewNode.next=self.head
            self.head=NewNode
        else:
            self.head=NewNode
            
    def pop(self):
        if self.head:
            temp=self.head
            if temp.next:
                self.head=temp.next
                
            else:
                self.head=None
            temp=None
        else:
            print("Empty linked list")
    def peek(self):
        if self.head:
            print(self.head.data)
        else:
            print("Empty linked list")
        
    def PrintList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

list=LinkedList()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.pop()
list.pop()
list.PrintList()
list.peek()
