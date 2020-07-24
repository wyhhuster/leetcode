class Solution(object):
    #直接根据规律判断N的奇偶性
    # N = 1的时候，区间(0, 1)(0, 1)中没有整数是的因数，所以此时Alice败。
    # N = 2的时候，Alice只能拿1，N变成1，Bob无法继续操作，故Alice胜。
    # N = 3的时候，Alice只能拿1，N变成2，根据N = 2的结论，我们知道此时Bob会获胜，Alice败。
    # N = 4的时候，Alice能拿1或2，如果Alice拿1，根据N = 3的结论，Bob会失败，Alice会获胜。
    # N = 5的时候，Alice只能拿1，根据N = 4的结论，Alice会失败。
    def divisorGame1(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N %2==1:
            return False
        else:
            return True
    #动态规划
    #定义f[i]表示当前数字i的时候先手是处于必胜态还是必败态，如果在0-i中存在一个m是必败的状态，
    # 那么Alice直接执行对应的操作让当前的数字变成m，Alice就必胜了，
    # 如果没有任何一个是必败的状态的话，说明Alice无论怎么进行操作，最后都会让Bob处于必胜的状态，此时Alice是必败的。
    def divisorGame2(self, N):
        if N==1:
            return False
        f=[False]*(N+1)
        f[1]=False
        f[2]=True
        for i in range(3,N+1):
            for j in range(1,i):
                if i%j==0 and not f[i-j]:
                    f[i]=True
        return f[N]