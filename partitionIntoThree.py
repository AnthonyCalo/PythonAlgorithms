class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        summ = sum(arr)
        if(summ % 3 != 0):
            return False
        target = summ / 3
        running_sum = 0
        count = 0
        for i in arr:
            running_sum += i
            if(running_sum == target):
                running_sum = 0
                count += 1
        return count >= 3
    '''
    1013. Partition Array Into Three Parts With Equal Sum
Easy
1.4K
136
Companies

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 
    
    '''