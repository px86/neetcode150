# https://neetcode.io/problems/anagram-groups?list=neetcode150

# BEGIN_NOTE
#
# I was making this mistake. The following line creates 'len(strs)' references
# to the same inner list. So change in one element shows up in all of them.
#   alphafreqs = [[0] * 26] * len(strs)
# Correct way would be:
#   alphafreqs = [[0] * 26 for _ in range(len(strs))]
# Also, [0] * 26 works, because 0 is an immutable int value
#
# END_NOTE


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphafreqs = [[0] * 26 for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                alphafreqs[i][ord(c) - ord("a")] += 1
        solution = {}
        for i, alphafreq in enumerate(alphafreqs):
            key = tuple(alphafreq)  # can not hash a list
            if key in solution:
                solution[key].append(strs[i])
            else:
                solution[key] = [strs[i]]
        return list(solution.values())
