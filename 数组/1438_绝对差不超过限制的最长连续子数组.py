"""
使用滑动窗口
基本思想：
    1-确定左右指针的初始值，一般右指针就是遍历一次数组，右指针会一直递增
    2-找出左边指针移动的条件，一般左指针在不满足条件的时候右移一位
    3-左指针右移的同时，需要对条件做出反馈，从而可能改变下次条件判断的值
    4-其中变动的地方就是条件判断部分
"""
import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0  # 初始左指针为0
        max_ = []
        min_ = []
        ret = 0
        # right为右指针
        for right in range(n):
            # 维护大顶堆和小顶堆（实际上堆顶是维护的边界条件，即当前区间中最大和最小满足limit条件的元素及下标）
            heapq.heappush(max_, (-nums[right], right))
            heapq.heappush(min_, (nums[right], right))
            # 循环判断，若不满足limit条件，则要更新left的值
            while max_ and min_ and -max_[0][0] - min_[0][0] > limit:
                # 如果是因为最大元素导致的不满足条件，则要将包含最大元素左边的元素都删除（可以考虑如果只是单纯移动左指针的话，就可能让最大元素的下标不再满足左边界left的要求）
                while max_[0][1] <= left:
                    heapq.heappop(max_)
                # 如果是因为最小元素导致的不满足条件，则要将包含最小元素左边的元素都删除
                while min_[0][1] <= left:
                    heapq.heappop(min_)
                # 左指针右移一位
                left += 1
            ret = max(ret, right - left + 1)
        return ret


# print(Solution().longestSubarray([8, 2, 4, 7], 4))
# print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
# print(Solution().longestSubarray([8], 10))
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
# print(Solution().longestSubarray([2, 5, 2], 9))
