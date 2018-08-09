"""
Project Euler: https://projecteuler.net/problem=1

Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

My approach:
> try a generator approach so that you don;t have to labour through 999 iterations

Result:
> simple way is faster!

"""
# import time to compare approaches
import time

limit = 1e6


start = time.time()
# generators to take you up to 999
myGenerator3 = (3*i for i in range(int((limit+2)/3)))
myGenerator5 = (5*j for j in range(int((limit+4)/5)))
# generator for multiples of 3 and 5 that you will subtract
myGenerator15 = (3*5*k for k in range(int((limit+(3*5-1))/(3*5))))

cumsum3 = 0
cumsum5 = 0
cumsum15 = 0

for i in myGenerator3:
    cumsum3 += i
for j in myGenerator5:
    cumsum5 += j
for k in myGenerator15:
    cumsum15 += k

print(cumsum3 + cumsum5 - cumsum15)
end = time.time()
print(end - start)


# simple way
start = time.time()

def getSum(limit):
  sum = 0
  for x in range(1, limit):
    if x % 3 == 0 or x % 5 == 0:
      sum += x
  return sum

print(getSum(int(1e6)))
end = time.time()
print(end - start) 
