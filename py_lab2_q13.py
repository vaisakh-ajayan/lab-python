list1=[1,2,3]
print("list:", list1)
sub_list = [[]]
for i in range(len(list1)):
	for j in range(i+1, len(list1)+1):
		sub_list.append(list1[i:j])
print("sublist:", sub_list)
