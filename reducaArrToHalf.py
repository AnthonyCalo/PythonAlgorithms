class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = dict()
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        n = len(arr)
        res = 0
        amount_left = n
        if(n%2 == 1):
            halfway = (n-1) / 2
        else:
            halfway = n / 2
        counts_idx = 0
        while amount_left > halfway:
            amount_left -= counts[counts_idx][1]
            res += 1
            counts_idx += 1
        return res

'''
1338. Reduce Array Size to The Half
Medium
3K
141
Companies

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.'''