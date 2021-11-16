class Solution:
    #run time of O(n)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy_price=99999999
        for i in range(len(prices)):
            if(prices[i]<buy_price):
                buy_price=prices[i]
            elif(buy_price<prices[i]):
                max_profit=max(prices[i]-buy_price, max_profit)
        return( max_profit)
                
            
        
