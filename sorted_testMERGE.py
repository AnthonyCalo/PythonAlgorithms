import random

def merge_sort(unsorted):
    if(len(unsorted)>1):
        mid = len(unsorted)//2
        left = unsorted[:mid]
        right = unsorted[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k=0

        while i<len(left) and j<len(right):
            if(left[i] <= right[j]):
                unsorted[k] = left[i]
                i+=1
            else:
                unsorted[k] = right[j]
                j+=1
            k+=1
        
        while i< len(left):
            unsorted[k] = left[i]
            i+=1
            k+=1
        while j< len(right):
            unsorted[k] = right[j]
            j+=1
            k+=1
        


unsorted_list=[random.randrange(1,150) for i in range(24)]
print(unsorted_list)
merge_sort(unsorted_list)
print(unsorted_list)