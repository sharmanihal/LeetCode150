### Solution 1: Sorting

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Easy nlogn Solution
        if len(nums) == 0:
            return 0
        
        # Remove duplicates and sort the list
        nums = list(set(nums))
        nums.sort()
        
        maxCount = 1
        count = 1
        
        # Traverse the sorted list and find consecutive elements
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 1
        
        return maxCount
"""
Explanation:
1. The solution begins by handling the edge case where the input list is empty, returning 0 as the longest consecutive sequence length.
2. Duplicates are removed from the list using a set to ensure each number is considered only once.
3. The list is sorted to arrange the numbers in ascending order.
4. A variable `maxCount` is initialized to track the maximum consecutive sequence length found so far.
5. A variable `count` is initialized to track the current consecutive sequence length.
6. Iterate through the sorted list, checking if the current number and the previous number form a consecutive sequence.
7. If they do, increment the `count` and update `maxCount` accordingly.
8. If they don't, reset `count` to 1.
9. Finally, return `maxCount` as the result.
"""

### Solution 2: HashSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxCount = 0
        
        for i in nums:
            if i - 1 not in hashset:
                num = i
                count = 0
                
                # Count consecutive elements starting from the current number
                while num in hashset:
                    count += 1
                    num += 1
                
                maxCount = max(maxCount, count)
        
        return maxCount
"""
Explanation:
1. This solution utilizes a hashset to efficiently check for the presence of numbers in the input list.
2. The hashset `hashset` is created using the input list `nums`.
3. Initialize `maxCount` to 0 to track the maximum consecutive sequence length found.
4. Iterate through each number in `nums`.
5. For each number `i`, check if `i - 1` is not in the `hashset`. If this condition holds, it means `i` is the start of a consecutive sequence.
6. Initialize `num` to `i` and `count` to 0.
7. Iterate while `num` is present in the `hashset`, incrementing `count` and `num` to find consecutive elements.
8. Update `maxCount` with the maximum value between `maxCount` and `count`.
9. Finally, return `maxCount` as the result.
"""
