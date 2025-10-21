#! /usr/bin/env python3


# 5.1 More on Lists

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)     

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

squares = list(map(lambda x: x**2, range(10)))
# equivalently
squares = [x**2 for x in range(10)]


# 5.3 Tuples

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888  # NOT POSSIBLE

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)


# 5.4 Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both


# 5.5 Looping techniques

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# A and not B or C is equivalent to (A and(not B)) or C