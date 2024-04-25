class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to store mapping from original nodes to their copies
        oldToCopy = {None: None}  # Initialize with None: None mapping
        
        # First pass: Create a copy of each node without connecting the random pointers
        cur = head
        while cur:
            # Create a copy of the current node
            copy = Node(cur.val)
            # Store the mapping from original node to its copy
            oldToCopy[cur] = copy
            # Move to the next node in the original list
            cur = cur.next
        
        # Second pass: Connect the next and random pointers of the copied nodes
        cur = head
        while cur:
            # Get the copy node corresponding to the current node
            copy = oldToCopy[cur]
            # Connect the next pointer of the copy to the copy of the next node
            copy.next = oldToCopy[cur.next]
            # Connect the random pointer of the copy to the copy of the random node
            copy.random = oldToCopy[cur.random]
            # Move to the next node in the original list
            cur = cur.next
        
        # Return the head of the copied linked list
        return oldToCopy[head]
"""
Explanation:
1. The solution uses a dictionary `oldToCopy` to map original nodes to their corresponding copies. It initializes with a mapping of `None: None` to handle the case where the `next` or `random` pointer of a node is `None`.
2. In the first pass, it iterates through the original list and creates a copy of each node while storing the mapping in `oldToCopy`.
3. In the second pass, it iterates through the original list again and connects the `next` and `random` pointers of the copied nodes using the mappings stored in `oldToCopy`.
4. Finally, it returns the head of the copied linked list, which is obtained from the mapping `oldToCopy[head]`.
"""

