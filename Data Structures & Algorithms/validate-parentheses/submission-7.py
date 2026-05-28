class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '{':'}',
            '(':')',
            '[':']'
        }
        for ch in s:
            if ch in mapping:
                stack.append(mapping[ch])
            elif not stack or stack.pop() != ch:
                    return False
        return len(stack)==0

        