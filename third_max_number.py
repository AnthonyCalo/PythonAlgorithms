# Given an integer array nums, return the third distinct maximum number in this array.
#  If the third maximum does not exist, return the maximum number.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct=[]
        for i in nums:
            if i in distinct:
                continue
            else:
                distinct.append(i)
        if(len(distinct)>2):
            distinct.sort()
            return(distinct[-3])
        else:
            return(max(distinct))