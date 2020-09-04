"""
动态规划
类似分治，将一个大的问题拆分为可以统一表示的小问题，这里的统一表示就是用状态转移方程作为问题延续下去的关系
状态转移方程：描述前一个小结果和后一个小结果之间的关系，依据关系链可以得到最终结果
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  # 数组的长度（三角形的高度）
        f = [0] * n  # 保存每一层的结果，到当前层当前元素的最小路径
        f[0] = triangle[0][0]  # 第一层，第一个元素的结果就是三角形顶的值

        # 遍历获取每一层的结果
        for i in range(1, n):
            f[i] = f[i-1] + triangle[i][i]  # 边界条件，f[i]是最后一个元素
            for j in range(i-1, 0, -1):
                # 第(i,j)个元素的结果，等于(i-1,j-1)和(i-1, j)中的较小值 加上 (i,j)处原本的值
                f[j] = min(f[j-1], f[j]) + triangle[i][j]
            # 这是边界条件，每一行的第最后一个元素只能由上一行的最后一个元素获得
            f[0] = f[0] + triangle[i][0]
        return min(f)


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))

"""
1. [2]       
2. [5, 6]                   
3. [11, 10, 13]          [6, 5, 7]    
"""