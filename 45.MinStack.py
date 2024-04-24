class MinStack:

    def __init__(self):
        # Initialize two stacks: one for storing elements and one for storing minimum values
        self.stack = []  # Stack to store elements
        self.minstack = []  # Stack to store minimum values
        self.min = 0  # Variable to track the current minimum value

    def push(self, val: int) -> None:
        # When pushing a value onto the stack, we update the minimum value if necessary
        if self.stack:
            self.min = min(self.min, val)  # Update minimum value
        else:
            self.min = val  # If the stack is empty, the current value becomes the minimum
        self.minstack.append(self.min)  # Append the current minimum to minstack
        self.stack.append(val)  # Push the value onto the stack

    def pop(self) -> None:
        # When popping an element, we remove it from both stacks
        self.stack.pop()  # Remove the top element from the stack
        self.minstack.pop()  # Remove the corresponding minimum value from minstack
        if self.minstack:
            self.min = self.minstack[-1]  # Update the current minimum to the top of minstack if it exists

    def top(self) -> int:
        # Return the top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum value
        return self.minstack[-1]

"""
Explanation:

- In the `__init__` method, two stacks are initialized: `stack` to store elements and `minstack` to store the minimum values encountered so far. `min` is a variable to keep track of the current minimum value.

- In the `push` method, when a value is pushed onto the stack, we update the current minimum value if necessary. If the stack is not empty, we compare the current value with the current minimum and update `self.min` accordingly. Then, we append the current minimum to `minstack` and push the value onto `stack`.

- In the `pop` method, we simply pop the top element from both `stack` and `minstack`. If `minstack` is not empty after popping, we update `self.min` to the value at the top of `minstack`.

- The `top` method returns the top element of the stack.

- The `getMin` method returns the current minimum value stored in `minstack`.
"""

class MinStack:
    def __init__(self):
        # Initialize the stack to store elements and min to keep track of the current minimum
        self.stack = []
        self.min = 0  # This will be updated as the minimum value in the stack
    
    def push(self, val: int) -> None:
        if not self.stack:  # If stack is empty
            # Append the value and the same value as minimum since it's the only element
            self.stack.append([val, val])
            self.min = val
        else:
            # Update the minimum and append the value along with the current minimum to the stack
            self.min = min(val, self.min)
            self.stack.append([val, self.min])
    
    def pop(self) -> None:
        # Pop the top element from the stack and check if it's the minimum
        if self.stack.pop()[1] == self.min:
            # If it was the minimum, update the minimum to the previous minimum
            if self.stack:
                self.min = self.stack[-1][1]
            else:
                self.min = 0  # If stack becomes empty, reset minimum to 0
    
    def top(self) -> int:
        # Return the top element of the stack
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        # Return the minimum element in the stack
        return self.stack[-1][1]
"""
Explanation:

- push(val): This method pushes an element onto the stack. If the stack is empty, it initializes both the value and the minimum to the given value. If the stack is not empty, it compares the given value with the current minimum and updates the minimum accordingly. It then appends the value along with the current minimum to the stack.

- pop(): This method removes the top element from the stack. If the removed element was the minimum, it updates the minimum to the previous minimum in the stack. If the stack becomes empty after popping, it resets the minimum to 0.

- top(): This method returns the top element of the stack without removing it.

- getMin(): This method returns the minimum element in the stack. Since the minimum is stored along with each element in the stack, it can be retrieved in constant time.

"""


