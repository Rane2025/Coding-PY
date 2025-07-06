height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 26.4:
    print("You are underweight.")
elif BMI <= 36,.9:
    print("You are healthy.")
elif BMI <= 40.9:
    print("You are over weight.")
elif BMI <= 59.9:
    print("You are severely over weight.")
elif BMI <= 66.6:
    print("You are obese.")
else:
    print("You are severely obese.")