class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cur_min = cur_max = prices[0]
        cur_profit = 0

        for price in prices:
            if price < cur_min:
                cur_min = cur_max = price
            if price > cur_max:
                cur_max = price
                cur_profit = max(cur_profit, cur_max - cur_min)

        
        return cur_profit

                 

