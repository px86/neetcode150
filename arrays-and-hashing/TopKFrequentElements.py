# https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            if num in freqmap:
                freqmap[num] += 1
            else:
                freqmap[num] = 1
        numsfreqlist = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqmap.items():
            numsfreqlist[freq].append(num)
        result = []
        for nlist in numsfreqlist[-1::-1]:
            for num in nlist:
                result.append(num)
                if len(result) == k:
                    return result
        return result
