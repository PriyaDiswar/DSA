class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def InsertAtBegin(self,data):
        NewNode=Node(data)
        if self.head:
            NewNode.next=self.head
            self.head=NewNode
            self.tail.next=self.head
            
        else:
            self.head=NewNode
            self.tail=NewNode
            NewNode.next=self.head
    
    
    def InsertAtEnd(self,data):
        NewNode=Node(data)
        if self.head:
            self.tail.next=NewNode
            self.tail=NewNode
            self.tail.next=self.head  
        else:
            self.head=NewNode
            self.tail=NewNode
            NewNode.next=self.head
            
            
    def DeleteAtEnd(self):
        if self.head:
            temp=self.head
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            
        else:
            print("Empty")
            
    def PrintList(self):
        temp=self.head
        while temp.next!=self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)
        
list=LinkedList()
list.InsertAtEnd(30)
list.InsertAtEnd(40)
list.InsertAtBegin(20)
list.InsertAtBegin(10)
list.InsertAtEnd(50)
list.DeleteAtEnd()
list.InsertAtBegin(100)
list.PrintList()
