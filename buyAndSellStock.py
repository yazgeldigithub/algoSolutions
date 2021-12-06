"""You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the
price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once,
your task is to find the maximum possible profit (the difference between the buy and sell prices). """
'''
EXAMPLE:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
'''
EXAMPLE:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


def buyAndSellStock(prices):
    # store maximum profit gained
    profit = 0

    # initialize local minimum to first element's index
    j = 0

    # start from second element
    for i in range(1, len(prices)):

        # update local minimum if decreasing sequence is found
        if prices[i - 1] > prices[i]:
            j = i

        # sell shares if current element is peak i.e. (previous <= current > next)
        if prices[i - 1] <= prices[i] and (i + 1 == len(prices) or prices[i] > prices[i + 1]):
            profit += (prices[i] - prices[j])
            print(f"Buy on day {j + 1} and sell on day {i + 1}")

    return profit


prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock(prices))  # 4


# 2
def buyAndSellStock2(prices):
    max_profit, min_price = 0, float("inf")
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock2(prices))  # 4


# 3
def buyAndSellStock3(prices):
    if len(prices) == 0:
        return 0
    max_profit = 0
    min_price = prices[0]
    for p in prices[1:]:
        if p < min_price:
            min_price = p
        elif max_profit < p - min_price:
            max_profit = p - min_price
    return max_profit


prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock3(prices))  # 4


# 4
def buyAndSellStock4(prices):
    l, r = 0, 1  #left = buy. right = sell
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit


prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock4(prices))