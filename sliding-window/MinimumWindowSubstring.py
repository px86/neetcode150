# https://neetcode.io/problems/minimum-window-with-characters?list=neetcode150

import string


class Solution:

    def isWindowValid(self, t_freq, win_freq) -> bool:
        for c in string.ascii_letters:
            if t_freq[c] > win_freq[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        tfreq = {c: 0 for c in string.ascii_letters}
        for c in t:
            tfreq[c] += 1

        solution = ""
        minlensolution = len(s) + 1

        l = 0
        winfreq = {c: 0 for c in string.ascii_letters}
        for r in range(len(s)):
            winfreq[s[r]] += 1
            if (r - l + 1) < len(t):
                continue

            if self.isWindowValid(tfreq, winfreq):

                candidate_solution = s[l : r + 1]
                if (r - l + 1) < minlensolution:
                    solution = candidate_solution
                    minlensolution = r - l + 1

                winfreq[s[l]] -= 1
                l += 1

            while l <= r and winfreq[s[l]] > tfreq[s[l]]:
                winfreq[s[l]] -= 1
                l += 1

        return solution
