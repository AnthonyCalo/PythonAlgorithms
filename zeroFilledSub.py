class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subs = []
        res = 0
        subDist = 0
        for num in nums:
            if(num==0):
                subDist+=1
            else:
                if(subDist!=0):
                    subs.append(subDist)
                subDist = 0
        if(subDist!=0):
            subs.append(subDist)
        
        for sub in subs:
            for i in range(sub):
                res += i+1
        return res
'''
2348. Number of Zero-Filled Subarrays
Medium
381
12
Companies

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

'''