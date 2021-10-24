import os

def path_of_file():
	x = input("Enter the path in which files contain: ")
	return x

def sorting_files(location):
	for root,dirs,files in os.walk(location):
		print("sorted file names are:\n")
		for x in sorted(files):
			print(x)

location = path_of_file()
sorting_files(location)
#/home/vaisakh/Desktop/mashupstack/python/lab5/exp1
