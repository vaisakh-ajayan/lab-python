def content_without_newline(file_1):
	with open(file_1, 'r') as f1:
		list1 = f1.readlines()
		print(list1, end='\n\n')
		print("contents without new line characters\n")
		for x in list1:
			print(x.replace('\n', ''))

content_without_newline('py_lab3_txt_q16.txt')
