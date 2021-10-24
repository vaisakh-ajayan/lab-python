import random
a = random.randint(1, 9)
one = ['too high','exactly right']
nine = ['too low','exactly right']
other =['too low','exactly right','too high']
print("guess a value between 1 and 9")
print("value is",a)
if a == 1:
	print("you guessed", random.choice(one))
elif a== 9:
	print("you guessed", random.choice(nine))
else:
	print("you guessed", random.choice(other))