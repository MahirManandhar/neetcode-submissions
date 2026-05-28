class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b, 
            "*": lambda a,b: a * b,
            "/": lambda a,b: a / b
        }
        stack = []
        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(ops[ch](val1,val2)))
        return stack.pop()