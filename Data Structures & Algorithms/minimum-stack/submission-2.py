class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []   # keeps track of minimums

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If min_stack is empty OR this value is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Repeat the current min to keep sizes equal
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]