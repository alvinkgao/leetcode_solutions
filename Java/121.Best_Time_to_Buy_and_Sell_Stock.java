class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;

        int cur_min = prices[0], cur_max = prices[0], profit = 0;

        for (int price : prices) {
            if (price < cur_min) {
                cur_min = cur_max = price;
            }
            else if (price > cur_max) {
                cur_max = price;
                profit = Math.max(profit, cur_max - cur_min);
            }
        }

        return profit;
    }
}