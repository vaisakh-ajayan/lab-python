with open('py_lab3_txt_q5.txt', 'r') as f1:
	final_list = list()
	list_1 = f1.readlines()
	for line in list_1:
		final_list.append(line.strip('\n'))
	print(final_list)

