`
@author: Fizz Cao 
@file: 122_best_time_to_buy_and_sell_stock_ii.py
@time: 6/10/2021 11:28 pm
`
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;

    let index = 0;

    while (index < prices.length) {
        while (index < prices.length - 1 && prices[index + 1] < prices[index])
            index += 1;
        let min_index = index;
        while (index < prices.length - 1 && prices[index + 1] > prices[index])
            index += 1;
        profit += prices[index] - prices[min_index];
        index += 1;
    }

    return profit;
};