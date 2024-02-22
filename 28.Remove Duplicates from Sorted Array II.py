class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize pointers i and j
        i, j = 0, 0
        
        # Iterate through the array
        while j < len(nums):
            # Initialize count to track the frequency of current number
            count = 1
            
            # Count the frequency of current number
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                count += 1
                j += 1
            
            # Place at most two occurrences of the current number in the array
            for x in range(min(count, 2)):
                nums[i] = nums[j]
                i += 1
            
            # Move to the next number
            j += 1
        
        # Return the length of the modified array
        return i
"""

1. **Initialization of Pointers**: 
    - We start by initializing two pointers `i` and `j` to keep track of positions in the array `nums`. Both pointers are set to 0 initially.
   
   ```python
   i, j = 0, 0
   ```

2. **Iteration through the Array**:
    - We iterate through the array using the pointer `j`. This pointer moves forward to check for duplicates.
    
    ```python
    while j < len(nums):
    ```

3. **Counting Duplicate Occurrences**:
    - Within the loop, we initialize a variable `count` to track the frequency of the current number.
    - We use another loop to count the frequency of the current number while there are consecutive duplicates.
    
    ```python
    count = 1
    while j + 1 < len(nums) and nums[j + 1] == nums[j]:
        count += 1
        j += 1
    ```

4. **Overwriting Duplicates**:
    - After counting the frequency, we ensure that at most two occurrences of the current number are kept.
    - We use a loop to overwrite duplicates with the unique element, up to two occurrences.
    - The `min(count, 2)` ensures that we consider at most two occurrences.
    
    ```python
    for x in range(min(count, 2)):
        nums[i] = nums[j]
        i += 1
    ```

5. **Moving to the Next Number**:
    - Once we have processed the duplicates, we move the `j` pointer to the next distinct number in the array.
    
    ```python
    j += 1
    ```

6. **Returning the Length of Modified Array**:
    - Finally, we return the value of `i`, which represents the length of the modified array containing unique elements.
    
    ```python
    return i
    ```

This approach efficiently removes duplicates in-place while ensuring that each unique element appears at most twice, maintaining the non-decreasing order of the array.
"""
