class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        abs_max=nums[0]
        rel_max=nums[0]
        startingpoint=0
        for i in range(1, len(nums)):
            if(nums[i]+rel_max<nums[i]):
                rel_max=nums[i]
            else:
                rel_max+=nums[i]
            abs_max=max(abs_max, rel_max)
        return(abs_max)