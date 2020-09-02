"""
使用hash_map
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, value in enumerate(nums):
            if hash_map.get(value) is not None:
                if i - hash_map.get(value) <= k:
                    return True
            hash_map[value] = i
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
