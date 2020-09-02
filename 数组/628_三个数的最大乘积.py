import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        x = heapq.nlargest(3, nums, key=lambda y: abs(y))
        return x[0] * x[1] * x[2]


print(Solution().maximumProduct([-1, -2, -3]))
