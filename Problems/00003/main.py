#
# 3. Longest Substring Without Repeating Characters
#

# ============================================================================ #

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # try to determine max_length
        max_length = 0
        try_length = 1
        index = 0
        while index + try_length <= len(s):
            substring = s[index : index + try_length]
            if len(substring) == len(set(substring)):
                max_length = try_length
                try_length += 1
            else:
                index += 1

        # return answer
        return max_length

# ============================================================================ #

cls = Solution()

ans = cls.lengthOfLongestSubstring("abcabcbb")
print(ans == 3)

ans = cls.lengthOfLongestSubstring("bbbbb")
print(ans == 1)

ans = cls.lengthOfLongestSubstring("pwwkew")
print(ans == 3)

ans = cls.lengthOfLongestSubstring("")
print(ans == 0)
