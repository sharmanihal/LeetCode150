       # Initialize variables to store the total product and count of zeros.
        total_product = 1
        zero_count = 0
        
        # Iterate through the array to calculate the total product and count zeros.
        for num in nums:
            if num:
                # If the number is not zero, update the total product.
                total_product *= num
            else:
                # If the number is zero, increment the zero count.
                zero_count += 1
                
        # If there are more than one zero in the array, all elements in the output will be zero.
        if zero_count > 1:
            return [0] * len(nums)
        
        # Initialize an empty list to store the output.
        output = []
        
        # Iterate through the array again to calculate the product except self for each element.
        for num in nums:
            if num and zero_count:
                # If the number is non-zero and there are zeros in the array, the output for this element will be zero.
                output.append(0)
            elif num and not zero_count:
                # If the number is non-zero and there are no zeros in the array,
                # the output for this element will be the total product multiple by the current number raised to power -1.
                output.append(int(total_product * pow(num,-1)))
            else:
                # If the number is zero, the output for this element will be the total product.
                output.append(total_product)
                
        # Return the final output list.
        return output
    
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix:| 1 | a | a * b | a * b * c |
        postfix: |b * c * d |  c * d | d | 1 |
        res=[[1]*[b*c*d], [a]*[c*d],[a*b]*[d],[a*b*c]*[1]]
        
        """
        # Initialize prefix product and result array
        prefix_product = 1
        result = [1] * len(nums)
        
        # Calculate prefix products
        for i in range(len(nums)):
            # Update result with product of elements before current element (prefix product)
            result[i] = result[i] * prefix_product
            # Update prefix product by multiplying it with the current element
            prefix_product = prefix_product * nums[i]
        
        # Reset postfix product and calculate postfix products
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            # Update result with product of elements after current element (postfix product)
            result[i] = result[i] * postfix_product
            # Update postfix product by multiplying it with the current element
            postfix_product = postfix_product * nums[i]
        
        return result
