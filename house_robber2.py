'''
The question is basically the same as the first house robber but this time its a circle

for example [1, 2, 3, 4], in this array 4 and 1 are neighbors
'''

class Solution:
    def rob(self, nums: List[int]) -> int:               
        def robberOne(nums):
            dp = [0 for i in range(len(nums))]
            n = len(nums)
            for i in range(len(nums)):
                if(i>1):
                    dp[i]= nums[i] + max(dp[i-2], dp[i-3])
                else:
                    dp[i]=nums[i]
            return max(dp)
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return( max(robberOne(nums[:-1]), robberOne(nums[1:])) )