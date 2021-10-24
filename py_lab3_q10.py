def worder(fil):
	with open(fil,'r') as f1:
		list1 = f1.read().splitlines()		#lines into list without \n
		content = " ".join(list1)	#to string
		content = content.split()	#string to list
		fre = dict()
		for word in content:
			if word not in fre:
				fre[word] = 1
			else :
				fre[word] += 1
		print("frequency and count")
		print(fre)
		
worder('py_lab3_txt_q10.txt')