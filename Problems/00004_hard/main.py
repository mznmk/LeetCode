#
# 4. Median of Two Sorted Arrays
#

from typing import List

# ============================================================================ #

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # create new list
        nums = []
        for v in nums1:
            nums.append(v)
        for v in nums2:
            nums.append(v)
        nums.sort()

        # determine median-index
        median_index1 = (1 + len(nums)) // 2
        if len(nums) % 2 == 1:
            median_index2 = median_index1
        else:
            median_index2 = median_index1 + 1

        # calculate median
        median = (nums[median_index1 - 1] + nums[median_index2 - 1]) / 2

        # return answer
        return median
        
# ============================================================================ #

cls = Solution()

ans = cls.findMedianSortedArrays([1,3],[2])
print(ans == 2.00000)

ans = cls.findMedianSortedArrays([1,2],[3,4])
print(ans == 2.500000)

ans = cls.findMedianSortedArrays([0,0],[0,0])
print(ans == 0.00000)

ans = cls.findMedianSortedArrays([],[1])
print(ans == 1.00000)

ans = cls.findMedianSortedArrays([2],[])
print(ans == 2.00000)
