"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        求中位数其实可以等效为找到两个数组中第 k//2 + 1小（k为奇数）或者 k//2和k//2 + 1（K为偶数）
        要求时间复杂度为O(log(k))，可以考虑二分法
        """
        # 先默认做奇数的 写完再优化为偶数的，实际就是找第k小的元素
        m, n = len(nums1), len(nums2)  # 两个数组的长度
        k = (m + n) // 2 + 1

        index1, index2 = 0, 0  # 分别指向nums1和nums2的初始下标
        while True:
            # 特殊情况
            if index1 == m:  # 下标越界
                return nums2[index2 + k - 1]
            if index2 == n:  # 下标越界
                return nums1[index1 + k - 1]
            if k == 1:  # 最小的数
                return min(nums1[index1], nums2[index2])

            new_index1 = min(index1 + k // 2 - 1, m - 1)  # 最新的下标
            new_index2 = min(index2 + k // 2 - 1, n - 1)  # 最新的下标
            if nums1[new_index1] <= nums2[new_index2]:
                k -= new_index1 - index1 + 1
                index1 = new_index1 + 1
            else:
                k -= new_index2 - index2 + 1
                index2 = new_index2 + 1


print(Solution().findMedianSortedArrays([1, 10], [1, 2, 3]))
