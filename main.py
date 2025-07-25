#BMI CHECKER

input_weight = float(input("Enter your weight in kg: "))
input_height = float(input("Enter your height in meters: "))

BMI = input_weight / (input_height ** 2)

print("Your BMI is:", BMI)

if BMI < 18.4:
    print("You are underweight")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight")
elif 25 <= BMI < 29.9:
    print("You are overweight")
elif 30 <= BMI < 34.9:
    print("You are obese (Class 1)")
elif 35 <= BMI < 39.9:
    print("You are obese (Class 2)")
else:
    print("You are obese (Class 3)")    

