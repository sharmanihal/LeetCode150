class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the candidate and its count
        candidate, count = nums[0], 1
        
        # Iterate through the rest of the array
        for num in nums[1:]:
            # Check if the current number is the same as the candidate
            if candidate == num:
                # Increment count if the current number is the same as the candidate
                count += 1
            else:
                # If count becomes 0, update the candidate and reset count to 1
                if count == 0:
                    candidate, count = num, 1
                else:
                    # Decrement count if the current number is different from the candidate
                    count -= 1
        
        # The final candidate is the majority element
        return candidate
"""
Explanation:

1. The code uses the Boyer-Moore Voting Algorithm to find the majority element in the array.

2. It initializes `candidate` with the first element of the array and `count` to 1.

3. It iterates through the array starting from the second element.

4. For each element, it checks if the current element is the same as the `candidate`. If yes, it increments the `count`.

5. If the current element is different from the `candidate`, it checks if the `count` becomes 0. If so, it updates the `candidate` to the current element and resets the `count` to 1.

6. If the `count` is not 0, it decrements the `count` since the current element is different from the `candidate`.

7. The final result is the `candidate`, which is the majority element in the array.

This algorithm works under the assumption that the majority element always exists in the array, as stated in the problem description.
                
"""

