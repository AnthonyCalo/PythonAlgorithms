class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret=[]
        for i in nums:
            if i % 2==0:
                ret.insert(0, i)
            else:
                ret.append(i)
        return ret