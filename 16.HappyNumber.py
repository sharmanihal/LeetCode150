
class Solution:
    def isHappy(self, n: int) -> bool:
        # Create a set named 'hashmap' to keep track of encountered numbers
        hashmap = set()

        # Loop will continue until we find a number twice which is not equal to 1
        while n not in hashmap:
            # Add the current number 'n' to the set
            hashmap.add(n)

            # Calculate the sum of the squares of its digits
            n = sum(int(digit) ** 2 for digit in str(n))

            # If the current number is 1, return True as it is a happy number
            if n == 1:
                return True

        # If the loop completes, it means 'n' entered a cycle without reaching 1, so return False
        return False
"""
- The function uses a set named 'hashmap' to keep track of encountered numbers and detect cycles.
- The loop continues until the number 'n' is found in the set or 'n' becomes 1.
- Inside the loop, the sum of the squares of its digits is calculated for each iteration.
- If the current number becomes 1, the function returns True as it is a happy number.
- If the loop completes without finding 1, it means 'n' entered a cycle, and the function returns False.

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # This can also be solved using the cycle detection algorithm
        slow, fast = self.digitSquareSum(n), self.digitSquareSum(self.digitSquareSum(n))
        while slow != fast:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(self.digitSquareSum(fast))
        return fast == 1

    def digitSquareSum(self, n):
        # Function to calculate the sum of the squares of digits in a number
        return sum(int(digit) ** 2 for digit in str(n))
"""
- This solution uses a cycle detection algorithm with two pointers (slow and fast).
- The 'isHappy' function initializes two pointers, 'slow' and 'fast', with the digit square sum of the input 'n'.
- The pointers move at different speeds, and if there is a cycle, they will eventually meet.
- The 'digitSquareSum' function calculates the sum of the squares of digits in a number.
- If the pointers meet at 1, the function returns True as it is a happy number; otherwise, it returns False.
"""
