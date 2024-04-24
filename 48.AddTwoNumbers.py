# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize carry to 0
        carry = 0
        # Initialize a new ListNode to store the result, initially set to 0
        l3 = ListNode(0)
        # Initialize a pointer 'curr' to the result ListNode
        curr = l3
        # Iterate over both input linked lists until both are empty
        while l1 or l2:
            # Extract the values of current nodes, if available, otherwise default to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of the current digits and the carry
            sum = val1 + val2 + carry
            # Update the carry for the next iteration
            carry = sum // 10
            # Update the current digit in the result ListNode
            sum = sum % 10
            curr.next = ListNode(sum)
            # Move to the next nodes in both input lists, if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Move the 'curr' pointer to the next node in the result ListNode
            curr = curr.next
        # After the loop, if there is still a carry, create a new node for it
        if carry:
            curr.next = ListNode(carry)
        # Return the result ListNode, excluding the initial dummy node
        return l3.next
"""
Explanation:
- The function `addTwoNumbers` takes two linked lists `l1` and `l2` as input, which represent two non-negative integers.
- It initializes `carry` to 0 and creates a new ListNode `l3` to store the result, initially set to 0.
- It then iterates over both input lists simultaneously until both are empty.
- Within each iteration, it extracts the values of the current nodes (or 0 if the nodes are None), calculates the sum along with the carry, updates the carry for the next iteration, and updates the current digit in the result ListNode.
- It moves to the next nodes in both input lists if available, and moves the `curr` pointer to the next node in the result ListNode.
- After the loop, if there is still a carry, it creates a new node for it.
- Finally, it returns the result ListNode, excluding the initial dummy node.
"""

