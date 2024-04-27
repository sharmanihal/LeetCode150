# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to simplify handling edge cases
        dummy = ListNode(0, head)
        leftprev = dummy  # Initialize a pointer to the node before the left position
        curr = head  # Start from the head of the list

        # 1. Reach Node at position left
        for i in range(left - 1):
            leftprev = curr  # Move leftprev to the node before the left position
            curr = curr.next  # Move curr to the left position

        prev = None  # Initialize a pointer to track the previous node during reversal

        # Now curr is at the "left" position and leftprev is the node before left

        # 2. Reverse from left to right
        for i in range(right - left + 1):  # Reverse the sublist from left to right
            temp = curr.next  # Store the next node of curr
            curr.next = prev  # Reverse the pointer of curr
            prev = curr  # Move prev to curr
            curr = temp  # Move curr to the next node

        # Update pointers to reconnect the reversed sublist with the original list
        leftprev.next.next = curr  # Connect the node after "right" to curr
        leftprev.next = prev  # Connect leftprev to the "right" node, which is now prev

        # Return the modified list (excluding the dummy node)
        return dummy.next
"""
Explanation:

1. Dummy Node: The dummy node helps simplify the process by allowing us to handle cases where the reversal happens from the first node.

2. Traversal to Left Position: We traverse the list until we reach the node just before the left position. This allows us to correctly reconnect the reversed sublist later.

3. Reversal: We reverse the sublist from left to right using a standard reversal technique. During this process, we keep track of the previous node to correctly adjust the pointers.

4. Reconnecting Pointers: After the reversal, we reconnect the pointers:
   - The next pointer of the node before the left position (leftprev) is connected to the "right" node (prev), which is the last node of the reversed sublist.
   - The next pointer of the last node of the reversed sublist is connected to the node after the "right" position (curr).

5. Return: Finally, we return the modified list, excluding the dummy node.
"""

