"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 """

#Using time-O(N) and space-O(1)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s=head
        f=head
        for i in range(n):
            f=f.next
        
        if f is None:
            return head.next
        
        while f.next:
            s=s.next
            f=f.next
        
        s.next=s.next.next
        return head




               OR






# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=1
        temp=head
        while temp.next:
            temp=temp.next
            length+=1
        pos=length-n
        curr=head
        for i in range(1,pos):
            curr=curr.next
        
        if pos==0:
            return head.next
        curr.next=curr.next.next
        return head
