class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        # Check if the last digit plus one results in carry
        if digits[index] + 1 == 10:
            carry = 1
            # Iterate backwards to handle carry
            while index >= 0 and digits[index] + carry == 10:
                digits[index] = 0
                index -= 1
            # If there are still digits left and no carry
            if index >= 0:
                digits[index] += carry
                carry = 0
            # If carry remains after iterating through all digits, add a new digit
            if carry:
                digits.insert(0, 1)
            return digits
        else:
            # If the last digit plus one does not result in carry, simply add one to it
            digits[index] += 1
            return digits
"""
Explanation:
1. The function `plusOne` takes a list of digits as input and returns a list of digits after incrementing the number by one.
2. The index variable is initialized to the index of the last digit in the list.
3. The solution first checks if adding one to the last digit results in a carry. If it does, it enters the loop to handle the carry.
4. Inside the loop, it iterates backwards through the digits, setting each digit to 0 if a carry is generated. The loop continues until either all digits are processed or there is no carry left.
5. After exiting the loop, if there are remaining digits and no carry, it adds the carry to the appropriate digit.
6. Finally, if there is still a carry remaining after iterating through all digits, it inserts a new digit with a value of 1 at the beginning of the list.
7. If adding one to the last digit does not result in a carry, it simply increments the last digit by one.
8. The function then returns the updated list of digits.
"""


