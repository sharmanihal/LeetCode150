#Solution 1
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # To find the h-index, we need to find such a number 'h' that there are 'h' papers
        # with at least 'h' citations each.
        
        # Step 1: Count the number of papers for each citation count.
        count = [0] * (max(citations) + 2)
        # We add 2 to handle the edge case where max(citations) is 1,
        # ensuring that the array has size 2 for 0 and 1 citations.
        for i in citations:
            count[i] += 1
        
        # Step 2: Calculate the cumulative sum of the counts in reverse order,
        # to get an array indicating the number of papers with citations greater than or equal to each index.
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]    
            # If we find a point where the citations are greater than or equal to the index,
            # we have found the h-index and return it.
            if count[i] >= i:
                return i
        # If no h-index is found, return 0 as the minimum h-index.
        return 0
"""
Explanation:
1. We first count the number of papers for each citation count using an array called 'count'.
2. We initialize this array to be of size `max(citations) + 2` to handle the edge case where the maximum citation count is 1.
3. We then iterate through the citations and increment the count for each citation count.
4. Next, we calculate the cumulative sum of counts in reverse order. This gives us an array where each index represents the number of papers with citations greater than or equal to that index.
5. While doing this, if we find a point where the number of papers with citations is greater than or equal to the index, we have found the h-index and return it.
6. If no such index is found, we return 0 as the minimum h-index.
"""

#Solution 2
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        We can optimize the size of the count array to match the length of the citations array,
        to avoid unnecessarily large arrays.
        """
        count = [0] * (len(citations) + 2)
        """
        We add 2 to handle the edge case where max(citations) is 1,
        ensuring that the array has size 2 for 0 and 1 citations.
        """
        
        """
        We handle the case where the citation value is greater than or equal to 
        the length of the count array by adding it to the last index of the count array.
        """
        for i in citations:
            if i >= len(count):
                count[-1] += 1
            else:
                count[i] += 1
        
        # Calculate the cumulative sum of the counts in reverse order
        # to get an array indicating the number of papers with citations greater than or equal to each index.
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]    
            # If we find a point where the citations are greater than or equal to the index,
            # we have found the h-index and return it.
            if count[i] >= i:
                return i
        
        # If no h-index is found, return 0 as the minimum h-index.
        return 0
    
#Solution 3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations array in descending order.
        citations.sort(reverse=True)
        
        #For [6, 5, 3, 1, 0], index 2 having 3 citations means there are 2 papers to the left with more citations, since the citations array is sorted in descending order.
        # Iterate through the sorted array with enumerate to get both index and value.
        for index, value in enumerate(citations):
            # If the index is greater than or equal to the citation value,
            # it means there are at least 'index' papers with 'value' or more citations.
            if index >= value:
                # Return the index, which represents the h-index.
                return index
        
        # If the loop completes without finding an h-index, it means all papers have citations greater than their index.
        # In this case, the h-index is equal to the length of the citations array.
        return len(citations)
"""
Explanation:
1. We first sort the citations array in descending order.
2. We iterate through the sorted array using the `enumerate` function, which provides both the index and value of each element.
3. Inside the loop, we check if the index is greater than or equal to the citation value.
4. If it is, it means there are at least 'index' papers with 'value' or more citations.
5. We return the index, which represents the h-index.
6. If the loop completes without finding an h-index, it means all papers have citations greater than their index. In this case, the h-index is equal to the length of the citations array. We return this value as the h-index.

"""


