days = 6
hours = 8

totalHours = days * hours

currentHour = 24
#as of 0800 day 3

percentComp = currentHour/totalHours*100
hoursleft = totalHours-currentHour
perRound = round(percentComp , 2)

print(f"The week is {perRound}% complete.")
print(f"There are {hoursleft} hours left in the week.")