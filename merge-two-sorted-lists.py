# https://leetcode.com/problems/merge-two-sorted-lists/submissions/885026073/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        tail = merged

        while list1 and list2:
            if(list1.val < list2.val):
                tail.next = list1 
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1 
        elif list2:
            tail.next = list2 
        
        return merged.next

             
        