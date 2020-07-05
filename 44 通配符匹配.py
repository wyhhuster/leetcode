def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    m, n = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[j][0] = dp[j - 1][0]

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[j][i] = dp[j - 1][i - 1]
            elif p[j - 1] == '*':
                dp[j][i] = dp[j - 1][i] or dp[j][i - 1]
                #j-1表示*为空 i-1表示任何匹配

    return dp[n][m]

print(isMatch("mississippi","m??*ss*?i*pi"))