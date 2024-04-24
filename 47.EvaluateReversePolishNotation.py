class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to hold operands
        stack = []
        
        # Iterate through each token in the input list
        for i in tokens:
            # If the token is an operator '+'
            if i == '+':
                # Pop the top two elements from the stack, add them, and push the result back onto the stack
                stack.append(int(stack.pop()) + stack.pop())
            # If the token is an operator '-'
            elif i == '-':
                # Pop the top two elements from the stack, subtract them, and push the result back onto the stack
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            # If the token is an operator '*'
            elif i == '*':
                # Pop the top two elements from the stack, multiply them, and push the result back onto the stack
                stack.append(stack.pop() * stack.pop())
            # If the token is an operator '/'
            elif i == '/':
                # Pop the top two elements from the stack, divide them (truncating towards zero), and push the result back onto the stack
                num1 = stack.pop()
                stack.append(int(stack.pop() / num1))
            # If the token is an operand (integer)
            else:
                # Convert the operand to an integer and push it onto the stack
                stack.append(int(i))
        
        # The final result is the only element left in the stack
        return stack[-1]
"""
Explanation:
- The code implements the evaluation of an arithmetic expression in Reverse Polish Notation (RPN).
- It uses a stack to store operands and intermediate results.
- It iterates through each token in the input list.
- When encountering an operator, it pops the required number of operands from the stack, performs the operation, and pushes the result back onto the stack.
- When encountering an operand, it simply pushes it onto the stack.
- Finally, it returns the top element of the stack, which is the result of the expression.
"""

