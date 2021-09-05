#
# 1984. Minimum Difference Between Highest and Lowest of K Scores
#

from typing import List

# ============================================================================ #

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # determine minimum difference
        nums.sort()
        min_diff = 1001001001
        if k == 1:
            min_diff = 0
        else:
            for i in range(len(nums)-(k-1)):
                score_min = nums[i]
                score_max = nums[i+k-1]
                min_diff = min(score_max - score_min, min_diff)
        # return
        return min_diff
        
# ============================================================================ #

cls = Solution()

ans = cls.minimumDifference([90], 1)
print(ans == 0)

ans = cls.minimumDifference([9,4,1,7], 2)
print(ans == 2)

# ---------------------------------------------------------------------------- #

ans = cls.minimumDifference([87063,61094,44530,21297,95857,93551,9918], 6)
print(ans == 74560)

ans = cls.minimumDifference([1730,78090,78197,76063,41072,25772,64973,44059,97954,20449,37462,60265,53283,43481,81501,73746,19123,34867,12144,62845,77983,59895,57157,38916,56188,37623,52200,88411,30711,28715,51323,77016,30741,63977,3071,9129,20313,80290,11220,90641,8553,79604,46684,86482,85661,55637,5453,86799,56086,80546,70214,99889,8780,48720,11455,47179,52401,44928,16540,65339,41927], 52)
print(ans == 76048)