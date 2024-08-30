class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtBegin(self,data):
        NewNode=Node(data)
        if self.head:
            NewNode.next=self.head
            self.head=NewNode
        else:
            self.head=NewNode
    def InsertAtEnd(self,data):
        NewNode=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
                
            temp.next=NewNode
        else:
            self.head=NewNode
    def InsertIndex(self,data,pos):
        NewNode=Node(data)
        if self.head:
            if pos==0:
               self.InsertAtBegin(data)
            else:
                temp=self.head
                ind=0
                while temp and ind<pos-1:
                    temp=temp.next
                    ind+=1
                if temp:
                    a=temp.next
                    temp.next=NewNode
                    NewNode.next=a
                else:
                    print("can not insert")
            
        else:
            self.head=NewNode
    
    def count_node(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        print("length=",c)
        
    def max_value(self):
        if self.head:
            temp=self.head
            val=temp.data
            while temp:
                val=max(val,temp.data)
                temp=temp.next
            print("Maximum value is", val)
        else:
            print("Empty")
    def insert_by_val(self,data,val):
        if self.head:
            temp=self.head
            while temp:
                if temp.data==val:
                    newNode=Node(data)
                    newNode.next=temp.next
                    temp.next=newNode
                    break
                temp=temp.next
            print("value Not found")
        else:
            print("Empty")
            
    def delete_begin(self):
        if self.head:
            temp=self.head
            if temp.next:
                self.head=temp.next
                
            else:
                self.head=None
            temp=None
        else:
            print("Empty linked list")
    def delete_end(self):
        if self.head:
            temp=self.head
            if temp.next:
                while temp.next.next:
                    temp=temp.next
                temp.next=None
            else:
                temp=None
        else:
            print("Empty linked list")
            
    def delete_pos(self,pos):
        if self.head:
            temp=self.head
            i=0
            if pos==0:
                self.delete_begin()
            else:
                while temp and i<pos-1:
                    temp=temp.next
                    i+=1
                if temp.next:
                    temp.next=temp.next.next
                else:
                    print("Not possible")
        else:
            print("Empty linked list")
            
    def delete_by_val(self,val):
        if self.head:
            temp=self.head
            if temp.data==val:
                self.head=temp.next
            else:
                prev=None
                while temp:
                    if temp.data==val:
                        temp=prev
                        temp.next=temp.next.next
                    prev=temp
                    temp=temp.next
        else:
            print("Empty linked list")
    
    def reverse(self):
        if self.head is None:
            print("Empty linkedlist")
        elif self.head.next is None:
            print(self.head.data)
        else:
            temp=self.head
            prev=None
            while temp:
                nxt=temp.next
                temp.next=prev
                prev=temp
                temp=nxt
            self.head=prev
            
                
    def PrintList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
list=LinkedList()
list.InsertAtBegin(10)
list.InsertAtBegin(20)
list.InsertAtBegin(30)
list.InsertAtBegin(40)
list.InsertAtEnd(50)
list.InsertIndex(8,5)
list.insert_by_val(70,300)
list.delete_begin()
list.delete_end()
list.delete_pos(6)
list.delete_by_val(50)
list.reverse()
list.PrintList()
list.max_value()
list.count_node()

