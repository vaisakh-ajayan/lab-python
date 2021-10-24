tuple_1 = ('a','b','c','d','e','f')
print(tuple_1)
string = input("enter the char want to check:")
try:
	index = tuple_1.index(string)
	print("index of",string,"is",index)
except Exception as e:
	print("input given is not in tuple")
