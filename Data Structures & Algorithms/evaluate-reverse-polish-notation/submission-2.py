class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                int_stack.append(int(token))
            else:
                a = int_stack.pop()
                b = int_stack.pop()
                if token == '+':
                    int_stack.append(b+a)
                elif token == '-':
                    int_stack.append(b-a)
                elif token == '*':
                    int_stack.append(b*a)
                else:
                    int_stack.append(int(b/a))
        
        return int_stack.pop()