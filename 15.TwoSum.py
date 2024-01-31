class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements in 'nums'
        hashmap = {}
        
        # Iterate through the elements and their indices in 'nums'
        for index, element in enumerate(nums):
            # Check if the complement (target - element) is already in 'hashmap'
            # and ensure that the index of the complement is not the same as the current index
            if target - element in hashmap and hashmap[target - element] != index:
                # Return the indices of the two numbers that add up to the target
                return [index, hashmap[target - element]]
            
            # Update the 'hashmap' with the current element and its index
            hashmap[element] = index
"""
Explanation:

- The `twoSum` function finds two numbers in the array 'nums' that add up to the given 'target'.
- It uses a dictionary (`hashmap`) to store the indices of elements in 'nums'.
- It iterates through the elements and their indices in 'nums'.
- For each element, it checks if the complement (target - element) is already in 'hashmap'
  and ensures that the index of the complement is not the same as the current index. 
  If both conditions are met, it means a pair of indices has been found, and it returns them.
- If the loop completes, it means no such pair was found, which should not happen based on the problem statement.

This solution efficiently finds a pair of indices whose corresponding elements add up to the target.
"""
