# https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxlen = 0
        l = r = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
