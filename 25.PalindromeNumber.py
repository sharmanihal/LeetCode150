
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check for special cases where x is not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_num = x
        
        # Reverse the second half of x and compare with the first half
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # For odd-length numbers, the middle digit does not matter
        # So we can remove it from reversed_num by dividing it by 10
        return x == reversed_num or x == reversed_num // 10
"""
Explanation:
1. The function `isPalindrome` takes an integer `x` as input and returns `True` if `x` is a palindrome and `False` otherwise.
2. The initial check ensures that negative numbers and numbers ending with zero (except zero itself) are not palindromes. For example, `-121` and `120` are not palindromes.
3. Inside the `while` loop, the function reverses the second half of `x` and stores it in the variable `reversed_num`. The loop continues until `x` is less than `reversed_num`, which means we've reached the midpoint of the number.
4. For even-length numbers, `reversed_num` will be equal to the first half of `x`. For odd-length numbers, `reversed_num` will be one digit ahead of the first half of `x`. To handle this, we check if `x` is equal to `reversed_num` or `reversed_num` with the last digit removed (`reversed_num // 10`).
5. If the conditions in step 4 are met, we return `True`, indicating that `x` is a palindrome. Otherwise, we return `False`.
"""

