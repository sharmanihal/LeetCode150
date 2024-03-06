"""
Approach 1 : Without Sorting
Explanation:
- It initializes a set `res` to store unique triplets.
- It iterates through the array and fixes one element as `x`.
- For each `x`, it calculates the target value `target` for the inner 2Sum problem.
- It then iterates through the remaining elements and finds two other elements whose sum is equal to the negative of `x`.
- If such complementary values are found, it adds the triplet to the result set `res`.
- It returns the set `res` containing unique triplets.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The idea behind 3Sum is similar to that of 2Sum, where we aim to find three numbers
        that sum up to zero. We fix one number (x), converting the equation to y + z = -x,
        essentially reducing it to a 2Sum problem.
        We then iterate through the array and for each element, find two other elements whose
        sum is equal to the negative of the current element.
        """
        res = set()  # Use a set to store unique triplets
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets
            x = nums[i]  # Fix the value of x
            target = -x  # Calculate the target value for 2Sum
            potential_ks = set()  # Keep track of potential values for the third element
            for j in range(i + 1, len(nums)):
                y = nums[j]
                inner_target = -y  # Calculate the target value for the inner 2Sum
                if target + inner_target in potential_ks:
                    # If the complementary value is found, add the triplet to the result set
                    res.add(tuple(sorted((nums[i], nums[j], target + inner_target))))
                potential_ks.add(nums[j])
        return res



"""
Approach 2 : With Sorting
Explanation:
- It initializes a set `res` to store unique triplets.
- The function sorts the array to simplify the process of finding triplets, since all duplicates will be together in the array instead of distributed.
- It iterates through the array and fixes one element as `x`.
- For each `x`, it calculates the target value `target` for the inner 2Sum problem.
- It then iterates through the remaining elements and finds two other elements whose sum is equal to the negative of `x`.
- If such complementary values are found, it adds the triplet to the result set `res`.
- It returns the set `res` containing unique triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The idea behind 3Sum is similar to that of 2Sum, where we aim to find three numbers
        that sum up to zero. We fix one number (x), converting the equation to y + z = -x,
        essentially reducing it to a 2Sum problem.
        We then iterate through the array and for each element, find two other elements whose
        sum is equal to the negative of the current element.
        """
        res = set()  # Use a set to store unique triplets
        nums.sort()  # Sort the array to simplify the process of finding triplets , and this will also help us in skipping duplicates since all duplicates will be together instead of distributed in the array at diffrent places.
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets
            x = nums[i]  # Fix the value of x
            target = -x  # Calculate the target value for 2Sum
            potential_ks = set()  # Keep track of potential values for the third element
            for j in range(i + 1, len(nums)):
                y = nums[j]
                inner_target = -y  # Calculate the target value for the inner 2Sum
                if target + inner_target in potential_ks:
                    # If the complementary value is found, add the triplet to the result set
                    res.add(tuple((nums[i], nums[j], target + inner_target)))
                potential_ks.add(nums[j])
        return res


