import string

import random

def generate(num):
	a1 = random.choice(string.punctuation)
	a2 = random.choice(string.ascii_lowercase)
	a3 = random.choice(string.ascii_uppercase)
	a4 = random.choice(string.digits)
	passw = a1 + a2 + a3 + a4
	for i in range(4, num):
		passw += random.choice(
			string.ascii_lowercase + string.punctuation + string.ascii_uppercase
			+ string.digits)
	passw = list(passw)
	random.shuffle(passw)
	passw = "".join(passw)
	print(passw)

number = int(input("enter the length of password you want(min:6,max:12):"))
if number<6 or number>12 :
	print("enter the valid length")
else:
	generate(number)