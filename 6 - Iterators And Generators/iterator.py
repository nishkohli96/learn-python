numbers = [1, 2, 3]

iterator = iter(numbers)
# <list_iterator object at 0x100930190>
# print(iterator)

# An iterator produces values one at a time using: next()
print(next(iterator))
print(next(iterator))
print(next(iterator))

# returns "StopIteration" exception as iterator finished all iterations
# print(next(iterator))
