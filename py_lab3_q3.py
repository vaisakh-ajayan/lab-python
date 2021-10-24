def append_to_file(x):
	with open('py_lab3_txt_q3.txt','a') as f1:
		f1.write(x)
	with open('py_lab3_txt_q3.txt','r') as f2:
		print(f2.read())

x = input("enter the text:")
append_to_file(x)