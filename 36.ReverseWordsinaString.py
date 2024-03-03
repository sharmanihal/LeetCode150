class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0  # Initialize index to traverse the string
        res = ''  # Initialize an empty string to store the reversed words
        
        # Loop through the string
        while i < len(s):
            # Skip leading spaces
            while i < len(s) and s[i] == " ":
                i += 1
            
            sub = ""  # Initialize an empty string to store each word
            
            # Extract each word
            while i < len(s) and s[i] != " ":
                sub += s[i]  # Append non-space characters to form a word
                i += 1
            
            # Add the extracted word to the result string with a leading space
            if sub != "":
                res = " " + sub + res
        
        # Return the result string with leading space removed
        return res[1:]
    
    
    
"""
Explanation:
- It initializes an index `i` to traverse the input string `s` and an empty string `res` to store the reversed words.
- The outer `while` loop iterates through the string `s`.
- The first nested `while` loop skips leading spaces in the string.
- The second nested `while` loop extracts each word from the string and appends it to the `sub` variable.
- After extracting a word, it adds it to the beginning of the `res` string with a leading space.
- Finally, it returns the result string with the leading space removed.
- The function handles cases with leading/trailing spaces and multiple consecutive spaces between words.
"""
