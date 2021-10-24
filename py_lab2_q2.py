string = input("enter the string:")
string = string.replace(" ","")
freq = [None] * len(string)
for i in range(len(string)):
	count = 1
	for j in range(i+1, len(string)):
		if string[i] == string[j]:
			count += 1
			freq[j]=-1
	if freq[i] != -1:
		freq[i] = count
print("character frequency is")
print("char  frequency")
for i in range(len(string)):
	if freq[i] != -1:
		print(string[i],"	",freq[i])
