"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
#http://bookshadow.com/weblog/2015/04/24/leetcode-remove-linked-list-elements/
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next=head
        current=dummy
        while current and current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next
