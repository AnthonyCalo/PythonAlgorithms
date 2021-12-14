class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        candidates.sort()
        def dfs(i=0, path=[],total=0):
            if(total==target):
                ret.append(path.copy())
                return
            if i> len(candidates)-1 or total>target:
                return
            total+=candidates[i]
            path.append(candidates[i])
            dfs(i+1, path, total)
            total-=candidates[i]
            path.pop()
            counter=i+1
            if(i+1> len(candidates)-1):
                return
            while candidates[i]==candidates[counter]:
                counter+=1
                if(counter>len(candidates)-1):
                    return
            dfs(counter, path, total)

            


        dfs()
        return(ret)


        '''
        Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]'''