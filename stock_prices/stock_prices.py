#!/usr/bin/python
import math
import argparse

def find_max_profit(prices):
  buy = math.inf
  buy_index = 0
  sell = 0
  for i in prices:
  # find the lowest price to buy at
    if i < buy:
      buy = i
      buy_index = prices.index(buy)
  print(buy)
  print(buy_index)

  # sell price must be after the buy price
  buy_prices = [ i for i in prices[buy_index + 1:] if i > buy ]
  for i in buy_prices:
    if i > sell:
      sell = i
  print(sell - buy)
  # find the largest price to sell at
  return sell - buy
    
find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))