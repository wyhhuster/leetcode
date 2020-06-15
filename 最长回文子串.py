#马拉车
class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        s = '#'.join(s)
        s = '$#' + s + '#$'
        id,mx,index,maxlength=0,0,0,-1
        p=[0 for i in range(len(s))]
        for i in range(1,len(s)-1):
            if mx>i:
                p[i]=min(p[2*id-i],mx-i)
            else:
                p[i]=1
            while i-p[i]>=1 and i+p[i]<=len(s)-2 and s[i-p[i]]==s[i+p[i]]:
                p[i]+=1
            if mx<i+p[i]:
                mx=i+p[i]
                id=i
            if maxlength<p[i]-1:
                maxlength=p[i]-1
                index=i
        s=s[index-maxlength:index+maxlength].replace('#','')
        return s
#动态规划
a=input()
n=len(a)
mat=[[0 for i in range(n)] for i in range(n)]
if n==0:
    print(0)
if n==1:
    print(1)
else:
    count=0
    for i in range(n-1,-1,-1):
        mat[i][i]=1
        count+=1
        for j in range(i+1,n):
            mat[i][j]=a[i]==a[j] and (j-i<3 or mat[i+1][j-1])
            if mat[i][j]!=0:
                count+=1
    print(count)