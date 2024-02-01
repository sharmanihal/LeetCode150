class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize two pointers i and j to track the start and end of a potential range
        i, j = 0, 0
        # Initialize an empty list to store the result ranges
        arr = []
        
        # Iterate through the elements of the input array 'nums'
        while j < len(nums):
            # Check if the current element and the next element form a consecutive sequence
            if j < len(nums) - 1 and nums[j + 1] == nums[j] + 1:
                j += 1  # If yes, move the 'j' pointer to the next element
            else:
                # If no, it means the current range has ended
                if i != j:
                    # If the range has more than one element, append "a->b" format to 'arr'
                    arr.append(str(nums[i]) + "->" + str(nums[j]))
                else:
                    # If the range has only one element, append "a" format to 'arr'
                    arr.append(str(nums[i]))
                
                # Update pointers to the next potential range
                i = j + 1
                j += 1
        
        # Return the final list of ranges
        return arr
"""
This code essentially uses two pointers (`i` and `j`) to identify consecutive elements in the input array. When a range ends (i.e., the next element is not part of the current consecutive sequence), it appends the corresponding range to the result list. The final list contains the smallest sorted ranges as per the specified format.
"""

