class Solution(object):
    def twoSum(self, nums, target):
        """
        return index of two numbers that add up to target
        """
        for i in range(len(nums)):
            
            coAdd = target - nums[i]
            if coAdd in nums:
                if nums.index(coAdd)!=i:
                    return[i, nums.index(coAdd)]

        
