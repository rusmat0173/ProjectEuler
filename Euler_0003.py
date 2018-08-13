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
# v Data Science form Scratch books prefers this method of division!
from __future__ import division

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
#
# z = 1000000
# z_root = z**0.5
# z_rootA = round(z_root)
# print(z_rootA)
# start = time.time()
# z1 = prime_factors(z_rootA)
# z = Eratosthenes(1000002)
# print(z1)
# end = time.time()
# print(end - start)
# print(max(z))

# later Euler puzzle
# trial and error to find 10001st prime
z = Eratosthenes(104746)
print(len(z), z[-1])


"""
DICTIONARIES AND LAMBDA PRACTICE

"""
# dictionaries/lambda practice
musicians = [{'id': 1, 'name': 'Paul McCartney', 'group': 'beatles'},
             {'id': 2, 'name': 'John Lennon', 'group': 'beatles'},
             {'id': 3, 'name': 'Ringo Starr', 'group': 'beatles'},
             {'id': 4, 'name': 'George Harrison', 'group': 'beatles'}]

w = sorted(musicians, key=lambda musicians: musicians['name'])
print(w)
print('\n', musicians)
musicians.sort(key=lambda musicians: len(musicians['name']), reverse=True)
print('\n', musicians)

for person in musicians:
    print('{}\t\t{}'.format(person['name'], person['group']))

musicians.append({'id': 5, 'name': 'Boy George', 'group': 'Culture Club'})
musicians.sort(key=lambda musicians: len(musicians['group']), reverse=True)
print('\n', musicians)

for person in musicians:
    if person['name'] == 'Boy George':
        person['instrument'] = 'vocals'
        print(person)


beatles = {'John Lennon': 'guitar',
           'Paul McCartney': 'bass',
           'Ringo Starr': 'drums',
           'George Harrison': 'guitar',
           'finn foobar': 'spoons'
           }

print(beatles.keys())
for item in beatles.keys():
    print(item, beatles[item])

beatles = {'John Lennon': 'guitar',
           'Paul McCartney': 'bass',
           'Ringo Starr': 'drums',
           'George Harrison': 'guitar',
           'finn foobar': 'spoons'
           }

for person in musicians:
    for keys, values in beatles.items():
        if person['name'] in keys:
            person['instrument'] = beatles[person['name']]

print('\n', musicians)
# ^ although this works well, it is not particularly efficient, and somewhat convoluted.
# The reason is that there was no common index between te two dictionaries.

# final practice, sort by last name only
george = {'id': 4, 'name': 'George Harrison', 'group': 'beatles'}
george['first name'] = george['name'].split()[0]
george['last name'] = george['name'].split()[-1]
print(george['first name'])
print(george['last name'])

print()

for person in musicians:
    if person['name'] == 'Paul McCartney':
        person['name'] = 'Paul Anthony McCartney'
        print(person)

musicians.sort(key=lambda musicians: musicians['name'].split()[-1], reverse=False)
for person in musicians:
    print(person['name'])

print()
# POWERFUL TECHNIQUE FOR PRINTING AND RETURNING!!!
# v the below works if we use (e.g.) print([...]), but not if we use print(...)!!!
print([musician['name'] for musician in musicians])
print([musician['name'] for musician in musicians if musician['group'] != 'beatles'])

for musician in musicians:
    musician['genre'] = 'pop'

print([[musician['name'], musician['genre']] for musician in musicians])

def find_beatle(musicians):
    return [musician['name'] for musician in musicians if musician['group'] == 'beatles']

print(find_beatle(musicians))

# more generally
def find_group(musicians, group):
    return [musician['name'] for musician in musicians if musician['group'] == group]

print(find_group(musicians, 'Culture Club'))

# another use of this
names_list = [person['name'] for person in musicians]
print('names list:', names_list)

# more dictionary sort practice
beatles = [{'id': 1, 'name': 'Paul McCartney', 'group': 'beatles', 'instrument': 'bass'},
             {'id': 2, 'name': 'John Lennon', 'group': 'beatles', 'instrument': 'spoons'},
             {'id': 3, 'name': 'Ringo Starr', 'group': 'beatles', 'instrument': 'drums'},
             {'id': 4, 'name': 'George Harrison', 'group': 'beatles', 'instrument':'guitar'}]

beatles.sort(key=lambda x: x['instrument'])
print([beatle['name'] for beatle in beatles])


