class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = [i for i in s]
        for i in t:
            if i in s_seen:
                s_seen.remove(i)
            else:
                return False
        if not s_seen:
            return True
        else:
            return False
        