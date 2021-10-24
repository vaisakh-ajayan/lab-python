import datetime

def days_between_dates(date_1, date_2):
	print("number of days between dates is", abs((date_1- date_2).days))

def date_input():
	year = int(input("Enter the year:"))
	month = int(input("Enter the month:"))
	day = int(input("Enter the day:"))
	x = datetime.datetime(year, month, day)
	return x

print("Enter the first date:")
first_date = date_input()
print("Enter second date:")
second_date = date_input()
days_between_dates(first_date, second_date)