""" 
SOCIAL NETWORK EXERCISE FROM DATA MGT. FROM SCRATCH BOOK

"""
# social network exercise from Data Mangement from Scratch book, cpt. 1
more_people = [{'id': 6, 'name': 'Duke Ellington', 'group': 'Duke Ellington Band',
                'instrument': 'piano', 'genre': 'jazz'},
               {'id': 7, 'name': 'Simon Lebon', 'group': 'Duran Duran',
                'instrument': 'keyboards', 'genre': 'pop'},
               {'id': 8, 'name': 'Adele', 'group': 'soloist',
                'instrument': 'vocals', 'genre': 'ballads'},
               {'id': 9, 'name': 'Patti Smith', 'group': 'Patti Smith Band',
                'instrument': 'bass', 'genre': 'rock'}
               ]

for person in more_people:
    musicians.append(person)
musicians.sort(key=lambda musicians: musicians['name'].split()[-1], reverse=False)
print([musician['name'] for musician in musicians])

friendships = [(1,2), (1,3), (1,4), (1,7), (1,8), (2,1), (2,3), (2,4), (2,6), (2,9),
               (3,1), (3,2), (3,4), (3,5), (3,7), (3,8), (4,1), (4,2), (4,3), (4,6),
               (5,7), (5,8), (6,2), (7,1), (7,5), (7,9), (8,1), (8,3), (9,1), (9,8)]

# let's imagine friends is inaccurate as not all relationships are reported in both directions
# we can fix this with a set
friends = set()
print(friends, type(friends))

for relations in friendships:
    friends.add((relations[0], relations[1]))
    friends.add((relations[1], relations[0]))

# now add to musicians
for musician in musicians:
    musician['relations'] = []

for musician in musicians:
    for pair in friends:
        if pair[0] == musician["id"]:
            musician['relations'].append(pair)

print()
print(musicians)
# ^ works nicely!

# number of friends per person
def num_friends(musicians):
    num_friends_list = []
    for musician in musicians:
        num_friends_list.append((musician['name'], len(musician['relations'])))
    num_friends_list.sort(key=lambda x: x[1], reverse=True)

    return num_friends_list

print(num_friends(musicians))


# average number of friends per person
z = num_friends(musicians)
total = sum([item[1] for item in z])
average = total / len(z)
print(average)


# now look for friend of friends!
def friend_of_friend(person, musicians):
    """ takes person in musicians, and checks their friends of friends"""
    # check person is in musicians
    # use of any command from:
    # https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work
    names = [musician['names'] for musician in musicians]

    def check_name(person, musicians):
        if person in names:
            return True
        else:
            return False

    if not check_name(person, musicians):
        return "Invalid name"

    # need to get person's id
    def find_id(person, musicians):
        for musician in musicians:
            if musician['name'] == person:
                unique_id = musician['id']
                return unique_id

    unique_id = find_id(person, musicians)
    # ^ actually, not sure this is needed

    # list person's friends, so you can check their friends
    def find_friends(person, musicians):
        """ returns a set"""
        friends = []
        for musician in musicians:
            if musician['name'] == person:
                for pair in musician['relations']:
                    friends.append(pair[1])
        return set(friends)

    friends = find_friends(person, musicians)

    # find level2 friends from friends set
    def level2_friends(friends, musicians):
        """ returns a set"""
        friends_of_friends = []
        for musician in musicians:
            if musician['id'] in friends:
                for pair in musician['relations']:
                    friends_of_friends.append(pair[1])

        level2_friends = friends_of_friends
        return set( level2_friends)

    level2_friends = level2_friends(friends, musicians)

    # finally, need to make sure no overlap between friends and level2friends
    do_you_know = level2_friends - friends

    return do_you_know

# z = friend_of_friend('Duke Ellington', musicians)
# print(z)



""" 
Not working, 1 known thing:
i. check_name function

Other than that seems to work
However, it's a lot more code than the book's brute force double-looping.
Book had it easier as I added tuples, e.g. (1,2) to the dictionary - not just, e.g. 2, 3, 4, ...
I won't do book's approach as is a kind of naive approach and is very nested, so hard to follow.

Actually the best way to do this is to create a 0/1 matrix from the list
of friends, and find as many levels as you want using matrix algebra. 
(Travelling salesman problem.) However, for massive datasets that would be 
computationally difficult.

"""

names = [musician['name'] for musician in musicians]
def check_name(person, musicians):
    if person in names:
        return True
    else:
        return False

print(check_name('John Lennon', names))













