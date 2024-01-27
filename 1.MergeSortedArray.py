class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
      
        # Initialize pointers for nums1, nums2, and the index to merge at in nums1
        pointer_nums1, pointer_nums2 = m - 1, n - 1
        merge_index = len(nums1) - 1
        
        # Iterate while both arrays have elements to compare
        while pointer_nums1 >= 0 and pointer_nums2 >= 0:
          
            # If the current element in nums1 is greater or equal, place it at merge_index
            if nums1[pointer_nums1] >= nums2[pointer_nums2]:
                nums1[merge_index] = nums1[pointer_nums1]
                pointer_nums1 -= 1
            else:
                # If the current element in nums2 is greater, place it at merge_index
                nums1[merge_index] = nums2[pointer_nums2]
                pointer_nums2 -= 1
         
            # Move the merge_index to the left
            merge_index -= 1
        
        # If there are remaining elements in nums2, add them to nums1
        while pointer_nums2 >= 0:
            nums1[merge_index] = nums2[pointer_nums2]
            merge_index -= 1
            pointer_nums2 -= 1

'''
Explanation:
1. The code initializes pointers (`pointer_nums1`, `pointer_nums2`) for the end of `nums1` and `nums2`, and `merge_index` for the position to merge elements in `nums1`.

2. It then iterates through the arrays in reverse order, comparing elements and placing the greater one at `merge_index` in `nums1`. This is done until either `nums1` or `nums2` is fully processed.

3. After the first loop, if there are remaining elements in `nums2`, they are added to the beginning of `nums1` since they are already sorted.

The key concept here is to iterate from the end of the arrays towards the beginning, using pointers to keep track of the current elements being compared. This allows for an in-place modification of `nums1`.
'''
