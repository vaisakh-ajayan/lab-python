high = int(input("how many nos do you want to enter:"))
lst = []
for i in range(high):
	n = int(input("enter number:"))
	lst.append(n)
print("enterd list is", lst)
print("sum of numbers ", sum(lst))
