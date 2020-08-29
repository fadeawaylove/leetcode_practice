"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


# 一个简单的实现使用了两次迭代。在第一次迭代中，我们将每个元素的值和它的索引添加到表中。然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]target−nums[i]）是否存在于表中。注意，该目标元素不能是 nums[i]nums[i] 本身！

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用hash map，两次遍历，第一次遍历存下 key为可能的target value为对应的下标
        hash_map = {target - v: i for i, v in enumerate(nums)}
        for i, n in enumerate(nums):
            j = hash_map.get(n)
            if j and i != j:
                return [i, j]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
