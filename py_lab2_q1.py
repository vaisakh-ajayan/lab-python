import random
array = ['a','e','i','o','u']
possible = [['a','e','i','o','u']]

q = 1
print("possible combination of 'a','e','i','o','u'")
print(array)
while q <120:
	random.shuffle(array)
	for x in possible:
		if array not in possible:
			possible.append(list(array))
			print(array)
			q += 1
