import random

def random_line(file_1):
	with open(file_1, 'r') as f1:
		print(random.choice(f1.readlines()))

random_line('py_lab3_txt_q15.txt')
