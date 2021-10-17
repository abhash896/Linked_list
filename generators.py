def gen(n):
    for i in range(n):
        yield i


# Creating a generator object.
g = gen(3)

# By applying __next__() operator, the generator object can be iterated one at a time.
print(next(g))
print(g.__next__())
print(g.__next__())

# Alternative approach to iterator over to a generator object.

# for i in g:
#     print(i)
