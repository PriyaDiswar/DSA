"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

 
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

#Using time-O(N) and space-O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if head is None or head.next is None:
                return head
            New_Node=reverse(head.next)
            front=head.next
            front.next=head
            head.next=None
            return New_Node
        
        def middle(head):
            s=head
            f=head
            while f.next and f.next.next:
                s=s.next
                f=f.next.next

            new_head=reverse(s.next)
            first=head
            second=new_head

            while second:
                if second.val!=first.val:
                    reverse(new_head)
                    return False

                first=first.next
                second=second.next
            reverse(new_head)
            return True
        
        if head is None or head.next is None:
            return True
        else:
            return middle(head)





             OR


#using time-O(N) and space-O(N)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        count=1
        while temp.next:
            count+=1
            temp=temp.next
        temp=head
        lis=[]
        for i in range(count//2):
            lis.append(temp.val)
            temp=temp.next
        if count%2:
            temp=temp.next
        i=-1
        while temp:
            if temp.val!=lis[i]:
                return False
            i-=1
            temp=temp.next
        return True
