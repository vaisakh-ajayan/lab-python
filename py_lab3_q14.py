def corresponding_lines(file_1, file_2, file_3):
	with open(file_1, 'r') as f1:
		with open(file_2, 'r') as f2:
			with open(file_3, 'r+') as f3:
				for line in f1.readlines():
					f3.write(line.strip('\n') + '\t' + f2.readline() + '\n')
				print("combined file is \n\n")
				f3.seek(0)
				print(f3.read())

corresponding_lines(
	'py_lab3_txt_q14_1.txt',
	'py_lab3_txt_q14_2.txt',
	'py_lab3_txt_q14_3.txt')
