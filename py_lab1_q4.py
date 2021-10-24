number = int(input("enter the number want to check:"))
if number > 0:
	print("divisors of",number)
	for i in range(1, number+1):
		if number % i == 0:
			print(i,end=" ")
	print()
else :
	print("enter a number greater than 0")