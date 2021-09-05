#
# 1. Two Sum
#

"""
point!
c = a + b
-> b = c - a
"""

from typing import List

# ============================================================================ #

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        index_dict = {}
        for i, v in enumerate(nums):
            if (target - v) in index_dict:
                ans.append(index_dict[target - v])
                ans.append(i)
                break
            else:
                index_dict[v] = i
        return ans

# ============================================================================ #

cls = Solution()

ans = cls.twoSum([2,7,11,15], 9)
print(ans == [0,1])

ans = cls.twoSum([3,2,4], 6)
print(ans == [1,2])

ans = cls.twoSum([3,3], 6)
print(ans == [0,1])
