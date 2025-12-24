#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        meetingNode = self.findFloydMeetingNode(slow, fast)

        if meetingNode is None:
            return None

        return self.findFloydLoopBeginningNode(head, meetingNode)

    def findFloydMeetingNode(
        self, slow: Optional[ListNode], fast: Optional[ListNode]
    ) -> Optional[ListNode]:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return slow
        return None

    def findFloydLoopBeginningNode(
        self, head: ListNode, meetingNode: ListNode
    ) -> ListNode:
        nodeFromHead = head
        nodeFromMeetingNode = meetingNode
        while nodeFromHead is not nodeFromMeetingNode:
            nodeFromHead = nodeFromHead.next
            nodeFromMeetingNode = nodeFromMeetingNode.next

        return nodeFromHead


# @lc code=end
