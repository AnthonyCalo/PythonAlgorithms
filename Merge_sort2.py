def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        print(left, right)
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        print(left,right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
         
            i += 1
            k += 1
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

unsorted_list=[54,7,23,22,11,55,152,61,32]
mergeSort(unsorted_list)
print(unsorted_list)