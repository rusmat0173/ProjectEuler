"""
Project Euler: https://projecteuler.net/problem=3

Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

My Approach?
> Initially, create a list of ptime numbers using Sieve of Eranthoses.
>> That can be done in different ways, including dictionary, list of dictionaries and set.
>> I'll try with a set approach. N.B. Set is not subscriptable, but can be iterated through. (for s in my_set: ...)
>> Also, cannot remove from set whilst iterating over it!

> Going through a tree needs while True: ...
>> However, this comes after for p in primes # <= that caused me a lot of grief/time!


Enhanced approach:
Step 1:
> Find a whole number nearly greater than the square root of A.
K ¿ square root(A)
Step 2:
> Test whether A is divisible by any prime number less than K.
If yes A is not a prime number. If not, A is prime number.



To test if some x is prime, we generally have to do divisibility tests only up to and including x√.

That's because if some y>x√ were a factor of x, then there would have to be some z
such that zy=x. And z<x√ because if z>x√, then clearly zy>x (as both z and y would be greater than x√).
But if z<x√, then we've already tested z in going up to x√!

"""
# initially generate the list of prime numbers using Sieve of Eranthoses (without 1)
def Eratosthenes(limit):
    primes = []
    True_dict = {i: True for i in range(1,limit+1)}

    # every integer is divisible by 1, so make 1: False
    True_dict[1] = False

    # rest of sieve
    for i in range(1, limit + 1):
        if True_dict[i] == True:
            # primes.append(True_dict[i])
            count = 0
            while (i**2 + i * count) <= limit:
                True_dict[i**2 + i * count] = False
                count += 1

    # check dictionary for True values
    for key, value in True_dict.items():
        if value == True:
            primes.append(key)

    return primes

# print(Eratosthenes(200))


def prime_factors(limit):
    # create a function for checking if something is integer

    def is_integer(num):
        if round(num) / num == 1:
            return True
        else:
            return False

    # everything else
    primes = Eratosthenes(limit)
    # print(primes)
    prime_factors = []
    remainder = limit

    # check if limit is a prime
    if remainder in primes:
        return [remainder]

    # rest of algorithm
    for p in primes:
        while True:
            if is_integer(remainder/p) == False:
                break
            else:
                prime_factors.append(p)
                remainder = remainder/p
            if remainder ==1:
                break

    return prime_factors

# test case
# print(prime_factors(27))

# now case in the problem: largest prime factor of 600851475143
import time

z = 600851475143
z_root = z**0.5
z_rootA = round(z_root)
print(z_rootA)
# start = time.time()
z1 = prime_factors(z_rootA)
# z = Eratosthenes(1000002)
print(z1)
# end = time.time()
# print(end - start)
# print(max(z))










