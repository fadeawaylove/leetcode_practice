"""
动态规划 最重要的就是状态转移方程 求什么就把什么设为状态
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # 表示从s[i:j]的回文状态
        ans = ""  # 结果

        for l in range(n):
            # l为子串的长度
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


print(Solution().longestPalindrome("babad"))
