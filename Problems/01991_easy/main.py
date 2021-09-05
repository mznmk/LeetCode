#
# 1991. Find the Middle Index in Array
#

from typing import List

# ============================================================================ #

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        count = len(nums)
        # create cumulative-sum table
        c = [0] * (count+1)
        for i in range(1, count+1):
            c[i] = c[i-1] + nums[i-1]
        # determine middle-index
        middle_index = -1
        for i in range(count):
            # determine left-side sum
            left_sum = 0
            if i != 0:
                left_sum = c[i] - c[0]
            # determine right-side sum
            right_sum = 0
            if i != count-1:
                right_sum = c[count] - c[i+1]
            # is middle-index ?
            if left_sum == right_sum:
                middle_index = i
                break
        # return
        return middle_index
        
# ============================================================================ #

cls = Solution()

ans = cls.findMiddleIndex([2,3,-1,8,4])
print(ans == 3)

ans = cls.findMiddleIndex([1,-1,4])
print(ans == 2)

ans = cls.findMiddleIndex([2,5])
print(ans == -1)

ans = cls.findMiddleIndex([1])
print(ans == 0)

# ---------------------------------------------------------------------------- #

ans = cls.findMiddleIndex([0,0,0,0])
print(ans == 0)
