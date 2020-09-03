from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ret = []
        temp = []
        for num in nums:
            if temp and num > temp[-1] + 1:
                ret.append("%s->%s" % (temp[0], temp[-1]) if len(temp) > 1 else str(temp[0]))
                temp = []
            temp.append(num)

        if temp:
            ret.append("%s->%s" % (temp[0], temp[-1]) if len(temp) > 1 else str(temp[0]))
        # print(temp)
        return ret


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
