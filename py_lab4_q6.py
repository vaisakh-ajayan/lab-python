def sum_of_list(list_para):
	print(list_para)
	list_sum = 0
	for i in range(len(list_para)):
		list_sum += list_para[i]
	return list_sum

def get_list():
	list_1 = list()
	length = int(input("enter the length of list:"))
	print("enter numbers")
	for i in range(length):
		list_1.append(int(input()))
	return list_1

input_list = get_list()
print("sum of list is", sum_of_list(input_list))
