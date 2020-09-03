"""
使用滑动窗口
基本思想：
    1-确定左右指针的初始值，一般右指针就是遍历一次数组，右指针会一直递增
    2-找出左边指针移动的条件，一般左指针在不满足条件的时候右移一位
    3-左指针右移的同时，需要对条件做出反馈，从而可能改变下次条件判断的值
    4-其中变动的地方就是条件判断部分
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        本方法可以得到正确结果，唯一问题就是判断条件部分过于耗时，最终导致超时不通过
        :param nums:
        :param limit:
        :return:
        """

        def check(sub_nums, l):
            s = sorted(sub_nums)
            if s[-1] - s[0] > l:
                return False
            return True

        n = len(nums)
        left = 0
        ret = 0
        wind = []
        for right in range(n):
            # 添加
            wind.append(nums[right])
            # 判断
            while not check(wind, limit):
                left += 1
                wind.pop(0)
            ret = max(ret, right - left + 1)
        return ret


# print(Solution().longestSubarray([8, 2, 4, 7], 4))
# print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
# print(Solution().longestSubarray([8], 10))
# print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
# print(Solution().longestSubarray([2, 5, 2], 9))
print(Solution().longestSubarray([2], 9))
