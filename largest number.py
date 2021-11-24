num_list =[]

def add_num_list():
    for i in range(4):
        numbers = int(input("Enter number "))
        num_list.append(numbers)
    return num_list

def find_max_number():
    max=0
    for number in num_list:
        if number > max:
            max = number
    return max

    

def sort_list(list1):
    
    for i in range (len(list1)):

        for j in range(i+1,len(list1)):

            if (list1[i]>list1[j]):
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1


numbers_list=add_num_list()
print (numbers_list)

max_num=find_max_number()
print("The max number is: ", max_num)

temp_list=sort_list(numbers_list)
print ("Ascending number ",temp_list)

