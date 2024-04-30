# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where the head itself is a duplicate
        dummy = ListNode(0, head)
        # Initialize pointers for traversal
        curr = head
        replace = dummy
        
        # Traverse the linked list
        while curr and curr.next:
            # Check if the current node's value is the same as the next node's value
            if curr.val == curr.next.val:
                # Store the value of the duplicate nodes
                value = curr.val
                # Iterate until the current node's value is different from the duplicate value
                while curr and curr.val == value:
                    curr = curr.next
                # Update the pointer of the previous node to skip the duplicate nodes
                replace.next = curr
            else:
                # If the current node is not a duplicate, move both pointers forward
                replace = replace.next
                curr = curr.next
        
        # Return the modified linked list starting from the dummy node's next
        return dummy.next
"""
Explanation:
- A dummy node is created to handle edge cases where the head itself is a duplicate. It acts as a placeholder to simplify the deletion process.
- Two pointers, `curr` and `replace`, are initialized for traversal. `curr` points to the current node being evaluated, and `replace` points to the node before `curr`.
- Traverse the linked list using `curr`, checking for duplicate values.
- If a duplicate value is found, iterate through all consecutive nodes with the same value and update the `replace` pointer to skip these duplicate nodes.
- If no duplicate is found, move both pointers (`curr` and `replace`) forward.
- Finally, return the modified linked list starting from the next node of the dummy node.

"""

