fhand = open("example.txt")

#open creates a handle variable as seen on left to allow file manipulation.
# \n creates a new line
#a txt file has \n at the end of every line. 

#print function creates a new line
#strip function to remove whitespace also removes newline.

for cheese in fhand:
    print(cheese)

#for each line in handle^

count = 0
for line in fhand:
    count = count + 1
print(f"Line count:{count}")


### Below will read the whole file into a string; len == length
# fhand = open("example.txt")
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

for line in fhand:
    if line.startswith("From: "):
        print(line)
#above will filter to lines that match string.

#all lines in text files end in \n, a newline

for line in fhand:
    line = line.rstrip()
    if line.startswith("From: "):
        print(line)

fname = input(f"Enter the filename: ")
try:
    thand = open(fname)
except:
    print(f"File cannot be opened: {fname}")
    quit()
newCount = 0
for line in thand:
    if line.startswith("Subject: "):
        count = count + 1
print(f"There were {count} subject lines in {fname}")

