#calculate BMI 
weight=float(input("Insert weight in kg"))
height= float(input("Insert height in cm"))
bmi = weight /( height/100)*2
print("BMI is ", bmi)
# BMI if else
if bmi <= 16:
    print("Severely Underweight")
elif bmi <=18.4:
    print("Underweight")
elif bmi <=24.9:
    print("Normal")
elif bmi <=29.9:
    print("overweight")
elif bmi <=34.9:
    print("Moderately obesse")
elif bmi <=39.9:
    print("Severely Obese")
elif bmi >40.0:
    print("Morbidly Obese")


    