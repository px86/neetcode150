# https://neetcode.io/problems/is-anagram?list=neetcode150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = s.lower()
        t = t.lower()
        alphafreq_s = [
            0,
        ] * 26
        alphafreq_t = [
            0,
        ] * 26
        for i in range(len(s)):
            alphafreq_s[ord(s[i]) - 97] += 1
            alphafreq_t[ord(t[i]) - 97] += 1
        return alphafreq_s == alphafreq_t
