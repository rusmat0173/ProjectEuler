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
# from __future__ import division
# ^ actually not needed as already have Pyuthon 3!

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

# Also, subscriptable in a sense
print()
print(beatles[0])
print(beatles[0]["name"], "!!!")
print()

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
    names = [musician['name'] for musician in musicians]
    def check_name(person, names):
        if person in names:
            return True
        else:
            return False

    if not check_name(person, names):
        return "Invalid name"

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
        """
        returns a set
        Also returns friends with yourself that has to be adjusted at very end
        """
        friends_of_friends = []
        for musician in musicians:
            if musician['id'] in friends:
                for pair in musician['relations']:
                    friends_of_friends.append(pair[1])

        level2_friends = friends_of_friends
        return set(level2_friends)

    level2_friends = level2_friends(friends, musicians)

    # need to make sure no overlap between friends and level2friends and original person
    level2_ids = level2_friends - friends

    # find names from ids
    def names_from_ids(ids, musicians):
        do_you_know = []
        for musician in musicians:
            if musician['id'] in ids:
                do_you_know.append(musician['name'])

        return do_you_know


    output_set = names_from_ids(level2_ids, musicians)
    # finally need to remove original person from being their own friend
    output_set.remove(person)

    # print(names_from_ids(friends, musicians))
    # print(names_from_ids(level2_ids, musicians))
    return output_set


z = friend_of_friend('Adele', musicians)
print(f"Do you know: {z} ?")

# or, turn z into a list and string
# It's a bit gritty and cumbersome, but belt and barces for immutable strings
z0 = list(z)
z0.insert(-1, 'or')
z1 = str(z0)
z2 = z1.strip("[]")
z3 = z2.replace("'", "")
last_comma = None
for idx in range(len(z3)):
    if z3[idx] == ',':
        last_comma = idx
z4 = z3[:int(last_comma)] + z3[last_comma +1:]
print(f"Do you know: {z4} ?")



""" 
^ Works well.

However, it's a lot more code than the book's brute force double-looping.
Book had it easier as I added tuples, e.g. (1,2) to the dictionary - not just, e.g. 2, 3, 4, ...
I won't do book's approach as is a kind of naive approach and is very nested, so hard to follow.

Actually the best way to do this is to create a 0/1 matrix from the list
of friends, and find as many levels as you want using matrix algebra. 
(Travelling salesman problem.) However, for massive datasets that would be 
computationally difficult.

"""
# Python's Easter Egg: the Zen of Python, from 'import this'
import this

# Let's try the book's approach

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

# Additional [RA] check what is happening
print("!!!", users[0])

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]     # for each of user's friends
            for foaf in friend["friends"]]    # get each of _their_ friends


z = friends_of_friend_ids_bad(users[0])
print(z)

# OK, my turn. First add ['relations2'], just the single id number of the level1 friends
print(musicians)
for musician in musicians:
    musician["relations2"] = []
    for item in musician["relations"]:
        musician["relations2"].append(item[1])

print(musicians[0])
# ^ ok, works. Now use same function as book, with correct (for me) variable names
def check(name, musicians):
    for musician in musicians:
        print(musician['instrument'])
        if musician['instrument'] == name:
            return True
        else:
            pass
    return False


print(check('keyboards', musicians))
# print(musicians)

"""
Actually, none of the above worked because of the difference between indexing from 0 as per book, 
and my string 'id' indexing. Not worthwhile to fix!

LESSON: (again) go for dictionary of dictionaries, not list of dictionaries, as Rice MOOC also does.

TASKS:
1. Create a toy dict of dict.
2. Search dict of dict.
3. Sort dict of dict by some internal key.

"""
# Task 1. sort musicians, so that again again in ID order.
musicians.sort(key=lambda musicians: musicians['id'], reverse=False)
# remove the relationships2 field, which is the last field
for musician in musicians:
    del musician['relations2']
# now rename ids to start with 0, just to make easier
musicians_plus = {}
for musician in musicians:
    musician['id'] -= 1
for idx, musician in enumerate(musicians):
    musicians_plus[idx] = musician
# print(musicians_plus)

# Task 2. search dict of dicts
def search(search_term, dict_of_dicts):
    """ search dictionary of dictionaries. Allows multiple results """
    output = []
    for key, values in dict_of_dicts.items():
        inner_dict = values
        if search_term in inner_dict.values():
            output.append(dict_of_dicts[key])
        else:
            pass
    if len(output) == 0:
        return "Unsuccessful search"
    else:
        return f"Search output is: {output}"

print()
print(search('guitar', musicians_plus))

# Task 3. sort dict of dicts by some internal key.
# Dude, is dictionary not a list!
# We could use OrderedDict, or turn into a some kind of list than sort,
# turning back into dictionary if desired. # <= prefer this to OrderDict
def sorter(sort_field, d_of_d):
    l_of_d = [value for value in d_of_d.values()]
    l_of_d.sort(key=lambda x: x[sort_field])
    d_of_d2 = {item['id']:item for item in l_of_d}
    return d_of_d2

z = sorter('group', musicians_plus)
print('\nsorter:\n', z)

"""
Chapter 4 of Grus' Data Mgt. from Scratch book (10-day trial copy).

N.B. zip (x, y), zip is a generator, so only works once!!!

N.B. Python has its own array, but not so efficient, so everyone uses numpy

"""
v, w = [1, 2], [2, 1]
# print(v + w)
# ^ not what we want

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

z = [vi +  wi for vi, wi in zip(v, w)]
# print(z)
# ^ this use the same powerful syntax we used earlier in this file.
# That  is 'list comprehension'!

friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0.5, 2, 0, -1, 'a', 'b', 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

print(friendships[0][2] == 1)
print(friendships[0][8] == 1)

# "Similarly, to find the connections a node has, you only need to inspect the column
# (or the row) corresponding to that node:"

# So how does is_friend work?????
friends_of_four = [i                                              # only need
                   for i, is_friend in enumerate(friendships[4])  # to look at
                   if is_friend]
print(friends_of_four)

friends_of_five = [i                                              # only need
                   for i, cheese in enumerate(friendships[5])  # to look at
                   if cheese]                                  # one row
print(friends_of_five)

# ^ Wow, that is powerful: the is_friend/cheese work so long as is a non-zero matrix entry!!!
# (Some kind of boolean.)
list0 = [0, 0, 1, 0, 2, 0 , -2, 8]
print([i for i, non_zero in enumerate(list0) if non_zero])



