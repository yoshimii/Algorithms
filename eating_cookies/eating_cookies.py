#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  cache = { }
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

# def dynamic_cookies(n, cache=None):
#   if cache is None:
#     cache = {0:1}

#   if n < 0:
#     print(0)
#     return 0
#   elif n not in cache:
#     cache[n] = dynamic_cookies(n - 3) + dynamic_cookies(n - 2) + dynamic_cookies(n - 1)
#   print(cache[n])  
#   return cache[n]
# dynamic_cookies(50)
  
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')