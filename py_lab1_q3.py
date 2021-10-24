a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = list(filter(lambda x: x<5, a))
print("elements less than 5 are")
for i in x:
	print(i)