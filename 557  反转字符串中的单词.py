class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[i[::-1] for i in s.split()]
        return ' '.join(a)
        # if not s:
        #     return s
        # s = s.split(' ')
        # ans=''
        # for i in range(len(s)):
        #     a=s[i][::-1]
        #     ans+=a
        #     ans+=' '
        # return ans
#java
# class Solution {
#     public String reverseWords(String s) {
#         String[] strs=s.split(" ");
#         StringBuffer buffer=new StringBuffer();
#         for(int i=0;i<strs.length;i++){
#             buffer.append(new StringBuffer(strs[i]).reverse().toString());
#             buffer.append(" ");
#         }
#         return buffer.toString().trim();
#     }
# }
A=Solution()
print(A.reverseWords("Let's take LeetCode contest"))

