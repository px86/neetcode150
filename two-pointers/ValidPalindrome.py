# https://neetcode.io/problems/is-palindrome?list=neetcode150


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            l = s[i].lower()
            h = s[j].lower()
            if l != h:
                return False
            i += 1
            j -= 1
        return True
