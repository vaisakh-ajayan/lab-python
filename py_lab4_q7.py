def series(n):
	if n <= 0:
		return 0
	else:
		return n + series(n-2)

input_number = int(input("enter the number want to check:"))
if input_number >= 0:
	print("sum of series is", series(input_number))
else:
	print("Invalid entry, enter positive number")
