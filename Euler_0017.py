"""
Project Euler: https://projecteuler.net/problem=17

Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


My Approach?
> Did using work on Problem 3.  Problem 3 shown (again) below, and then trial anderor for Project 7.

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