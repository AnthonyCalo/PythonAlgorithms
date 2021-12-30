class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydick=dict()
        for i in nums:
            if(mydick.get(i,0)!=0):
                return True
            else:
                mydick[i]=1
        return False