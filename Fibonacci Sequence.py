# Program to display the Fibonacci sequence up to n-th term
def finonacci(term):
    n1, n2 = 0, 1
    count = 0
    if term <= 0:
         print("Please enter a positive integer")

    elif term == 1:
        print("Fibonacci sequence upto",term,":")
        print(n1)

    else:
        print("Fibonacci sequence:")
    while count < term:
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       count += 1

terms = int(input("How many terms? : "))
finonacci(terms)