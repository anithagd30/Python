import random
n = random.randint(1,10)
guess = int(input("Insert number "))
if guess < 1 or guess > 10:
    print ("Enter number in range")
elif guess > n:
    print ("Too high")
elif guess < n:
    print ("Too low")
elif guess == n:
    print ("Correct!")



