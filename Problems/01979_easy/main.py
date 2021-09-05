#
# 1979. Find Greatest Common Divisor of Array
#

from typing import List

# ============================================================================ #

class Solution:
    def gcd_euclidian(self, a:int, b:int) ->int:
        # base case
        if b == 0:
            return a
        # recursive
        return self.gcd_euclidian(b, a%b)

    def findGCD(self, nums: List[int]) -> int:
        # determine GCD
        nums.sort()
        ans = self.gcd_euclidian(nums[0], nums[-1])
        # return
        return ans

# ============================================================================ #

cls = Solution()

ans = cls.findGCD([2,5,6,9,10])
print(ans == 2)

ans = cls.findGCD([7,5,6,8,3])
print(ans == 1)

ans = cls.findGCD([3,3])
print(ans == 3)
