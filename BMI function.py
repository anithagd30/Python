def bmi_input():
    weight=float(input("Enter your weight in kg "))
    height= float(input("Entet your height in cm "))
    return weight,height


def calculate_bmi(weight,height):
    bmi = weight /( height/100)*2
    bmi_index(bmi)
    print("BMI is ", bmi)

def bmi_index(bmi):
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
user_weight,user_height= bmi_input()
calculate_bmi(user_weight,user_height)
    





    