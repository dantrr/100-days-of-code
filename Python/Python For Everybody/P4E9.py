# dictionaries day 35

# a dictionary is a "bag" of values, essentially a label on an item
# they allow database-like operations in python

bag = dict()
bag["money"] = 150
bag["candy"] = 10
bag["gun"] = 1

print(bag)
print(bag["money"])

bag["money"] = bag["money"] + 300

print(bag)

# dictionaries are like lists, except with different "keys", instead of index numbers, you use your own custom key essentially
# you can also use numbers as the index

# you can also fill the dict at declaration using curly braces:
forest = {"cedar":15, "bushes":200, "pine":50 }
print(forest)
