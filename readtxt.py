


text_file = open("ebsd2.txt","r")
lines = text_file.readlines()

num_lines = len(lines) - 6
text_file.close()



text_file = open("ebsd2.txt","r")

text_file.next()
text_file.next()
text_file.next()
text_file.next()
text_file.next()
text_file.next()

coordinates = []
i = 0
flag = 1

for num in range(num_lines): 
	line = text_file.next()
	for c in line:
		if c != ' ':
			i += 1
		else:
			if flag == 1:
				end1 = i-1
				start = i+1
			elif flag == 2:
				end2 = i-1

			flag += 1
			if flag > 2:
				break
	
		 
	num1 = line[:end1]
	num2 = line[start:end2]
	point = (float(num1),float(num2))
	coordinates = coordinates + [point]
	i = 0
	flag = 1

text_file.close()

#print coordinates