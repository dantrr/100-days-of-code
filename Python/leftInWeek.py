days = 6
hours = 8
currentHour = 40
#as of 0800 day 5

totalHours = days * hours
percentComp = currentHour/totalHours*100
hoursleft = totalHours-currentHour
perRound = round(percentComp , 2)
print(f"The week is {perRound}% complete.")
print(f"There are {hoursleft} hours left in the week.")