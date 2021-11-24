import random
n = 100
guess = int(n* random.random())
if guess < 1 or guess > 100:
    print ("Enter number in range")
elif guess > n:
    print ("Too high")
elif guess < n:
    print ("Too low")
elif guess == n:
    print ("Correct!")
