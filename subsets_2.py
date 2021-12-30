class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums = sorted(nums)
        def dfs(i, path):
            path.append(nums[i])
            if path not in res:
                res.append(path)
            if(i>len(nums)):
                return
            for j in range(i+1,len(nums)):
                dfs(j, path.copy())
        for i in range(len(nums)):
            dfs(i, [])
        return(res)
    '''
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    '''