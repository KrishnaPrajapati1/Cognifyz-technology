import re

text = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):

	if(re.fullmatch(text, email)):

		print("Valid Email")
	else:
		print("Invalid Email")
if __name__ == '__main__':

	email = input("enter any email: ")

check(email)

