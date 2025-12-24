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
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     reached = set()
    #     current = head
    #     while current is not None:
    #         if current in reached:
    #             return current
    #         reached.add(current)
    #         current = current.next
    #     return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # step1 Floydの循環検出でloopするかどうかを判定する
        slow = fast = head
        hasLoop = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                hasLoop = True
                break
        if hasLoop != True:
            return None

        # step2
        # 片方のNodeをheadに設定し、headと循環検出で合流した点からそれぞれ1stepずつたどる
        # 合流した点がloopの開始の点になる
        nodeFromHead = head
        nodeFromMeetingPoint = slow
        while nodeFromHead != nodeFromMeetingPoint:
            nodeFromHead = nodeFromHead.next
            nodeFromMeetingPoint = nodeFromMeetingPoint.next
        return nodeFromHead


# @lc code=end
