string = input("enter a string to check:")
string = string.casefold()
reverse = string[::-1]
if string == reverse:
	print("string is pallindrome")
else:
	print("string is not pallindrome")