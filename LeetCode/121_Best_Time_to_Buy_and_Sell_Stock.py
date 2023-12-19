'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

import unittest

def best_time_to_buy_and_sell_stocks(prices: list) -> int:
    profit = 0
    min_n = prices[0]
    for x in prices:
        if x < min_n:
            min_n = x
        if x - min_n > profit:
            profit = x - min_n
    return profit
    

class Testbest_time_to_buy_and_sell_stocks(unittest.TestCase):

    # def test_best_time_to_buy_and_sell_stocks_of_zero(self):
    #     self.assertEqual(best_time_to_buy_and_sell_stocks([0]), [0])

    def test_best_time_to_buy_and_sell_stocks_of_positive_integer(self):
        self.assertEqual(best_time_to_buy_and_sell_stocks([7,1,5,3,6,4]), 5)
        self.assertEqual(best_time_to_buy_and_sell_stocks([7,6,4,3,1]), 0)
        # self.assertEqual(best_time_to_buy_and_sell_stocks(20), 2432902008176640000)

    # def test_best_time_to_buy_and_sell_stocks_of_negative_number(self):
    #     self.assertEqual(best_time_to_buy_and_sell_stocks(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()