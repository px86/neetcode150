# https://neetcode.io/problems/median-of-two-sorted-arrays?list=neetcode150


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            left1 = nums1[i] if i >= 0 else float("-infinity")
            right1 = nums1[i + 1] if i < len(nums1) - 1 else float("infinity")

            left2 = nums2[j] if j >= 0 else float("-infinity")
            right2 = nums2[j + 1] if j < len(nums2) - 1 else float("infinity")

            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
