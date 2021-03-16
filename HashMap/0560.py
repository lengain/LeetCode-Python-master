"""
和为 K 的子数组
给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数k的范围是[-1e7, 1e7]。


作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/2021-spring-recruitment/5felih/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

"""
前缀和法
分析：使用连续前缀和
    0……j……i

    假设A(i)表示数组中的下标为i的值，S(i) = A(0) + A(0) + ... + A(i)
    那么S(i) - S(j - 1) = k
    S(j - 1) == S(i) - k
    那么存储 前缀和为pre
    当pre-k出现的次数就是 和为 k 的子数组 的数量
    建立以pre为key，pre的出现的次数为value的字典。存储
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pre = 0
        ans = 0
        cacheDiff = {0: 1}
        for value in nums:
            pre += value
            diff = pre - k
            ans += cacheDiff.get(diff, 0)
            cacheDiff[pre] = 1 + cacheDiff.get(pre, 0)
        return ans


"""
暴力破解法
"""
class Solution2:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    ans += 1
        return ans


print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))
print(Solution2().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))