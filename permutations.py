class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i, path=[]):
            path.append(nums[i])
            if(len(path)==len(nums)):
                res.append(path.copy())
                return
            for j in range(len(nums)):
                if(nums[j] not in path and i!=j):
                    dfs(j, path.copy())
        for i in range(len(nums)):
            dfs(i, [])
        return res

        