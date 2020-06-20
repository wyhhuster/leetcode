#递归
class Solution:
    def match(self, s, pattern):
        # write code here
        if len(s)==0 and len(pattern)==0:
            return True
        elif len(s)!=0 and len(pattern)==0:
            return False
        elif len(s)==0 and len(pattern)!=0:
            if len(pattern)>1 and pattern[1]=='*':
                return self.match(s,pattern[2:])
            else:
                return False
        else:
            if len(pattern)>1 and pattern[1]=='*':
                if pattern[0]==s[0] or pattern[0]=='.':
                    return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
                else:
                    return self.match(s,pattern[2:])
            else:
                if pattern[0]==s[0] or pattern[0]=='.':
                    return self.match(s[1:],pattern[1:])
                else:
                    return False

    #动态规划
    def isMatch(self, s, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # write code here
        m, n = len(s), len(pattern)
        if m == 0 and n == 0:
            return True
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 初始化
        dp[0][0] = True
        for j in range(1, n + 1):
            if j > 1 and pattern[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[j - 1] == "." or pattern[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j] and (
                                s[i - 1] == pattern[j - 2] or pattern[j - 2] == ".")
        return dp[m][n]