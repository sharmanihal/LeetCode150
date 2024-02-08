class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  Check if the lengths of 's' and 't' are not equal, if so, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create a Counter for the characters in 's'
        hashmap_s = Counter(s)
        
        # Iterate through each character in 't'
        for i in t:
            # Check if the character is not in 'hashmap_s' or its frequency is already 0
            if i not in hashmap_s or hashmap_s[i] == 0:
                return False
            # Decrease the frequency of the character in 'hashmap_s'
            hashmap_s[i] -= 1

        # If the loop completes, 't' is an anagram of 's', so return True
        return True
"""
Explanation:

- The `isAnagram` function checks if two strings, 's' and 't', are anagrams of each other.
- It first checks if the lengths of 's' and 't' are equal. If not, they cannot be anagrams, so it returns False.
- It uses the `Counter` class to create a dictionary-like object (`hashmap_s`) to store the frequency of each character in 's'.
- It then iterates through each character in 't':
  - It checks if the character is not in 'hashmap_s' or its frequency is already 0. If either condition is met, it returns False.
  - Otherwise, it decreases the frequency of the character in 'hashmap_s'.
- If the loop completes, it means all characters in 't' have corresponding characters in 's' with the same frequencies, so 't' is an anagram of 's', and the function returns True.

This solution efficiently checks whether 't' is an anagram of 's'.
"""
