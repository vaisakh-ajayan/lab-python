def read_func(x):
	with open("py_lab3_txt_q2.txt","r") as f1:
		for i in range(x):
			print(f1.readline())


x = int(input("no of lines to read:"))
read_func(x)