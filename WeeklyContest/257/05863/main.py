#
# 5863. Count Special Quadruplets
#

from typing import List
import itertools

# ============================================================================ #

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for v in itertools.combinations(nums, 4):
            if v[0] + v[1] + v[2] == v[3]:
                count += 1
        return count
        
# ============================================================================ #

cls = Solution()

ans = cls.countQuadruplets([1,2,3,6])
print(ans == 1)

ans = cls.countQuadruplets([3,3,6,4,5])
print(ans == 0)

ans = cls.countQuadruplets([1,1,1,3,5])
print(ans == 4)
