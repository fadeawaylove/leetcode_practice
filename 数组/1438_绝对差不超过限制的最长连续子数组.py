"""
使用滑动窗口
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        def check(sub_nums, l):
            s = sorted(sub_nums)
            if s[-1] - s[0] > l:
                return False
            return True

        n = len(nums)
        if n == 1:
            return 1

        left = 0
        right = 1
        wind = [nums[0], nums[1]]
        ret = 0
        while right < n - 1 and left < n - 1:
            if not check(wind, limit):
                left += 1
                wind.pop(0)
                if left == right:
                    right += 1
                    wind.append(nums[right])
            else:
                right += 1
                wind.append(nums[right])
                ret = max(len(wind), ret)
        return ret


# print(Solution().longestSubarray([8, 2, 4, 7], 4))
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
# print(Solution().longestSubarray([8], 10))
# print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
# print(Solution().longestSubarray([2, 5, 2], 9))
