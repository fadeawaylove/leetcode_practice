from typing import List


class Solution:
    def countTriplets(self, arr) -> int:
        D = {0: (1, -1, 0)}  # (n,last_k,sum)
        ans = xor = 0  # xor[i]=arr[0]^arr[1]^...^arr[i]
        for i, a in enumerate(arr):
            xor ^= a  # xor是概念xor[]的最新值
            if xor in D:  # sum=sum(A,n)
                n, last_k, sum = D[xor]  # last_k=k[n-1]
                sum += n * (i - last_k) - 1  # i=k[n]
                ans += sum
                D[xor] = (n + 1, i, sum)
            else:
                D[xor] = (1, i, 0)
        print(D)
        return ans


# print(Solution().countTriplets([2, 3, 1, 6, 7]))
print(Solution().countTriplets([1, 1, 1, 1, 1]))
# print(Solution().countTriplets([2, 3]))
# print(Solution().countTriplets([1, 3, 5, 7, 9]))
