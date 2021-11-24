num_list =[]

def add_num_list():
    for i in range(6):
        numbers = int(input("Enter number "))
        num_list.append(str(numbers))
        num_tuple=tuple(num_list)
    return num_tuple



num_tuple=add_num_list()
print("numbers ")

print(num_list)
print(num_tuple)

