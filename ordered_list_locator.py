def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target<nums[0]):
            return(0)
        if(target>nums[-1]):
            return(len(nums))
        search_nums=nums
        found = False
        mid=9999999
        while mid>1:
            mid=len(search_nums)//2
            if(target>search_nums[mid]):
                search_nums=search_nums[mid:]
            elif(target< search_nums[mid]):
                search_nums=search_nums[:mid]
            else:
                print("here")
                return(nums.index(search_nums[mid]))
                break
        print(search_nums)
        if(len(search_nums)==2):
            return(nums.index(search_nums[1]))
        elif(len(search_nums)==3):
            #length will be 3
            if(target>search_nums[1]):
                return (nums.index(search_nums[2]))
            else:
                return(nums.index(search_nums[1]))
        else:
            print(search_nums)
            if(search_nums[0]>target):
                return(nums.index(search_nums[0]))
            elif(search_nums[0]==target):
                return(nums.index(search_nums[0]))
            else:
                return(nums.index(search_nums[0])+1)
            
print(searchInsert([1,2,3,5,7,8,9,13], 4
))