from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 使用dp将所有回文存储起来dp[i][j]表示s[i:j+1]是否是回文字符串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[right] == s[left] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
        print(dp)

        pass


Solution().partition("aab")
