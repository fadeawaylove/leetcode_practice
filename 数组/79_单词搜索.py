from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)  # 行数
        if m == 0:
            return False
        n = len(board[0])  # 列数

        marked = [[False] * n for _ in range(m)]  # 记录每个位置被访问的状态

        # 从第一个开始检查是否有符合的
        for i in range(m):
            for j in range(n):
                if self._check(board, i, j, marked, 0, word, m, n):
                    return True
        return False

    def _check(self, board, start_x, start_y, marked, index, word, m, n):
        # 递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了继续搜索
        if board[start_x][start_y] == word[index]:
            # 匹配成功则标记下
            marked[start_x][start_y] = True
            # 寻找下一个位置
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n \
                        and not marked[new_x][new_y] and \
                        self._check(board, new_x, new_y, marked, index + 1, word, m, n):
                    return True
            marked[start_x][start_y] = False
        return False


# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(Solution().exist([["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]], "ABCC"))
