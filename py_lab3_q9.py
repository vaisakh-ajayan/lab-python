def no_of_lines(file_ref) :
	with open(file_ref, 'r') as f1:
		list_1 = f1.readlines()
		print("no. of lines in file is", len(list_1))

no_of_lines('py_lab3_txt_q9.txt')