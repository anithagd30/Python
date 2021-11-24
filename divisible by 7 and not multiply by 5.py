list=[]
def numbers():
    for i in range(2000,3200):
        if i%7==0 and (i%5)!=0:
         list.append(str(i))
      
    return list 


list=numbers()
print(','.join (list))

