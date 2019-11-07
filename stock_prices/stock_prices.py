#!/usr/bin/python

import argparse


def find_max_profit(prices):
  best_trade = []
  for i in prices:
      prices_idx = prices.index(i)  
      
      for j in range(prices_idx + 1, len(prices)):    
          best_choice = prices[j] - prices[prices_idx]
          best_trade.append(best_choice)
  
  return max(best_trade)


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))