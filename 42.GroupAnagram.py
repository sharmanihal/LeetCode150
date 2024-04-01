class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict to store groups of anagrams
        res = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Create an array to count the occurrences of each character in the string
            count = [0] * 26
            
            # Count the occurrences of each character in the string
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Use the counted array as a key for grouping anagrams
            # Anagrams will have the same key (same array of character counts)
            res[tuple(count)].append(s)
        
        # Return the values (lists of anagrams) from the defaultdict
        return res.values()
"""
Explanation:
1. The `groupAnagrams` method takes a list of strings `strs` as input and returns a list of lists containing grouped anagrams.
2. It initializes a `defaultdict` named `res` to store groups of anagrams. This allows us to append anagrams to a list associated with a specific key (character count array).
3. It iterates through each string `s` in the input list `strs`.
4. For each string `s`, it creates an array `count` of size 26 (since there are 26 lowercase English letters) initialized with zeros. This array is used to count the occurrences of each character in the string.
5. It then iterates through each character `c` in the string `s` and increments the corresponding count in the `count` array.
6. After counting the occurrences of each character in the string, it converts the `count` array into a tuple to use it as a key for grouping anagrams.
7. It appends the current string `s` to the list associated with the key (tuple) in the `res` defaultdict.
8. Finally, it returns the values (lists of anagrams) from the defaultdict `res`, which contain grouped anagrams.
"""

