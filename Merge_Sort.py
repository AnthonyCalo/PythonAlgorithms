

            

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


#function splits the list until they are all of length 1 then adds it to split List
def split(unsortedList, splitList):
    if len(unsortedList)>1:
        mid=(len(unsortedList)//2)
        L=unsortedList[:mid]
        R=unsortedList[mid:]
        split(L, splitList)
        split(R, splitList)
    else:
        splitList.append(unsortedList)


def merge_sort(array):
    #can't merge a list that isn't split up. Becomes true at the end of split function
    ready_to_merge=False
    splitList = []
    split(array, splitList)
    if(len(splitList)==len(array)):
        ready_to_merge=True
    if(ready_to_merge):
        #once list is sorted it will be of length 1
        while len(splitList) !=1:
            #merge the lists if splitList isn't of length one
            merging_list = []
            if (len(splitList)%2==1):
                #odd length list. merge the uncoupled number with the last of merged couples
                for i in range(len(splitList)-1):
                    if i==0 or i%2==0:
                        merging_list.append(merge(splitList[i], splitList[i+1]))                
                merging_list[-1]=merge(merging_list[-1], splitList[-1])
                splitList=merging_list
            else:
                #even list. Merge every other list item together
                for i in range(len(splitList)-1):
                    if i==0 or i%2==0:
                        merging_list.append(merge(splitList[i],splitList[i+1]))
                splitList=merging_list
        print("SORTED LIST: ", splitList[0])
        return(splitList[0])

            
unsorted_numbers = [2,54,123,5,23,44,32,1489,5,8,66,69,15,25,31,55,849,77,63,45,85,99,77,53,23,22,24,41,213,213,69,124,14,32]
merge_sort(unsorted_numbers)

