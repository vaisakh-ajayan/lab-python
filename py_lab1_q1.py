import datetime
name = input("enter your name:")
old = int(input("enter your age:"))
today = datetime.datetime.now()
x = today.year
ag = x + (100-old)
if old > 0:
	print("Hai",name,"you will turn 100 years old on",ag)
else:
	print("invaid age")