class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        int index = 0;

        while (index < prices.length) {
            while (index < prices.length - 1 && prices[index + 1] < prices[index])
                index += 1;
            int min_index = index;
            while (index < prices.length - 1 && prices[index + 1] > prices[index])
                index += 1;
            profit += prices[index] - prices[min_index];
            index += 1;
        }

        return profit;
    }
}