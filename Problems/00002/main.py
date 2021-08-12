#
# 2. Add Two Numbers
#

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================================================ #

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create linked-list
        root_ptr = ListNode(0, None)
        cursor_ptr = root_ptr

        # start to calculate
        carry = 0
        while l1 or l2 or carry:
            digit = carry
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            carry = digit // 10
            digit = digit % 10
            # contain digit to next ptr
            cursor_ptr.next = ListNode(digit)
            cursor_ptr = cursor_ptr.next
        
        # return answer
        return root_ptr.next

# ============================================================================ #

# cls = Solution()

# ans = cls.addTwoNumbers([2,4,3],[5,6,4])
# print(ans == [7,0,8])

# ans = cls.addTwoNumbers([0],[0])
# print(ans == [0])

# ans = cls.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
# print(ans == [8,9,9,9,0,0,0,1])
