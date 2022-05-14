print("Hello World!")

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

#below is a user DEFINED function, starting with def
# def example():
#     print("test")

#Arguments can specifify differences in same func. 

# def example(lang)
#     if lang == en
#         print("en example")
#     elif lang == es 
#         print("es example")

#return can be used to concatentate with str such as
# def example()
#     return "Hello"
#print (example(), Bob)
