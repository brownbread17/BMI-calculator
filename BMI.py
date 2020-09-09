weight = float(input("Enter weight(Kg): "))
height = float(input("Enter height(M): "))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 25:
    print("You are normal weight")
else:
    print("You are overweight")
print(BMI)
