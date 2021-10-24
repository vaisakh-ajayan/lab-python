import datetime

def date_details():
	x = datetime.datetime.now()
	print("current date and time", x)
	print("year:", x.year)
	print("month:", x.strftime("%B"))
	print("week number:", x.strftime("%U"))
	print("weekday:", x.strftime("%A"))
	print("day of month", x.strftime("%d"))
	print("day of year", x.strftime("%j"))
	print("day of week", x.strftime("%w"))

date_details()
