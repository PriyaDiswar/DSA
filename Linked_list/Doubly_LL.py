class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def InsertAtBegin(self,data):
        NewNode=Node(data)
        if self.head:
            NewNode.next=self.head
            self.head.prev=NewNode
            self.head=NewNode
        else:
            self.head=NewNode
    
    
    def InsertAtEnd(self,data):
        NewNode=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            NewNode.prev=temp
            temp.next=NewNode
            
        else:
            self.head=NewNode
        
        
    def InsertAtPos(self,data,pos):
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
                    if temp.next:
                        temp.next.prev=NewNode
                    NewNode.prev=temp
                    NewNode.next=temp.next
                    temp.next=NewNode
                
                else:
                    print("Not valid index")
        else:
            self.head=NewNode
            
    
    def Insert_after_val(self,data,val):
        NewNode=Node(data)
        if self.head:
            temp=self.head
            while temp:
                if temp.data==val:
                    if temp.next:
                        temp.next.prev=NewNode
                    NewNode.next=temp.next
                    NewNode.prev=temp
                    temp.next=NewNode
                    break
                temp=temp.next
            else:
                print("value not found")
        else:
            print("Empty")
            
            
    def DeleteAtBegin(self):
        if self.head:
            if self.head.next:
                temp=self.head
                self.head=temp.next
                self.head.prev=None
                temp=None
                
            else:
                self.head=None
        else:
            print("Empty")    
            
    def DeleteAtEnd(self):
        if self.head:
            if self.head.next:
                temp=self.head
                # while temp.next.next:
                #     temp=temp.next
                # temp.next=None
                while temp.next:
                    temp=temp.next
                temp.prev.next=None
                
            else:
                self.head=None
        else:
            print("Empty")
            
            
    def DeleteAtPos(self,pos):
        if self.head:
            if pos==0:
                self.DeleteAtBegin()
            else:
                temp=self.head
                i=0
                while temp and i<pos-1:
                    temp=temp.next
                    i+=1
                if temp.next:
                    if temp.next.next:
                        temp.next.next.prev=temp
                        temp.next=temp.next.next
                    else:
                        temp.next=None
                else:
                    print("Index not possible")
        else:
            print("empty linked list")
            
    def DeleteByVal(self,val):
        if self.head:
            if self.head.data==val:
                self.DeleteAtBegin()
            else:
                
                temp=self.head    
                while temp:
                    if temp.data==val:
                        if temp.next:
                            temp.prev.next=temp.next
                            temp.next.prev=temp.prev
                        else:
                            temp.prev.next=None
                    temp=temp.next
                else:
                    print("value not found")
        else:
            print("Empty")
                
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
list.InsertAtPos(70,5)
list.Insert_after_val(80,30)
list.DeleteAtBegin()
list.DeleteAtEnd()
list.DeleteAtEnd()
list.DeleteAtPos(5)
list.DeleteByVal(90)
list.PrintList()
