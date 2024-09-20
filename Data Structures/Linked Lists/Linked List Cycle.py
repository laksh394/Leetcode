"""Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that 
pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False

"""Note: The main idea to solve the question of detecting a cycle in a singly-linked list is to use the concept 
of two pointers: a "slow" pointer that moves one step at a time and a "fast" pointer that moves two steps at a time. By having 
these two pointers traverse the list simultaneously if there is a cycle, the fast pointer will eventually catch up to the slow pointer. 
If there is no cycle, the fast pointer will reach the end of the list."""

