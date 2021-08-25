class Solution:
    def removeDuplicates(self, nums):
        counter = 0
        while (counter < len(nums)-1):
            print(nums[counter], nums[counter+1])
            if nums[counter]==nums[counter+1]:
                nums.pop(counter)
                counter-=1
            counter += 1
        return (len(nums));