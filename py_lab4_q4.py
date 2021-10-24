import datetime

def week_number(date_obj):
	print("The date is", date_obj)
	print("week number:", date_obj.strftime("%w"))

x = datetime.datetime(2016,6,16)
week_number(x)