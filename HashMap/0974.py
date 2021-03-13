"""
974. 和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000


作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/2021-spring-recruitment/5fh4qt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
"""
dict.get(value, default)
根据同余定理解答
"""
class Solution:
    def subarraysDivByK(self, A: list[int], K: int) -> int:
        record = {0: 1}
        total = 0
        ans = 0
        for ele in A:
            total += ele
            mod = total % K
            same = record.get(mod, 0)
            ans += same
            record[mod] = same + 1
        return ans

text1 = [4, 5, 0, -2, -3, 1]
print(Solution().subarraysDivByK(text1, 5))
