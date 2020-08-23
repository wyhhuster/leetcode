class Solution:
    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        i=0
        while m!=n:
            m>>=1
            n>>=1
            i+=1
        return m<<i

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        while n>m:
            n=n&(n-1)
        return n
