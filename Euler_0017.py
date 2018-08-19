"""
Project Euler: https://projecteuler.net/problem=17

Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.


My Approach?
> Initially quite complex, as I did not want to iterate over 1000 numbers.  However this approach
would have used a lot of memory, so have decided to go with iteration and lower memory variables.
> Basically a more conventional approach.
> First step is to create the dictionaries you want, and basically as you iterate, to create one
huge string whose length is counted at the end.
> The complication comes from the numbers 11-19 being in a different pattern than all else.

Afterwards
> Discovered there is a Python num2words library, though doesn't seem much used
(or part of main supported packages?)

"""
# needed for rounding with floor method
import math

# create dictionary where the integer is the key, and the string equivalent is the value.
numbers = {0:'', 1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
           7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
           13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
           18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30:'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
           100: 'hundred', 1000: 'thousand'
           }

def mini_func(num):
    """ Just writes any number as string, as required in puzzle"""
    thousands = math.floor(num/1000)
    hundreds = math.floor(num/100)
    tens = math.floor((num % 100) / 10) * 10
    units = num % 10

    if num == 0:
        long_string = numbers[num]
    elif num == 1000:
        long_string = numbers[thousands] + 'thousand'
    elif (num % 100) == 0:
        long_string = numbers[hundreds] + 'hundred'
    elif (hundreds == 0) and (10 < num % 100 < 20):
        long_string = numbers[10 + units]
    elif (hundreds == 0):
        long_string = numbers[hundreds] + numbers[tens] + numbers[units]
    elif (hundreds != 0) and (10 < num % 100 < 20):
        long_string = numbers[hundreds] + 'hundredand' + numbers[10 + units]
    else:
        long_string = numbers[hundreds] + 'hundredand' + numbers[tens] + numbers[units]

    return long_string


# easy thing now is just to iterate over range(1001) for min_func and add to a long_string
long_string = ''
for n in range(0, 1001):
    # print(mini_func(n))
    long_string += mini_func(n)

# print(long_string)
print(len(long_string))

"""
An interesting way seen on Project Euler solution thread for this is to add a dictionary item for 
every number, in a kind of automated fashion. 
While the partitioning of number is elegant does ask for 1001 items in the dict, however!

"""



