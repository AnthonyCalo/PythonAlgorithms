class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        res = 0
        for num in nums:
            if num != mn and num != mx:
                res+=1
        return res


        '''
        
        Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

 
        '''