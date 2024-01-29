class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Initialize an empty string to store the common prefix
        common = ""

        # Iterate through each character of the first string in the list
        for index, char in enumerate(strs[0]):
            # Check each subsequent string for the current character
            for string in strs[1:]:
                # If the index is beyond the length of the current string
                # or the character at the current index is not equal to the character in the first string,
                # return the common prefix found so far
                if index >= len(string) or string[index] != char:
                    return common

            # If all strings have the same character at the current index, append it to the common prefix
            common += char

        # Return the final common prefix
        return common

"""
Explanation:

1. The function initializes an empty string (common) to store the common prefix.
2. It iterates through each character of the first string in the list (strs[0]).
3. For each character of the first string, it checks the corresponding character in the same position of each subsequent string in the list.
4. If the character is not the same in any of the strings or if the index is beyond the length of a string, it returns the common prefix found so far.
5. If all strings have the same character at the current index, it appends that character to the common prefix.
6. The final common prefix is returned.
"""
