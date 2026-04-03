class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i=0
        j=1
        maxp=0
        while j<len(prices):
            if prices[j]>prices[i]:
                profit = prices[j]-prices[i]
                maxp=max(maxp,profit)

            else:
                i=j
            j+=1
        return maxp
