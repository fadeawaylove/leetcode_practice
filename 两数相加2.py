# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = []
        nums2 = []
        while l1:
            nums1.append(str(l1.val))
            l1 = l1.next
        while l2:
            nums2.append(str(l2.val))
            l2 = l2.next
        nums1 = int("".join(nums1[::-1]))
        nums2 = int("".join(nums2[::-1]))
        ret = str(nums1 + nums2)
        ret = ret[::-1]
        head = ListNode(0)
        x = head
        for r in ret:
            x.next=ListNode(int(r))
            x=x.next
        return head.next
