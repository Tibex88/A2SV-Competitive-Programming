# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/884375036/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print(head)
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next