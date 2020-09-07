from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = 0
                for x in arr[i: j]:
                    a ^= x
                for k in range(j, n):
                    b = 0
                    for y in arr[j: k + 1]:
                        b ^= y
                    if a == b:
                        # print(i, j, k)
                        count += 1
        return count


# print(Solution().countTriplets([2, 3, 1, 6, 7]))
print(Solution().countTriplets([1, 1, 1, 1, 1]))
# print(Solution().countTriplets([2, 3]))
# print(Solution().countTriplets([1, 3, 5, 7, 9]))
