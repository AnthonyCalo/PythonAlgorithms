class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counts = dict()
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            
        return(list(counts.keys())[list(counts.values()).index(1)])  