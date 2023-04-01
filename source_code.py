import math
print("Welcome to BMI Calculator!");
print("BMI Chart:\n")
print("          BMI          |             BMI CATEGORY      ")
print("-----------------------|-------------------------------")
print("Less than 15           |Very severely underweight")
print("Between 15 and 16      |Severely underweight")
print("Between 16 and 18.5    |Underweight")
print("Between 18.5 and 25    |Normal")
print("Between 25 and 30      |Overweight")
print("Between 30 and 35      |Moderately Obese")
print("Between 35 and 40      |Severely Obese")
print("Over 40                |Very severely obese")
weight = float(input("\nEnter your Weight (in kg): "))
height = float(input("\nEnter your Height (in cm): "))
bmi = (weight / (height ** 2)) *10000
print("Your BMI is",bmi)
if (bmi<15):
    print("\nYou are very severely underweight")
elif(bmi>=15 and bmi<16):
    print("\nYou are severely underweight")
elif(bmi>=16 and bmi<18.5):
    print("\nYou are underweight")
elif(bmi>=18.5 and bmi<25):
    print("\nYou are Normal (healthy)")
elif (bmi >= 25 and bmi<30):
    print("\nYou are overweight")
elif(bmi>=30 and bmi<35):
    print("\nYou are moderately Obese")
elif(bmi>=35 and bmi<40):
    print("\nYou are severely Obese")
elif(bmi>=40):
    print("\nYou are very severely obese")
input()