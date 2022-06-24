import re #regular expressions

# re.search("^From: ", line) ### searches for this text at the beginning of a line 

# \s searches whitespace
#\S searches any nonswhitespace

# . matches any character

# * character is "any amount of times"

x = "my 2 favorite numbers are 9 and 42"

y = re.findall("[0-9]+", x) #finds all numbers in x

print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

# \$ is a REGEX dollar sign, as $ is sometimes used for other things. 