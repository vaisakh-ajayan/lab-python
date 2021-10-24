import os

def last(x):
	with open('py_lab3_txt_q4.txt', 'r') as f1:
		if os.stat("py_lab3_txt_q4.txt").st_size == 0:
			print("File is empty")
			return
		for line in (f1.readlines()[-x:]) :
			print(line)
	

x = int(input("how many last lines do you want to read:"))
try:
	if x <= 0:
		raise Exception;
	else:
		last(x)
except Exception as e:
	print("enter a positive number")
