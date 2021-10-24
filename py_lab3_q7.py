array = []
with open('py_lab3_txt_q7.txt', 'r') as f1:
	for line in f1:
		array.append(line.strip('\n'))
	print(array)