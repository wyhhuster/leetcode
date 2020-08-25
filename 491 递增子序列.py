class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        def find(num,ans):
            if len(ans)>=2:
                a=ans[:]
                if a not in self.res:
                    self.res.append(a)
            for i in range(len(num)):
                if not ans:
                    ans.append(num[i])
                    find(num[i+1:],ans)
                    ans.pop()
                if len(ans)>0 and num[i]>=ans[-1]:
                    ans.append(num[i])
                    find(num[i+1:],ans)
                    ans.pop()
        find(nums,[])
        return self.res

#java
class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> res;
        vector<int> tmp;
        dfs(nums,0,tmp,res);
        return vector<vector<int>>(res.begin(),res.end());
    }
    void dfs(vector<int>&nums,int i,vector<int>&tmp,set<vector<int>>&res){
        if(tmp.size()>=2){
            res.insert(tmp);
        }
        for(int j=i;j<nums.size();j++){
            if (!tmp.empty() && tmp.back()>nums[j]) continue;
            tmp.push_back(nums[j]);
            dfs(nums,j+1,tmp,res);
            tmp.pop_back();
        }
    }
};


