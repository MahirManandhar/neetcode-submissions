class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trim = ""
        for ch in s:
            if ch.isalnum():
                s_trim += ch.lower()
        for i in range(len(s_trim)//2):
            l = i
            r = len(s_trim) - 1 - i
            if s_trim[l] != s_trim[r]:
                return False
        return True
        