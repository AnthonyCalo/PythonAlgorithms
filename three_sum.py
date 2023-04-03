class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            l, r = i+1, len(nums) - 1
            while(l < r):
                summ = nums[i] + nums[l] + nums[r]
                if(summ == 0):
                    if([nums[i],nums[l],nums[r]] not in res):
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                elif(summ > 0):
                    r -= 1
                else:
                    l+=1
        return res
        
            