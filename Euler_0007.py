"""
Project Euler: https://projecteuler.net/problem=7

10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


My Approach?
> Did using work on Problem 3.  Problem 3 shown (again) below, and then trial and error for Project 7.

BELOW IS PROJECT 3 TEXT
> Initially, create a list of prime numbers using Sieve of Eranthoses.
>> That can be done in different ways, including dictionary, list of dictionaries and set.
>> I'll try with a set approach. N.B. Set is not subscriptable, but can be iterated through. (for s in my_set: ...)
>> Also, cannot remove from set whilst iterating over it!

> Going through a tree needs while True: ...
>> However, this comes AFTER for p in primes # <= that caused me a lot of grief/time!


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
# initially generate the list of prime numbers using Sieve of Eratothenses (without 1)
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
# Step 1. What is just larger than sqrt of 600851475143
z = 600851475143
z_root = z**0.5
z_rootA = round(z_root)
print(z_rootA)

# Step 2. So now we need to find prime factors up to z_rootA
z1 = Eratosthenes(z_rootA)
print(max(z1))
# ok, maximum value needed for sieve is 775121

# Step 3. We need to generate all prime numbers up to 137, using Eratothesnes function,
# and then check prime factors of 600851475143, but only with a sieve up to 137.
# I.e. don't need to sieve up to 600851475143.
# If it has no prime factors <= 137, it is a prime itself.
# This needs a modification to prime_factors, to input the max value of the sieve
def prime_factors2(limit, sieve):
    # create a function for checking if something is integer
    def is_integer(num):
        if round(num) / num == 1:
            return True
        else:
            return False

    # everything else
    primes = Eratosthenes(sieve)
    # print(primes)
    prime_factors = []
    remainder = limit

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



z2 = prime_factors2(600851475143, 775121)
print(z2)
print(max(z2))
# ^ this is the answer



# later Euler puzzle 7
# trial and error to find 10001st prime
z = Eratosthenes(104746)
print(len(z), z[-1])