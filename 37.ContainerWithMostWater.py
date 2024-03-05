class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater, i, j = 0, 0, len(height) - 1  # Initialize maxwater and two pointers
        while i < j:  # Iterate until the two pointers meet or cross each other
            maxwater = max(maxwater, (j - i) * min(height[i], height[j]))  # Calculate the current area and update maxwater
            if height[i] < height[j]:  # Move the pointer with smaller height towards the other pointer
                i += 1
            else:
                j -= 1
        return maxwater  # Return the maximum water area

"""
Explanation:
- It initializes `maxwater` to 0, and two pointers `i` and `j` at the start and end of the array respectively.
- It iterates through the array using the two pointers and calculates the maximum water area:
  - It calculates the area between the two lines represented by the pointers `i` and `j` using the formula `(j - i) * min(height[i], height[j])`.
  - It updates `maxwater` with the maximum of the current area and the previous maximum.
  - It moves the pointer with the smaller height towards the other pointer, as increasing the width of the container while keeping the height the same can only result in a smaller area.
- After the iteration, it returns the maximum water area stored in `maxwater`

"""

