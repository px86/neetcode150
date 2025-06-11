# https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        l = r = 0
        while l <= r and r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                win_len = r - l + 1
                if win_len > max_len:
                    max_len = win_len
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        return max_len
