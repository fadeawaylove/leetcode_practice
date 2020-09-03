from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m_count = [0] * len(grid)  # 每一行1的个数
        n_count = [0] * len(grid[0])  # 每一列1的个数
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    m_count[i] += 1
                    n_count[j] += 1

        ret = 0
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1 and (m_count[i] > 1 or n_count[j] > 1):
                    ret += 1

        print(m_count, n_count)
        return ret


print(Solution().countServers([[1, 0], [0, 1]]))
