with open('py_lab3_txt_q8.txt','r') as f1:
	list1 = f1.readlines()
	strip_list = list()
	split_list = list()
	long_list = list()
	
	high = 0
	for line in list1:
		strip_list.append(line.strip('\n'))
	print(strip_list)
	for line in strip_list:
		split_list = line.split()
		for x in split_list:
			if len(x) >= high:
				high = len(x)
				long_list.append(x)
	print("longest words")
	for y in long_list:
		if len(y) == high:
			print(y)
