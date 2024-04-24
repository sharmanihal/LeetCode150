class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Initialize a stack to store directories
        
        # Split the input path by '/' characters
        # Example: "/../abc//./def/" -> [' ', '..', 'abc', ' ', '.', 'def', ' ']
        for i in path.split('/'):
            if i == '..':  # If encountered '..', pop the top directory from stack
                if stack:
                    stack.pop()
            elif i != '' and i != '.':  # If i is not empty or '.', it's a valid directory name
                stack.append(i)  # Append it to the stack
        
        # Join the directories in the stack with '/' as separator and add '/' at the beginning
        # to form the simplified canonical path
        return '/' + '/'.join(stack)
