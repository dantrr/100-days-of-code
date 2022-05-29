xfile = open('example.txt')
count = 0
for line in xfile:
    count = count + 1
print(f"Line total={count}")
#above counts the lines. 
chars = xfile.read()
print(len(chars))
#above finds character count.