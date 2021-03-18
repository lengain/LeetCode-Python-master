"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/2021-spring-recruitment/5f2cm2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            start1, end1 = self.extendString(s, i, i)
            if end1 - start1 > end - start:
                start, end = start1, end1
            if i < len(s) - 1:
                start2, end2 = self.extendString(s, i, i + 1)
                if end2 - start2 > end - start and s[i] == s[i + 1]:
                    start, end = start2, end2

        return s[start: end + 1]

    def extendString(self, s: str, start: int, end: int):
        add = False
        while start >= 0 and end < len(s) and s[start] == s[end]:
            add = True
            start -= 1
            end += 1
        if add:
            return start + 1, end - 1
        else:
            return start, end


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("abb"))

