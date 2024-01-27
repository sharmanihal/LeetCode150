
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers, i for iterating through the array and k for handling removals from the end
        i, k = 0, len(nums) - 1
        
        # Iterate through the array as long as i is less than or equal to k
        while i <= k:
            # If the current element is equal to val
            if nums[i] == val:
                # Find the rightmost non-val element from the end of the array
                while k >= 0 and k > i and nums[k] == val:
                    k = k - 1
                
                # Replace the current element with the rightmost non-val element
                nums[i] = nums[k]
                k = k - 1
            
            # Move to the next element in the array
            i += 1
        
        # Return the count of elements not equal to val (k + 1)
        return k + 1
"""
Explanation:
1. The code initializes two pointers, `i` for iterating through the array from the beginning and `k` for handling removals from the end.

2. It iterates through the array using a while loop as long as `i` is less than or equal to `k`.

3. If the current element (`nums[i]`) is equal to the target value (`val`), it finds the rightmost non-target value from the end of the array.

4. It then replaces the current element at `i` with the rightmost non-target value and updates the `k` pointer.

5. The process continues until `i` surpasses `k`.

6. Finally, it returns the count of elements not equal to `val`, which is represented by `k + 1`.

This approach efficiently removes elements equal to the given value in-place and returns the count of elements remaining in the array.
"""
