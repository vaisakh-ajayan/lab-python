import datetime

def subtract_five():
	current_date = datetime.datetime.now()
	print("current date:", current_date.date())
	difference_date = datetime.timedelta(5)
	print("5 days subtracted:", (current_date-difference_date).date())

subtract_five()
