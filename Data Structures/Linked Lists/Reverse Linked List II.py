"""Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes 
of the list from position left to position right, and return the reversed list.

Example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
