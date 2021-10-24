import datetime

def unix_to_readable():
	x = datetime.datetime.now()
	unix_timestamp = x.timestamp()
	print("timestamp:", unix_timestamp)
	print("readable date:", datetime.datetime.fromtimestamp(unix_timestamp))

unix_to_readable()