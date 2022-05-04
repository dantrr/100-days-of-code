hoursStr = input("Enter hours worked: ")
payRateStr = input("Enter your Pay Rate: ")

try:
    hours = float(hoursStr)
    payRate = float(payRateStr)
except:
    hours = 0
    payRate = 0
    print("Use a number, not text.")
grossPayStr = str(hours * payRate)
print ("Your gross pay is $" + grossPayStr)

