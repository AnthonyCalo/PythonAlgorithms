'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1, nums2):
            m = len(nums1)
            n = len(nums2)
            nums1S = []
            for i in range(len(nums1)):
                nums1S.append(nums1[i])
            #print(nums1)

            merged = []
            i=0
            j=0
            #i, j keep track of what number in the smaller lists to see what part has been appended to the merged list
            while i<m or j<n:
                if i==m:
                    #this means all of num1 is into the merged list in order.
                    #just append the rest of nums2 to the merged list
                    for i in range(len(nums2[j:])):
                        merged.append(nums2[j + i])
                    break
                if j==n:   
                    #all of nums 2 is in order. Append the rest of num1 to merged             
                    for l in range(len(nums1S[i:])):
                        merged.append(nums1S[l+i])
                    break
                if(nums1S[i]>nums2[j]):
                    merged.append(nums2[j])
                    j+=1
                elif(nums1S[i]<nums2[j]):
                    merged.append(nums1S[i])
                    i+=1
                else:
                    merged.append(nums1S[i])
                    i+=1
                    merged.append(nums2[j])
                    j+=1
            return merged
        merged=merge(nums1, nums2)
        if(len(merged)%2!=0):
            return(merged[(len(merged)//2)])
        else:
            halfway=int(len(merged)/2)
            half=merged[halfway]
            otherhalf=merged[halfway-1]
            return (half+otherhalf)/2'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1, nums2):
            m = len(nums1)
            n = len(nums2)
            nums1S = []
            for i in range(len(nums1)):
                nums1S.append(nums1[i])
            #print(nums1)

            merged = []
            i=0
            j=0
            #i, j keep track of what number in the smaller lists to see what part has been appended to the merged list
            while i<m or j<n:
                if i==m:
                    #this means all of num1 is into the merged list in order.
                    #just append the rest of nums2 to the merged list
                    for i in range(len(nums2[j:])):
                        merged.append(nums2[j + i])
                    break
                if j==n:   
                    #all of nums 2 is in order. Append the rest of num1 to merged             
                    for l in range(len(nums1S[i:])):
                        merged.append(nums1S[l+i])
                    break
                if(nums1S[i]>nums2[j]):
                    merged.append(nums2[j])
                    j+=1
                elif(nums1S[i]<nums2[j]):
                    merged.append(nums1S[i])
                    i+=1
                else:
                    merged.append(nums1S[i])
                    i+=1
                    merged.append(nums2[j])
                    j+=1
            return merged
        merged=merge(nums1, nums2)
        if(len(merged)%2!=0):
            return(merged[(len(merged)//2)])
        else:
            halfway=int(len(merged)/2)
            half=merged[halfway]
            otherhalf=merged[halfway-1]
            return (half+otherhalf)/2