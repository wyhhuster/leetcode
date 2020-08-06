class Solution(object):
    #超时
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    word=words[i]+words[j]
                    if self.isPalindrome(word):
                        ans.append([i,j])
        return ans

    def isPalindrome(self,word):
        left,right=0,len(word)-1
        while left<right:
            if word[left]!=word[right]:
                return False
            left+=1
            right-=1
        return True
    #分解字符串
    def palindromePairs1(self, words):

        def findWord(s, left, right):
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s, left, right):
            preorder=s[left:right+1]
            postorder=preorder[::-1]
            return preorder==postorder

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m +1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])
        return ret
c='bat'
m = len(c)
for j in range(m +1):
    print(j)
    print(c[j:m])
print(c[0:0])
A=Solution()
print(A.palindromePairs1( ["bat","tab","cat"]))
