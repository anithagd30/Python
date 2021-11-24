weight =[]
height =[]
category =[]

def add_values_in_list(bmi):
    "bmi calculator"
    print("start calculating def")
    for i in range (3):
        calculate = input("enter value ")
        bmi.append(calculate)

    return bmi

my_weight = add_values_in_list(weight)
my_height = add_values_in_list(height)
my_category = add_values_in_list(category)
