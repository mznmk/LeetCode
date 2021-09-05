#
# 7. Reverse Integer
#

from typing import List

# ============================================================================ #

class Solution:
    def reverse(self, x: int) -> int:
        intmax = 1<<31
        intmin = -(1<<31) - 1
        # reverse operation
        rev_x = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x != 0:
            # pop operation
            pop = x % 10
            x //= 10
            # push operation
            rev_x *= 10
            rev_x += pop
        rev_x *= sign
        # overflow ?
        if rev_x < intmin or intmax < rev_x:
            rev_x = 0
        # return
        return rev_x

# ============================================================================ #

cls = Solution()

ans = cls.reverse(123)
print(ans == 321)

ans = cls.reverse(-123)
print(ans == -321)

ans = cls.reverse(120)
print(ans == 21)

ans = cls.reverse(0)
print(ans == 0)

# ---------------------------------------------------------------------------- #
