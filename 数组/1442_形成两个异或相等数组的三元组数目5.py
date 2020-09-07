from typing import List
from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        hash_map = defaultdict(list)  # 累亦或的value:对应的下标列表
        hash_map[0].append(-1)  # value为0的第一个下标定义为-1

        xor = 0
        for i, v in enumerate(arr):
            xor ^= v
            hash_map[xor].append(i)

        ans = 0
        for index_list in hash_map.values():
            for index in range(len(index_list)):
                i = index_list[index] + 1
                for k in index_list[index + 1:]:
                    ans += k - i
        return ans


# print(Solution().countTriplets([2, 3, 1, 6, 7]))


# print(Solution().countTriplets([1, 1, 1, 1, 1]))
# print(Solution().countTriplets([2, 3]))
print(Solution().countTriplets([1, 3, 5, 7, 9]))
