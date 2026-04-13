# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr_one = list1
        curr_two = list2

        while curr_one and curr_two:
            if curr_one.val > curr_two.val:
                curr.next = curr_two 
                curr_two = curr_two.next
            else:
                curr.next = curr_one
                curr_one = curr_one.next
            curr = curr.next
        
        if curr_one:
            curr.next = curr_one
        elif curr_two:
            curr.next = curr_two

        return dummy.next