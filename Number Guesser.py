import random
import math

lower = int(input("enter lower range"))

upper = int(input("enter heigher range"))


x = random.randint(lower, upper)
count=1
while(count<=10):
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in ")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")


    if (count==10):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
    count=count+1




