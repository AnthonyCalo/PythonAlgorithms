#my initial thoughts unoptimized
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)-1
        l, r = 0, n
        optimal_sub = -999999
        while l<=k:
            res = min(nums[l:r+1]) * (r -l + 1)
            if(res > optimal_sub):
                optimal_sub = res
            while r >= k:
                res = min(nums[l:r+1]) * (r -l + 1)

                if(res > optimal_sub):
                    optimal_sub = res
                r -= 1
                if(r==l):
                    break
            l+=1
            r = n
        return optimal_sub


        '''
        
        1793. Maximum Score of a Good Subarray
Hard
866
27
Companies

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

        '''
# optimized solution
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = nums[k]
        n = len(nums) - 1
        minval = nums[k]
        l = r = k
        while l > 0 or r< n:
            if(nums[l-1] if l else 0) < (nums[r+1] if r < n else 0):
                r += 1
            else: 
                l -= 1
            minval = min(minval, nums[l], nums[r])
            res = max(res, (minval * (r- l + 1)))
        return res
            


