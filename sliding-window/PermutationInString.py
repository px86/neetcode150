# https://neetcode.io/problems/permutation-string?list=neetcode150


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0] * 26
        for char in s1:
            s1freq[ord(char) - ord("a")] += 1

        winfreq = [0] * 26
        l = 0
        for r in range(len(s2)):
            winfreq[ord(s2[r]) - ord("a")] += 1
            if winfreq == s1freq:
                return True
            if (r - l + 1) == len(s1):
                winfreq[ord(s2[l]) - ord("a")] -= 1
                l += 1
        return False
