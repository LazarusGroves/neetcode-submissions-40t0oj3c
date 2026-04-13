

class MinStack:
    def __init__(self):
        self.base_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.base_stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.base_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.base_stack.pop()

    def top(self) -> int:
        return self.base_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
