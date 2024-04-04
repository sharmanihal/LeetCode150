### Solution 1:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Appending the new interval to the existing list of intervals
        intervals.append(newInterval)
        # Sorting the intervals based on the start time
        intervals.sort(key=lambda x: (x[0]))
        # Initializing a list to store the merged intervals
        ans=[intervals[0]]
        # Iterating through the sorted intervals
        for i in range(1,len(intervals)):
            # If the end time of the last interval in ans is greater than or equal to the start time of the current interval
            if ans[-1][1] >= intervals[i][0]:
                # Merge the intervals by updating the end time of the last interval in ans
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                # Otherwise, add the current interval to ans as there's no overlap
                ans.append(intervals[i])
        # Return the list of merged intervals
        return ans
"""
Explanation:
- This solution first appends the new interval to the existing list of intervals.
- Then, it sorts the intervals based on the start time of each interval.
- Next, it initializes a list `ans` with the first interval from the sorted list.
- It then iterates through the sorted intervals and merges overlapping intervals by updating the end time of the last interval in `ans`.
- Finally, it returns the list of merged intervals.
"""

### Solution 2:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize pointers for binary search
        start, end = 0, len(intervals) - 1
        position = 0

        # Perform binary search to find the correct position to insert the new interval
        while start <= end:
            mid = (start + end) // 2
            if intervals[mid][0] == newInterval[0]:
                position = mid
                break
            elif intervals[mid][0] > newInterval[0]:
                end = mid - 1
            else:
                start = mid + 1

        # If position is not found, set it to the start pointer
        if not position:
            position = start

        # Insert the new interval at the correct position
        intervals.insert(position, newInterval)
        ans = [intervals[0]]

        # Merge overlapping intervals
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        # Return the list of merged intervals
        return ans
"""
Explanation:**
- This solution uses binary search to find the correct position to insert the new interval within the existing list of intervals.
- Once the position is found, it inserts the new interval at that position.
- Then, it merges overlapping intervals similar to Solution 1 by iterating through the intervals and updating the end time of the last interval if there's an overlap.
- Finally, it returns the list of merged intervals.

Both solutions achieve the same result, but Solution 1 uses sorting to ensure the intervals are in ascending order, while Solution 2 uses binary search to find the correct insertion position.
"""
