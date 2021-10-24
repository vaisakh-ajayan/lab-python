import csv

def write_csv(file_name):
	with open(file_name, 'w', newline='') as file:
		wt = csv.writer(file)
		wt.writerow(['id', 'name', 'product', 'price'])
		wt.writerow([1,'hp laptop','laptop','35000'])
		wt.writerow([2,'parle-g','biscut','10'])
		wt.writerow([3,'everyday','battery','15'])
		wt.writerow([4,'quartz','watch','600'])
		wt.writerow([5,'pepsi','soft drink','35'])

def third_row(file_name):
	with open(file_name, 'r') as file1:
		reader = csv.reader(file1)
		row_count = 0
		print("\nthird row")
		for row in reader:
			if row_count == 2:
				print(row)
				break
			row_count += 1	

def second_column(file_name):
	with open(file_name, 'r') as file1:
		reader = csv.reader(file1)
		print("\nsecond column")
		for row in reader:
			print(row[2])

def first_three_rows(file_name):
	with open(file_name, 'r') as file1:
		reader = csv.reader(file1)
		print("\nfirst three rows")
		row_count = 0
		file1.seek(0,0)
		for row in reader:
			if row_count < 3:
				print(row)
			row_count += 1



write_csv('py_lab5_csv_q3.csv')
third_row('py_lab5_csv_q3.csv')
second_column('py_lab5_csv_q3.csv')
first_three_rows('py_lab5_csv_q3.csv')
