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

    for key, value in True_dict.items():
        if value == True:
            primes.append(key)

    return primes

print(Eratosthenes(200))














