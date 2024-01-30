class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        i, j = 0, 0

        # Iterate through the characters of both strings
        while i < len(s) and j < len(t):
            # Check if the current characters match
            if s[i] == t[j]:
                # If they match, move to the next character in the subsequence string
                i += 1

            # Move to the next character in the main string
            j += 1

        # Check if all characters in the subsequence were found in order
        return i == len(s)

"""
Explanation:

- The `isSubsequence` function checks if string `s` is a subsequence of string `t`.
- It uses two pointers, `i` for the subsequence `s` and `j` for the main string `t`.
- The function iterates through the characters of both strings using a `while` loop.
- Inside the loop:
  - It checks if the current characters at positions `i` and `j` match.
  - If they match, it means a character from the subsequence has been found, so it moves to the next character in the subsequence by incrementing `i`.
  - It always moves to the next character in the main string by incrementing `j`.
- After the loop, it checks if all characters in the subsequence were found in order (i.e., `i` has reached the length of `s`).
- If all characters in the subsequence are found in order, the function returns `True`; otherwise, it returns `False`.

This solution efficiently determines if `s` is a subsequence of `t` by iterating through both strings using two pointers.
"""
