class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        res=[]
        def dfs(i=0, total=0, path=[]):
            if(total>n or i>len(nums)-1 or nums[i]>10 or len(path)>k):
                return
            if(len(path)==k):
                if(path not in res and total==n):
                    res.append(path.copy())
                    return
                else:
                    return
            total+=nums[i]
            path.append(nums[i])
            dfs(i+1, total, path)
            total-=nums[i]
            path.pop()
            dfs(i+1, total, path)
            return res
        return(dfs())
''''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
'''