# dictionaries: common applications, day 36 of coding.

# you can declare values as you see them, or need them, for example in an inventory, you can declare new "labels".

counts ={"quincy":1,"mrugesh":42,"beau":100,"0":10}
print(counts.get("kris",0))

#since kris is not in counts, it will just print the default listed, 0

# dictionaries and loops. 

# you can run a loop through the dictionary. 

# items() can get both keys and values; i.e. 
print(counts.keys()) # to print just keys
print(counts.items())
 