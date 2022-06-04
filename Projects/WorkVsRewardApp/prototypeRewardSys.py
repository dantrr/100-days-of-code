work = input("How many hours did you work or study today? ")
work = float(work)
# formula will be 25% of work time is now free time.
playPercent = 25
theMath = work * playPercent / 100
rounded = round(theMath, 2)
print(f"You now have {rounded} hours of free time available.")
