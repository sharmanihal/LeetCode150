# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None (empty tree), the depth is 0.
        if not root:
            return 0
        
        # Recursive call to find the maximum depth of the left subtree.
        lh = self.maxDepth(root.left)
        
        # Recursive call to find the maximum depth of the right subtree.
        rh = self.maxDepth(root.right)
        
        # The depth of the current node is one plus the maximum depth of its left and right subtrees.
        return 1 + max(lh, rh)
"""
Explanation:
1. The `maxDepth` function calculates the maximum depth of a binary tree using recursion.

2. The base case checks if the current node (`root`) is `None`, indicating an empty tree. In this case, the depth is 0.

3. The function then recursively calculates the maximum depth of the left subtree (`lh`) and the right subtree (`rh`).

4. The depth of the current node is determined by adding 1 to the maximum depth of its left and right subtrees.

5. The final result is the maximum depth of the entire binary tree.

The key concept here is the use of recursion to traverse the tree and compute the depth. The depth of each node is determined by the maximum depth of its subtrees. The recursion continues until the base case is reached (an empty tree), and then the depths are calculated in a bottom-up manner.
"""

