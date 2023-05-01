class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def get_small_larger_index(lst, target):
            left = 0
            right = len(lst) - 1
            # check if target is greater than all elements in the list
            if target >= lst[right]:
                return -1
            while left <= right:
                mid = (left + right) // 2
                # check if mid is greater than target
                if lst[mid] > target:
                    # check if mid is the smallest element greater than target
                    if mid == 0 or lst[mid - 1] <= target:
                        return mid
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            return -1

        nums1.sort()
        output=[]
        for num in nums2:
            li = get_small_larger_index(nums1, num)            

            if(li == -1):
                output.append(nums1.pop(0))
            else:
                output.append(nums1.pop(li))

        return output
            

            '''
            You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

Example 1:

Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]

            
            '''