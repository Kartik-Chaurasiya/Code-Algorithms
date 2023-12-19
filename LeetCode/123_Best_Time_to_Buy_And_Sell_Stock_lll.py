'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.'''

import unittest

def best_time_to_buy_and_sell_stocks_III(prices: list) -> int:
    if sorted(prices, reverse = False) == prices:
        return  prices[len(prices) - 1] - prices[0]
    elif sorted(prices, reverse = True) == prices:
        return 0
    elif len(prices) < 2:
        return 0
    else: 
        A = -prices[0]
        B = float("-inf")
        C = float("-inf")
        D = float("-inf")

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)
        return D
    

class Testbest_time_to_buy_and_sell_stocks_III(unittest.TestCase):

    # def test_best_time_to_buy_and_sell_stocks_III_of_zero(self):
    #     self.assertEqual(best_time_to_buy_and_sell_stocks_III([0]), [0])

    def test_best_time_to_buy_and_sell_stocks_III_of_positive_integer(self):
        self.assertEqual(best_time_to_buy_and_sell_stocks_III([3,3,5,0,0,3,1,4]), 6)
        self.assertEqual(best_time_to_buy_and_sell_stocks_III([1,2,3,4,5]), 4)
        self.assertEqual(best_time_to_buy_and_sell_stocks_III([7,6,4,3,1]), 0)

    # def test_best_time_to_buy_and_sell_stocks_III_of_negative_number(self):
    #     self.assertEqual(best_time_to_buy_and_sell_stocks_III(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()