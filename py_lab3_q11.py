import os

def size_of_file(file_name):
	f_size = os.stat(file_name)
	return f_size.st_size
	
print("size of file is", size_of_file('py_lab3_txt_q11.txt'))