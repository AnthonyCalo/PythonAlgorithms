class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def mode(array):
            most = max(list(map(array.count, array)))
            return list(set(filter(lambda x: array.count(x) == most, array)))
        if(len(nums)==2):
            if(nums[0]==1):
                return [1,2]
            else:
                return [2,1]
        returnarr=[0,0]
        last = nums[0]
        compList=[i for i in range(1, len(nums)+1)]
        for i in nums:
            if i in compList:
                compList.pop(compList.index(i))
        print(compList)
        returnarr[1]=compList[0]
        return [mode(nums)[0], returnarr[1]]