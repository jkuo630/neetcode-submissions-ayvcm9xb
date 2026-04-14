# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # while theres more than 1 list, 
        # merge 2 lists at a time 
        if not lists:
            return None
            
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                mergedList.append(self.mergeLists(list1, list2))
            lists = mergedList
        return lists[0]
    
    def mergeLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> List[Optional[ListNode]]:
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
        if curr_two:
            curr.next = curr_two 
        
        return dummy.next