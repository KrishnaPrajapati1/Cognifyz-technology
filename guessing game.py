import random
print("Let me think of a number between 1 to 100: ")

lower = int (1)

upper = int (100)


x = random.randint(lower, upper)
count = 1
while(count):
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
    count = count+1




