def addition():
    result = int(num1 + num2)
    print(result)

def subtract():
    result = int(num1 - num2)
    print(result)

def multi():
    result = int(num1 * num2)
    print(result)


def division():
    result = float(num1 / num2)
    print(result)

def percentage():
    result = float(num1 % num2)
    print(result)


num1 = int(input("Enter a number: "))
num2 = int(input("Enter b number: "))
operator = input("enter operator: ")
if(operator=="+"):addition()
if (operator == "-"):subtract()
if (operator == "*"):multi()
if(operator=="/"):division()
if(operator=="%"):percentage()








