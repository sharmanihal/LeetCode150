class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check if the matrix has only one row, return that row
        if len(matrix)==1:
            return matrix[0]
        # Check if the matrix has only one column, flatten the matrix and return
        if len(matrix[0])==1:
            return [item for sublist in matrix for item in sublist]
        
        # Initialize variables to keep track of boundaries and result list
        first_row=0
        last_column=len(matrix[0])
        last_row=len(matrix)
        first_column=0
        res=[]
        
        # Loop until all elements are visited
        while first_row<=last_row and first_column<=last_column:
            # Traverse from left to right along the top row
            for i in range(first_column,last_column):
                res.append(matrix[first_row][i])
            first_row+=1
            
            # Traverse from top to bottom along the last column
            for j in range(first_row,last_row):
                res.append(matrix[j][last_column-1])
            last_column-=1      
            
            # Traverse from right to left along the last row
            for k in range(last_column-1,first_column-1,-1):
                res.append(matrix[last_row-1][k])
            last_row-=1   
            
            # Traverse from bottom to top along the first column
            for q in range(last_row-1,first_row-1,-1):
                res.append(matrix[q][first_column])
            first_column+=1
        
        # If there are extra elements in the result list, trim it to match the original matrix size
        if len(res)>len(matrix[0])*len(matrix):
            return res[0:len(matrix[0])*len(matrix)]
        return res
