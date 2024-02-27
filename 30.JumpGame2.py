"""
Greedy approach:
Imagine you're traversing the array, and at each step, you want to take the biggest jump possible to maximize your progress. This is the greedy part. The code identifies the furthest reachable index from the current window using farthest.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the result variable to track the number of jumps needed.
        res = 0
        # Initialize two pointers 'l' and 'r' representing the current range to explore.
        l = r = 0
        
        # Continue jumping until the right pointer reaches the last index.
        while r < len(nums) - 1:
            # Initialize a variable 'farthest' to track the farthest index reachable from the current range.
            farthest = 0
            
            # Iterate over the current range [l, r] to find the farthest index reachable.
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move the left pointer to the next index after the current range.
            l = r + 1
            # Update the right pointer to the farthest index reachable from the current range.
            r = farthest
            # Increment the result variable to count the jump.
            res += 1
        
        # Return the minimum number of jumps needed to reach the last index.
        return res


"""
Explanation:
1. We initialize variables 'res' to track the number of jumps, and 'l' and 'r' to represent the current range to explore.
2. We loop until the right pointer 'r' reaches the last index of the array.
3. Inside the loop, we iterate over the current range [l, r] to find the farthest index reachable.
4. We update the left pointer 'l' to the next index after the current range and set the right pointer 'r' to the farthest index reachable from the current range.
5. We increment the result variable 'res' to count the jump.
6. Finally, we return the minimum number of jumps needed to reach the last index.
"""
