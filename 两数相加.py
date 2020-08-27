# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ret = head
        flag = 0
        while l1 and l2:
            temp_sum = l1.val + l2.val + flag
            flag, temp_sum = temp_sum // 10, temp_sum % 10
            ret.next=ListNode(temp_sum)
            ret = ret.next
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2:
                l1 = ListNode(0)
            if l2 is None and l1:
                l2 = ListNode(0)
        if flag:
            ret.next = ListNode(flag)
        return head.next
