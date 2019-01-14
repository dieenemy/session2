h = int(input("Enter your height(cm) :"))
w = int(input("Enter your weight(kg) :"))
h1 = h*0.01

BMI = w/(h1*h1)
print(BMI)

if BMI < 16:
    print("Severely")
elif BMI < 18.5:
    print("Underweight")
elif BMI <25:
    print("Normal")
elif BMI <25:
    print("Overweigh")
else:
    print("Obese")
 