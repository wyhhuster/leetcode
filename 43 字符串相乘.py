class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1)<len(num2):
            num1,num2=num2,num1
        num1,num2,ans,c=num1[::-1],num2[::-1],[0]*(len(num1)+len(num2)),0
        for i in range(len(num2)):
            m1=int(num2[i])
            for j in range(len(num1)):
                m2 = int(num1[j])
                m = m1 * m2 + ans[i + j]
                c = m // 10
                a = m % 10
                ans[i + j] = a
                ans[i + j + 1] += c
                # m2=int(num1[j])
                # m=m1*m2
                # c=m//10
                # a=m%10
                # ans[i+j]+=a
                # d=ans[i+j]//10
                # ans[i+j]=ans[i+j]%10
                # ans[i+j+1]+=c+d

        res=''
        for i in range(len(ans)-1,-1,-1):
            res+=str(ans[i])
        if res[0]=='0':
            return res[1:]
        else:
            return res
A=Solution()
print(A.multiply('2','3'))
