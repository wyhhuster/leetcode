class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left,maxscore=A[0],-1
        for i in range(1,len(A)):
            maxscore=max(maxscore,left+A[i]-i)
            left=max(left,A[i]+i)
        return maxscore