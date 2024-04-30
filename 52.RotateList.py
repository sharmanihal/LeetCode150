# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the linked list is empty
        if not head:
            return None
        # Check if the linked list has only one node
        if not head.next:
            return head
        
        # Find the length of the linked list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next

        # If the number of rotations is equal to the size of the linked list, no rotation needs to be performed
        if k % length == 0:
            return head
        k = k % length
        
        # Initialize pointers for rotation
        fast = head
        slow = head
        
        # Move fast pointer ahead by k steps
        for i in range(k):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Set the new head after rotation
        new_head = slow.next
        slow.next = None
        
        # Connect the end of the rotated list to the original head
        current.next = head
        
        return new_head
"""
Explanation:
1. We first check if the linked list is empty or has only one node. If so, there's no need to rotate, and we return the head unchanged.
2. We then find the length of the linked list to determine the number of rotations needed.
3. If the number of rotations is equal to the length of the linked list, it means the list will be rotated back to its original position, so we return the head as it is.
4. Otherwise, we calculate the actual number of rotations needed by taking the modulo of k with the length of the linked list.
5. We then initialize two pointers, fast and slow, both pointing to the head of the linked list.
6. We move the fast pointer k steps ahead.
7. We then move both pointers simultaneously until fast reaches the end of the list.
8. At this point, slow is pointing to the node just before the new head of the rotated list.
9. We set the new head to be slow.next and cut off the connection between slow and the new head.
10. We then connect the end of the rotated list to the original head by making the current node (which is the last node of the original list) point to the original head.
11. Finally, we return the new head of the rotated list.
"""

