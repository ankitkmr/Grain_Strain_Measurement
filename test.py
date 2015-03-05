

text_file = open("ebsd1.rtf","r")
lines = text_file.readlines()

num_lines = len(lines)
text_file.close()



text_file = open("ebsd1.rtf","r")


init = []
i = 0
flag = 1

for num in range(num_lines): 
	line = text_file.next()
	for c in line:
		if c != ' ':
			i += 1
		else:
			if flag == 1:
				end1 = i
				start1 = i+1
				i += 1
			elif flag == 2:
				end2 = i
				start2 = i+1
				i += 1
			elif flag == 3:
				end3 = i
				start3 = i+1
				i += 1
			

			flag += 1
			if flag > 3:
				break
	i=0
	for c in line:
		if c != '\n':
			i += 1
		else:
			end4 = i
	
		 
	num1 = line[:end1]
	num2 = line[start1:end2]
	num3 = line[start2:end3]
	num4 = line[start3:end4]

	
	point = ((float(num1),float(num2)),(int(num3),int(num4)))
	print point
	init = init + [point]
	i = 0
	flag = 1

text_file.close()

#print coordinates

print type(point)

text_file = open("ebsd2.rtf","r")

final = []
i = 0
flag = 1


for num in range(num_lines): 
	line = text_file.next()
	for c in line:
		if c != ' ':
			i += 1
		else:
			if flag == 1:
				end1 = i
				start1 = i+1
				i += 1
			elif flag == 2:
				end2 = i
				start2 = i+1
				i += 1
			elif flag == 3:
				end3 = i
				start3 = i+1
				i += 1
			
			flag += 1
			if flag > 3:
				break
	
	i=0
	for c in line:
		if c != '\n':
			i += 1
		else:
			end4 = i
	
		 
	num1 = line[:end1]
	num2 = line[start1:end2]
	num3 = line[start2:end3]
	num4 = line[start3:end4]
	point = ((float(num1),float(num2)),(int(num3),int(num4)))
	final = final + [point]
	i = 0
	flag = 1

text_file.close()

text_file = open("test1.rtf","w")
text_file.write('\n'.join('%s %s ' % x for x in init))
text_file.close()


