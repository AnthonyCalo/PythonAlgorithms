# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
def bin_search(arr, x):
    low=0
    high=len(arr)-1
    mid=0
    
    while low<=high:
        mid = (high+low) // 2
        if arr[mid] < x:
            low=mid+1
        
        #x is smaller
        elif arr[mid]>x:
            high=mid-1
        else:
            return( mid )
        
    return (-1)
print(binary_search([5,7,7,8,8,10],8))
print(bin_search([5,7,7,8,8,10],8))
