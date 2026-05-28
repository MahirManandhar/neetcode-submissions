class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(eval(f"{val1}{ch}{val2}")))
        return stack.pop()