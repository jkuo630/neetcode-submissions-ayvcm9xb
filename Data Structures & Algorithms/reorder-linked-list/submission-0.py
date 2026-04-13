# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use fast and slow pointer to find midpoint 
        # separate into two lists 
        # reverse the second list 
        # iterate between two lists, combining it into one list 
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # now the slow pointer is at the midpoint, detach second half to reverse
        second = slow.next 
        slow.next = None

        # reverse second list
        prev = None
        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp
        
        first = head 
        second = prev 

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2