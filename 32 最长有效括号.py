#https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
#栈
def longestValidParentheses( s):
    """
    :type s: str
    :rtype: int
    """
    stack=[]
    zero_one=[0 for i in range(len(s))]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        else:
            if not stack:
                zero_one[i]=1
            else:
                stack.pop()
    while stack:
        index=stack.pop()
        zero_one[index]=1
    print(zero_one)
    maxlength=0
    curlength=0
    for i in range(len(zero_one)):
        if zero_one[i]==0:
            curlength+=1
            continue
        else:
            maxlength=max(maxlength,curlength)
            curlength=0
    maxlength = max(maxlength, curlength)
    return maxlength
print(longestValidParentheses(''))



#动态规划
def longestValidParentheses1( s):
    """
    :type s: str
    :rtype: int
    """
    if len(s)==0:
        return 0
    dp=[0 for i in range(len(s))]
    for i in range(1,len(s)):
        if s[i]==')':
            if s[i-1]=='(':
                if i-2>=0:
                    dp[i]=dp[i-2]+2
                else:
                    dp[i]=2
            elif i-dp[i-1]>=1 and s[i-dp[i-1]-1]=='(':
                if i-dp[i-1]-2>=0:
                    dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
                else:
                    dp[i]=dp[i-1]+2
    return max(dp)
print(longestValidParentheses1('(()))())('))
#左右遍历
def longestValidParentheses2( s):
    left,right,length=0,0,0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            length=max(right*2,length)
        if right>left:
            right,left=0,0
    maxlength=length
    length=0
    left,right=0,0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            length=max(2*left,length)
        if left>right:
            left,right=0,0
    maxlength=max(maxlength,length)
    return maxlength
print(longestValidParentheses2("(()))())("))


