from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # find '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])   # number before '#'
            i = j + 1               # start of string
            j = i + length         # end of string

            res.append(s[i:j])
            i = j

        return res