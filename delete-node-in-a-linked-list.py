# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/885011338/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        node.val = node.next.val
        node.next = node.next.next
        temp.next = None