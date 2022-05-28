#normal biweekly pay is $944
# Formula paycheckAmt*saveRate/100
netPay = 944

dontTouch= 262

leftOver = netPay - dontTouch
# below are percents
investRate = 15
saveRate = 10

print(f"Investment amount should be ${leftOver * investRate / 100}")
print(f"Savings amount should be ${leftOver * saveRate / 100}")

# $102 save x2 = $204
# $68 save x2 = $136