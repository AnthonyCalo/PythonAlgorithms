class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dick = dict()
        length = len(nums)
        for i in (nums):
            dick[i]=dick.get(i, 0) + 1
        ret=[]
        for i in range(length):
            if dick.get(i+1,0)==0:
                ret.append(i+1)
        return ret