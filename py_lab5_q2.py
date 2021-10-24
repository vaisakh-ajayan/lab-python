import os

def path_of_file():
	x = input("Enter the path in which files contain: ")
	return x

def filenames_to_month(location):
	for root,dirs,files in os.walk(location):
		for x in files:
			month = (x[2:4])
			if month == '01':
				print("jan-", x)
			elif month == '02':
				print("feb-", x)
			elif month == '03':
				print("mar-", x)
			elif month == '04':
				print("apr-", x)
			elif month == '05':
				print("may-", x)
			elif month == '06':
				print("jun-", x)
			elif month == '07':
				print("jul-", x)
			elif month == '08':
				print("aug-", x)
			elif month == '09':
				print("sep-", x)
			elif month == '10':
				print("oct-", x)
			elif month == '11':
				print("nov-", x)
			elif month == '12':
				print("dec-", x)

location = path_of_file()
filenames_to_month(location)
#/home/vaisakh/Desktop/mashupstack/python/lab5/exp2