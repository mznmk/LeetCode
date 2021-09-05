#
# 1996. The Number of Weak Characters in the Game
#

"""
Hint1:
Sort the array on the basis of the attack values and
group characters with the same attack together.
How can you use these groups?
Hint2:
Characters in one group will always have a lesser attack value
than the characters of the next group.
Hence, we will only need to check
if there is a higher defense value present in the next groups.
"""

from typing import List
import bisect

# ============================================================================ #

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        characters = len(properties)
        # sort properties (by 1st elem -> attack)
        properties.sort()
        # determine max defense value with higher attack value than self
        defense_higher_than_self = [property[1] for property in properties]
        defense_higher_than_self[-1] = properties[-1][1]
        for i in range(characters-2, -1, -1):
            defense_higher_than_self[i] = max(defense_higher_than_self[i],
                                                defense_higher_than_self[i+1])
        # determine weak chararacters count
        weak_characters_count = 0
        for i in range(characters-1):
            j = bisect.bisect_left(properties, [properties[i][0] + 1, 0])
            if j < characters and properties[i][1] < defense_higher_than_self[j]:
                weak_characters_count += 1
        # return
        return weak_characters_count
            
# ============================================================================ #

cls = Solution()

ans = cls.numberOfWeakCharacters([[5,5],[6,3],[3,6]])
print(ans == 0)

ans = cls.numberOfWeakCharacters([[2,2],[3,3]])
print(ans == 1)

ans = cls.numberOfWeakCharacters([[1,5],[10,4],[4,3]])
print(ans == 1)

# ---------------------------------------------------------------------------- #

ans = cls.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]])
print(ans == 1)

ans = cls.numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]])
print(ans == 2)
