
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string 's' into a list of words
        arr = s.split(' ')
        
        # Create dictionaries to store mappings between characters in 'pattern' and words in 's'
        hashmap_p = {}
        hashmap_s = {}

        # Check if the lengths of 'arr' and 'pattern' are equal, if not, return False
        if len(arr) != len(pattern):
            return False

        # Iterate through each character in 'pattern' and its corresponding word in 'arr'
        for i in range(len(pattern)):
            # Check the mapping from pattern to string
            if pattern[i] in hashmap_p and hashmap_p[pattern[i]] != arr[i]:
                return False
            # Check the mapping from string to pattern
            if arr[i] in hashmap_s and hashmap_s[arr[i]] != pattern[i]:
                return False
            # Update the mappings
            hashmap_p[pattern[i]] = arr[i]
            hashmap_s[arr[i]] = pattern[i]

        # If the loop completes, it means a bijection exists, so return True
        return True
"""
Explanation:

- The `wordPattern` function checks if there is a bijection between characters in 'pattern' and words in 's'.
- It uses two dictionaries (`hashmap_p` and `hashmap_s`) to store mappings in both directions.
- It splits the string 's' into a list of words ('arr').
- It checks if the lengths of 'arr' and 'pattern' are equal. If not, it means there cannot be a bijection, so it returns False.
- It iterates through each character in 'pattern' and its corresponding word in 'arr':
  - It checks if the current character is already mapped to a different word in 'hashmap_p'.
  - It checks if the current word is already mapped to a different character in 'hashmap_s'.
  - If either condition is met, it returns False.
  - Otherwise, it updates the mappings in both dictionaries.
- If the loop completes, it means a bijection exists, and the function returns True.

This solution efficiently checks whether 's' follows the same pattern as specified by the input 'pattern'.
"""
