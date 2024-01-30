class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is an empty string
        if not needle:
            # If needle is empty, it's always found at the beginning of haystack
            return 0

        # Get the lengths of needle and haystack
        needle_len = len(needle)
        haystack_len = len(haystack)

        # Iterate through possible starting positions in haystack
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring of haystack at position i and of the same length as needle
            # is equal to the needle
            if haystack[i:i + needle_len] == needle:
                # If it is, return the starting position i
                return i

        # If no match is found, return -1
        return -1
"""
Explanation:

- The `strStr` function looks for a smaller string (`needle`) inside a bigger string (`haystack`).
- If `needle` is empty, it's always found at the beginning of `haystack`, so it returns 0.
- It then goes through each possible starting position in `haystack`.
- For each starting position, it checks if the part of `haystack` starting at that position and having the same length as `needle` is equal to `needle`.
- If it finds a match, it returns the starting position.
- If it goes through all possible positions and doesn't find a match, it returns -1 to indicate that `needle` is not inside `haystack`.

In simpler terms, it's like looking for a smaller word in a bigger sentence and telling where that word starts. If the smaller word is empty, it's always considered to start at the very beginning.

"""

    
