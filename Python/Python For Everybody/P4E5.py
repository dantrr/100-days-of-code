i = 0
x = 0
while i < 4:
    x+=i
    i+=1

print(x)

words = ["Hello","World","!"]
print(words[0])
print(words[1])
print(words[2])

#each row needs brackets
m = [
    [0, 2, 3],
    [4, 5, 1],
    [300, 450, 1000]
]
print(m[2][2])

seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]

row = int(input("What is the seat row? "))
col = int(input("What is your seat column? "))
print(seats[row][col])