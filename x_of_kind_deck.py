from collections import Counter

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if(deck == [1]):
            return False
        counted = dict(Counter(deck))
        vals = counted.values()
        def gcd(x, y):
            if(y==0):
                return x
            else:
                return gcd(y, x%y)

        def get_gcd(nums):
            if(len(nums)==1):
                return nums[0]
            div = gcd(nums[0], nums[1])
    
            for i in range(2, len(nums)):
                div = gcd(div, nums[i])
                if(div == 1):
                    return 1
            return div
        return get_gcd(vals) > 1        


'''
    LeetCode Logo

Problem List
Premium
0
914. X of a Kind in a Deck of Cards
Easy
1.6K
398
Companies

You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

    Each group has exactly x cards where x > 1, and
    All the cards in one group have the same integer written on them.

Return true if such partition is possible, or false otherwise.

 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
'''