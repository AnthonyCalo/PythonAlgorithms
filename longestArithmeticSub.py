class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        res = 2
        for i in range(len(nums)):
            dp[i] = dict()
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])
        return res


        '''
        1027. Longest Arithmetic Subsequence
Medium
2.7K
126
Companies

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
    A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic seq


Valid Alternate approach

class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp[j, nums[j]-nums[i]] = dp.get((i, nums[j]-nums[i]), 1) + 1
        
        return max(dp.values())
'''