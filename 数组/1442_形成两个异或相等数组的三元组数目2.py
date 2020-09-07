from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n - 1):
            temp = arr[i]
            for j in range(i + 1, n):
                temp = temp ^ arr[j]
                if temp == 0:
                    count += j - i
        return count


# print(Solution().countTriplets([2, 3, 1, 6, 7]))
print(Solution().countTriplets([1, 1, 1, 1, 1]))
# print(Solution().countTriplets([2, 3]))
# print(Solution().countTriplets([1, 3, 5, 7, 9]))
