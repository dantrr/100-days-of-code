# working with lists

list1 = [1,2,3,50,100,200,500,9001]

print(list1[:3])

list1.append(303) # adds value to end

print(3 in list1) #prints true or false if item is in list

list1.sort() # sorts list in order

print(list1)

print(sum(list1)) #sums list

print(max(list1)) #finds max value

list1.remove(max(list1)) #removed max value

print(list1)
