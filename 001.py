"""
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

分析：
    第一种方法是暴力破解法，双重循环就行了。
    时间复杂度O(n^2)
    空间复杂度O(1)
    第二种方法是利用哈希表查询

    如果本题中声明数组是顺序的，那么还可以使用首尾缩进查找法
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution1:
    """
    暴力破解法
    """

    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        count = len(nums) - 1
        for i in range(0, count):
            for j in range(i + 1, count + 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
            i += 1
        return []


class Solution2:
    """
    哈希表查询
    """

    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[nums[i]] = i
        return []


# print(Solution1.twoSum(nums=[2, 7, 11, 15], target=9))
# print(Solution1.twoSum(nums=[2, 5, 5, 11], target=10))
print(Solution2.twoSum(nums=[3, 2, 4], target=6))
