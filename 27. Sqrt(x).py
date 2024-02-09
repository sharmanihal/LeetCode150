class Solution:
    def mySqrt(self, num: int) -> int:
        # Initialize the start and end pointers for binary search
        start = 0
        end = num // 2 + 1
        # Initialize a variable to store the previous result
        prev = 0
        
        # Binary search loop
        while start <= end:
            # Calculate the middle value
            mid = (start + end) // 2
            # Calculate the square of the middle value
            prod = mid * mid
            
            # Check if the square of the middle value equals the input number
            if prod == num:
                return mid
            # If the square is greater than the input number, adjust the end pointer
            elif prod > num:
                end = mid - 1
            # If the square is smaller than the input number, adjust the start pointer
            else:
                # Store the current middle value as the previous result
                prev = mid
                start = mid + 1
        
        # Return the previous result (the largest integer less than or equal to the square root)
        return prev
"""
The binary search is performed within the range `[0, num//2 + 1]`, as the square root of `num` cannot be greater than `num // 2 + 1`. The loop iterates until the start pointer exceeds the end pointer. During each iteration, it calculates the square of the middle value and compares it with the input number. Based on the comparison, it adjusts the start or end pointer accordingly. Finally, it returns the previous result, which represents the largest integer less than or equal to the square root of `num`.
"""
