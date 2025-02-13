int maxProfit(int* prices, int pricesSize) {
    int l = 0;
    int r = 1;
    int max_profit = 0;

    while (r < pricesSize) {
        if (prices[l] < prices[r]) {
            int profit = prices[r] - prices[l];
            max_profit = (max_profit > profit) ? max_profit : profit;
        }
        else {
            l = r;
        }
        ++r;
    }

    return max_profit;
}