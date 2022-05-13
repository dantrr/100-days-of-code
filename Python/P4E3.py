for n in "banana":
    print(n)
#above prints each letter
#each letter is indexed, starting from 0
fruit = "watermelon"
letter = fruit[0]
print(letter)
for n in "watermelon":
    print(f"Meme town {n}")
    
#string slicing:
py = "Monty Python"
print(py[0:4])
print(py[8:])
print(py[6:20])

#in is a logical operator that returns true or false

# .lower() is a function call, will lowercase a string

# .find() finds substring within a string and gives position

# .replace() replaces a string with something else, including every instance of a letter

# .lstrip() and .rstrip() strips whitespace off of a str

# .startswith() returns true or false for string start

data = "stephen.marquard@uct.ac.za "
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
#above finds just the host for the email
