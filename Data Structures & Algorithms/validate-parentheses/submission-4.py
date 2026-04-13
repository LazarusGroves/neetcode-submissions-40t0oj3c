from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = deque()
        for index, char in enumerate(s):
            print(stack)
            if self.isOpen(char):
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif not (self.isClose(char) and self.areSame(stack[-1], char)):
                return False
            else:
                stack.pop()
        return len(stack) == 0

    def isOpen(self, c: str) -> bool:
        return c == '(' or c == '[' or c == '{'
    
    def isClose(self, c: str) -> bool:
        return not self.isOpen(c)

    def areSame(self, a: str, b: str) -> bool:
        return a == '(' and b == ')' or a == '[' and b == ']' or a == '{' and b == '}'