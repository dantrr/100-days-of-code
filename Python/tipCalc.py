bill = float(input("What is your bill amount? "))
percent = float(input("What percentage would you like to tip? "))
tip = (bill*percent/100)
print(f"Your tip should be ${tip}")