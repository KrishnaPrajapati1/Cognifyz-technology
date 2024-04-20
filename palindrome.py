def is_palindrome(string):

  string = string.replace(" ", "").lower()


  reversed_string = string[::-1]


  return string == reversed_string

str=input("enter any string: ")
check=is_palindrome(str)
if(check):print("String is palindrome")
else:print("String is not palindrome")

