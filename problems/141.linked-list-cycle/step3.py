#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        reached = set()
        while current:
            if current in reached:
                return True
            reached.add(current)
            current = current.next

        return False


# @lc code=end
