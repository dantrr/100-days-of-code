#weight is in kg and is int.
#height is a float, and is in meters.
#115 kg
#1.7272 m height
weight = int(0)
height = float(0.0)
#bmi formula is weight/height**2
weight = int(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = weight/height**2

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi > 30:
    print("Obesity")
else: 
    print("Use valid numbers.")