class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res=[]
        def find(s,dot,ans):
            if dot>4:
                return
            if len(s)==0 and dot==4:
                a=ans[:]
                a='.'.join(a)
                self.res.append(a)
                return
            for i in range(1,len(s)+1):
                if 0<=int(s[:i]) and int(s[:i])<=255 and str(int(s[:i]))==s[:i]:
                    ans.append(s[:i])
                    find(s[i:],dot+1,ans)
                    ans.pop()
        find(s,0,[])
        return self.res

A=Solution()
print(A.restoreIpAddresses("010010"))
