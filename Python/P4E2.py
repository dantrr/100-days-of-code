for i in [1, 2, 3, 4, 5]:
    print(i)
#definite loops


#what's the largest number
large = 0
for largest in [3, 41, 12, 9, 74, 15]:
    if largest > large:
        large = largest
print(large)

#counting in a loop
zork = 0
print(f"Before {zork}")
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(f"{zork} {thing}")
print(f"After {zork}")

#finding the average
count = 0 
sum = 0
print(f"Before {count} {sum}")
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print(f"After {count} {sum} {sum/count}")

#filtering
print("Before")
for value2 in [9, 41, 12, 3, 74, 15]:
    if value2 > 20:
        print(f"Filtered {value2}")
print("After")

#bool searching
found = False
print("Before")
for value3 in [9, 41, 12, 3, 74, 15]:
    if value3 == 3:
       found = True
    print(found, value3)
print("After")

# is is stronger than =
#properly compare, above example was inefficient
large = None
for largest in [3, 41, 12, 9, 74, 15]:
    if large is None:
        large = largest
    elif large < largest:
        large = largest        
print(large)