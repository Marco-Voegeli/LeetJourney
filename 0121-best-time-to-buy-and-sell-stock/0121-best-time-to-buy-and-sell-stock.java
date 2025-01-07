class Solution {
    public int maxProfit(int[] prices) {
        int lowestPrevPrice = prices[0];
        int profit = 0;
        for (int i = 1; i < prices.length; i++){
            int price = prices[i];
            if (price < lowestPrevPrice){
                lowestPrevPrice = price;
            }else if(profit < price -lowestPrevPrice){
                profit = price - lowestPrevPrice;
            }
        }
    return profit;
    }
}