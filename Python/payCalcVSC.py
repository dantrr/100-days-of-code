hours = 80

pay = 16.87

grossPay = hours * pay

tax = grossPay - 944

netPay = grossPay - tax
netString = str(netPay)

print("Your biweekly pay is $"+netString)

