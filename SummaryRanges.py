

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start=0
        end=0
        se=[]
        if nums==[]:
            return []
        nextio=nums[0]
        for i in range(len(nums)):
            if nums[i]!=nextio:
                se.append([start,i-1])
                start=i
                end=i
            nextio=nums[i]+1
        se.append([start,len(nums)-1])
        ret_string=[]
        for i in se:
            if(i[0]==i[1]):
                ret_string.append(str(nums[i[0]]))
            else:
                app_string=str(nums[i[0]]) + "->" + str(nums[i[1]])
                ret_string.append(app_string)
        return(ret_string)

'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''