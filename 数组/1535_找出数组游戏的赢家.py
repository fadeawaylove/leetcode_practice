"""
可以等价为：
当k>=n-1的时候，就是求数组的最大值;
当k<n-1的时候，
"""

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cur, temp = arr[0], k
        if k <= n - 1:
            for i in range(1, n):
                if cur < arr[i]:
                    cur = arr[i]
                    temp = k - 1
                else:
                    temp -= 1
                if temp == 0:
                    return cur
            return cur
        else:
            return max(arr)


# print(Solution().getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
# print(Solution().getWinner([1, 25, 35, 42, 68, 70], 6))
# print(Solution().getWinner([2, 1, 3, 5, 4, 6, 7], 2))
print(Solution().getWinner([1, 25, 35, 42, 68, 70], 3))
# print(Solution().getWinner([1, 25, 35, 42, 70, 68], 3))
# print(Solution().getWinner([69, 25, 35, 42, 70, 68], 3))
