
def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    worddic={}
    for i in wordDict:
        worddic[i]=1
    print(worddic)
    dp=[0]*(len(s)+1)
    dp[0]=1
    for i in range(1,len(s)+1):
        for j in range(0,i):
            if dp[j] and s[j:i] in worddic:
                dp[i]=1
                break
    return dp[len(s)]!=0
print(wordBreak("leetcode",["leet","code"]))


