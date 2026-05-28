class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if ch == "+":
                    stack.append(int(val1 + val2))
                elif ch == "-":
                    stack.append(int(val1 - val2))
                elif ch == "/":
                    stack.append(int(val1 / val2))
                elif ch == "*":
                    stack.append(int(val1 * val2))
        return stack.pop()