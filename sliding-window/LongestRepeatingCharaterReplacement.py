# https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq = [0] * 26
        maxlen = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord("A")] += 1
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
