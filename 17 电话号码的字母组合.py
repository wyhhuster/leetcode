class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        res=[]
        for i in range(len(digits)):
            if not res:
                for j in dic[digits[i]]:
                    res.append(j)
                print(res)
            else:
                tem = []
                for k in range(len(res)):
                    for j in dic[digits[i]]:
                        tem.append(res[k]+j)
                res=tem
        return res
class Solution1:
    def letterCombinations(self, digits: str) -> list:
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre+suf for pre in ans for suf in KEY[num]]
        return ans
#java
# class Solution {
#     public vector<string> letterCombinations(string digits) {
#         unordered_map<char, string> table{
#             {'0', " "}, {'1',"*"}, {'2', "abc"},
#             {'3',"def"}, {'4',"ghi"}, {'5',"jkl"},
#             {'6',"mno"}, {'7',"pqrs"},{'8',"tuv"},
#             {'9',"wxyz"}};
#         vector<string> res;
#         if(digits == "") return res;
#         func(res, "", digits, table, 0);
#         return res;
#     }
#
#     void func(vector<string> &res, string str, string &digits, unordered_map<char, string> &m, int k){
#         if(str.size() == digits.size()){
#             res.push_back(str);
#             return;
#         }
#         string tmp = m[digits[k]];
#         for(char w : tmp){
#             str += w;
#             func(res, str, digits, m, k+1);
#             str.pop_back();
#         }
#         return ;
#     }
# };
A=Solution()
print(A.letterCombinations(''))




