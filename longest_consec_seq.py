class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        res = 0
        
        for num in s:
            if(num-1 in s):
                continue
            else:
                count=1
                k = num
                
                while k+1 in s:
                    count+=1
                    k+=1
                res = max(count, res)
        return res