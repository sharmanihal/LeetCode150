class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns for validity
        for i in range(9):
            row_set = set()  # Set to store numbers encountered in the current row
            col_set = set()  # Set to store numbers encountered in the current column
            
            for j in range(9):
                # Check for duplicate numbers in the current row
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if num in row_set or num > 9:
                        return False
                    row_set.add(num)
                
                # Check for duplicate numbers in the current column
                if board[j][i].isdigit():
                    num = int(board[j][i])
                    if num in col_set or num > 9:
                        return False
                    col_set.add(num)
        
        # Check subgrids for validity
        subgrid_combinations = [
            [[0, 1, 2], [0, 1, 2]],
            [[0, 1, 2], [3, 4, 5]],
            [[0, 1, 2], [6, 7, 8]],
            [[3, 4, 5], [0, 1, 2]],
            [[3, 4, 5], [3, 4, 5]],
            [[3, 4, 5], [6, 7, 8]],
            [[6, 7, 8], [0, 1, 2]],
            [[6, 7, 8], [3, 4, 5]],
            [[6, 7, 8], [6, 7, 8]]
        ]
        
        for combo in subgrid_combinations:
            subgrid_set = set()  # Set to store numbers encountered in the current subgrid
            
            # Iterate through the cells of the current subgrid
            for i in combo[0]:
                for j in combo[1]:
                    if board[i][j].isdigit():
                        num = int(board[i][j])
                        if num in subgrid_set or num > 9:
                            return False
                        subgrid_set.add(num)
        
        # If all checks pass, the Sudoku is valid
        return True
           
            
        
