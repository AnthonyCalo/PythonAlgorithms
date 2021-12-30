class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[[]]
        def dfs(i, path):
            path.append(nums[i])
            res.append(path)
            if(i>len(nums)):
                return
            for j in range(i+1,len(nums)):
                dfs(j, path.copy())
        for i in range(len(nums)):
            dfs(i, [])
        return(res)
        '''
        Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
w
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        '''
