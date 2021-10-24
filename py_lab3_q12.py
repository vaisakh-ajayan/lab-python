def write_list(l1):
	with open('py_lab3_txt_q12.txt', 'w') as f1:
		for line in l1:
			f1.write("{} \n".format(line))
	with open('py_lab3_txt_q12.txt', 'r') as f2:
		print("\ncontents are \n", f2.read())
			

n = int(input("enter length of list:"))
list_1 = list()
print("enter elements")
for i in range(n):
	list_1.append(input())
write_list(list_1)