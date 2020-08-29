#马拉车
class Solution1(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        id,index,mx,length=0,0,0,0
        s='#'.join(s)
        s = '$#' + s + '#$'
        p=[0]*len(s)
        for i in range(1,len(s)-1):
            if mx>i:
                p[i]=min(p[2*id-i],mx-i)
            else:
                p[i]=1
            while i+p[i]<=len(s)-1 and i-p[i]>=1 and s[i+p[i]]==s[i-p[i]]:
                p[i]+=1
            if mx<p[i]+i:
                id=i
                mx=p[i]+i
            if i-p[i]==0:
                index=i
                length=p[i]-1
        s=s.strip('$').replace('#','')
        ind=index//2-1
        length//=2
        print(ind)
        print(length)
        a=s[ind+length+1:]
        a=a[::-1]
        return a+s
A=Solution1()
print(A.shortestPalindrome('abbacd'))

class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        for i in range(n-1, -1, -1):
            s1 = s[:i+1]
            if s1 == s1[::-1]:
                s2 = s[i+1:]
                break
        return s2[::-1] + s