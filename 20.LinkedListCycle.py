class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty
        if not head:
            return False
        
        # Initialize two pointers, slow and fast, both starting at the head of the linked list
        slow, fast = head, head
        
        # Iterate through the linked list using the two pointers
        while fast and fast.next:
            # Move the slow pointer one step at a time
            slow = slow.next
            # Move the fast pointer two steps at a time
            fast = fast.next.next
            
            # Check if the slow pointer meets the fast pointer, indicating a cycle
            if slow == fast:
                return True
        
        # If the loop completes without meeting pointers, there is no cycle
        return False
"""
This code uses the "tortoise and hare" approach to detect a cycle in a linked list. 
The slow pointer advances one node at a time, while the fast pointer advances two nodes at a time. 
If there is a cycle, the fast pointer will eventually catch up to the slow pointer. 
If there is no cycle, the fast pointer will reach the end of the list. 
This algorithm has a time complexity of O(n) where n is the number of nodes in the linked list.
"""

