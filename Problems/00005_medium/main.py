#
# 5. Longest Palindromic Substring
#

# ============================================================================ #

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # try to determine palindrome
        max_length = len(s)
        index = 0
        while 42:
            substring = s[index : index + max_length]
            if substring == substring[::-1]:
                # palindrome
                break
            else:
                # not palindrome
                if index + max_length == len(s):
                    max_length -= 1
                    index = 0
                else:
                    index += 1

        # return answer
        return s[index : index + max_length]
        
# ============================================================================ #

cls = Solution()

ans = cls.longestPalindrome("babad")
print(ans == "bab")

ans = cls.longestPalindrome("cbbd")
print(ans == "bb")

ans = cls.longestPalindrome("a")
print(ans == "a")

ans = cls.longestPalindrome("ac")
print(ans == "a")
