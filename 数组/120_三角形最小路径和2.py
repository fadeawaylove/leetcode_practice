"""
动态规划
类似分治，将一个大的问题拆分为可以统一表示的小问题，这里的统一表示就是用状态转移方程作为问题延续下去的关系
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  # 数组的长度（三角形的高度）

        # 遍历获取每一层的结果
        for i in range(1, n):
            # 当前是第i行，从第二行（i=1表示第二行）开始
            # 这是边界条件，每一行的第一个元素只能由上一行的第一个元素获得
            triangle[i][0] = triangle[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                # 第(i,j)个元素的结果，等于(i-1,j-1)和(i-1, j)中的较小值 加上 (i,j)处原本的值
                triangle[i][j] = min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
            # 这是边界条件，每一行的第最后一个元素只能由上一行的最后一个元素获得
            triangle[i][i] = triangle[i - 1][i - 1] + triangle[i][i]
        return min(triangle[n - 1])


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
