def checkPassword(password):
    upperChars,specialChars, digits, length = 0, 0, 0, 0
    length = len(password)
    for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    if (upperChars >= 2 and digits >= 2 and specialChars >= 1):
        print("The strength of password is strong.\n")
    else:
        print("The strength of password is weak.\n")

password = input("Please enter password: ")
checkPassword(password)