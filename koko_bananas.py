class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if(len(piles) == h):
            return max(piles)
        left= 1
        right = max(piles)
        while(left<right):
            mid = (left+right) //2
            if(self.canEatAll(mid, piles, h)):
                left = mid
            else:
                right = mid+1
        return left


    def canEatAll(self, k, piles, h):
        time = 0
        for pile in piles:
            if(pile%k == 0):
                time += pile/k
            else:
                time += 1 + pile//k
            if(time> h):
                return False
        return True        
    
    '''
    875. Koko Eating Bananas
Medium
7.3K
340
Companies

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

    '''