class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        def isFlsh(suits):
            if(len(set(suits)) == 1):
                return True
            return False
        if(isFlsh(suits)):
            return "Flush"
        counter = dict()
        for rank in ranks:
            counter[rank] = counter.get(rank, 0) +1
        mc = max(counter.values())
        if(mc > 2):
            return "Three of a Kind"
        elif(mc > 1):
            return "Pair"
        else:
            return "High Card"

            '''
            2347. Best Poker Hand
Easy
245
15
Companies

You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

    "Flush": Five cards of the same suit.
    "Three of a Kind": Three cards of the same rank.
    "Pair": Two cards of the same rank.
    "High Card": Any single card.

Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.

 

Example 1:

Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"'''