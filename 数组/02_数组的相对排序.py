from typing import List


class Solution(object):
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))


if __name__ == "__main__":
    sol = Solution()
    ret = sol.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
    print(ret)
