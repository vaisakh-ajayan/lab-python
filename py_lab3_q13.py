def copy_files(file_1, file_2):
	with open(file_1, 'r') as f1:
		list_1 = f1.readlines()
		with open(file_2, 'w') as f2:
			for line in list_1:
				f2.write(line)
		print("contents in new files is \n\n")
		with open(file_2, 'r') as f3:
			print(f3.read())

copy_files('py_lab3_txt_q13_1.txt', 'py_lab3_txt_q13_2.txt')