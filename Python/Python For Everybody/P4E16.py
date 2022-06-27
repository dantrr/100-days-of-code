#networking: text processing and urllib 

# most websites use UTF-8

# 8 bits is a byte and all that stuff i already knew, ACSII is the standard, all characters are essentially agreed upon unicode. 

########

# urllib is kinda like importing a socket, but simpler.

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) 


import urllib.request
fhand1 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand1:
    print(line.decode().strip()) 