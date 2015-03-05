
import numpy as np
import matplotlib.pyplot as plt
from random import random
import scipy.interpolate
import matplotlib as m




def strain(init_coordinates, final_coordinates, init_index):

	x,y = zip(*init_coordinates)

	j = 1
	while (y[j] != y[0]):
		j += 1

	i = 0

	init_group = []
	final_group = []
	
	strain_group = []
	final_group = []
	final_avg_group_strain = []
	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0
	init_vector_group = []
	flag = 1
	while (j < len (init_coordinates)):
		strain_grain = []
		init_vector = []
		final_vector = []

		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i][0], init_coordinates[j+1][1] - init_coordinates[i][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i][0], init_coordinates[j+2][1] - init_coordinates[i][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i+1][0], init_coordinates[j+1][1] - init_coordinates[i+1][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i+1][0], init_coordinates[j+2][1] - init_coordinates[i+1][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i+2][0], init_coordinates[j+1][1] - init_coordinates[i+2][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i+2][0], init_coordinates[j+2][1] - init_coordinates[i+2][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i+3][0], init_coordinates[j+1][1] - init_coordinates[i+3][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i+3][0], init_coordinates[j+2][1] - init_coordinates[i+3][1])]
		

		init_vector = init_vector + [(init_coordinates[i+1][0] - init_coordinates[i][0], init_coordinates[i+1][1] - init_coordinates[i][1])]
		init_vector = init_vector + [(init_coordinates[i+2][0] - init_coordinates[i][0], init_coordinates[i+2][1] - init_coordinates[i][1])]
		init_vector = init_vector + [(init_coordinates[i+3][0] - init_coordinates[i][0], init_coordinates[i+3][1] - init_coordinates[i][1])]

		init_vector = init_vector + [(init_coordinates[i+2][0] - init_coordinates[i+1][0], init_coordinates[i+2][1] - init_coordinates[i+1][1])]
		init_vector = init_vector + [(init_coordinates[i+3][0] - init_coordinates[i+1][0], init_coordinates[i+3][1] - init_coordinates[i+1][1])]

		init_vector = init_vector + [(init_coordinates[i+3][0] - init_coordinates[i+2][0], init_coordinates[i+3][1] - init_coordinates[i+2][1])]

		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[j+1][0], init_coordinates[j+2][1] - init_coordinates[j+1][1])]
		
		final_vector = final_vector + [(final_coordinates[j+1][0] - final_coordinates[i][0], final_coordinates[j+1][1] - final_coordinates[i][1])]
		final_vector = final_vector + [(final_coordinates[j+2][0] - final_coordinates[i][0], final_coordinates[j+2][1] - final_coordinates[i][1])]
		
		final_vector = final_vector + [(final_coordinates[j+1][0] - final_coordinates[i][0], final_coordinates[j+1][1] - final_coordinates[i+1][1])]
		final_vector = final_vector + [(final_coordinates[j+2][0] - final_coordinates[i][0], final_coordinates[j+2][1] - final_coordinates[i+1][1])]
		
		final_vector = final_vector + [(final_coordinates[j+1][0] - final_coordinates[i][0], final_coordinates[j+1][1] - final_coordinates[i+2][1])]
		final_vector = final_vector + [(final_coordinates[j+2][0] - final_coordinates[i][0], final_coordinates[j+2][1] - final_coordinates[i+2][1])]
		
		final_vector = final_vector + [(final_coordinates[j+1][0] - final_coordinates[i][0], final_coordinates[j+1][1] - final_coordinates[i+3][1])]
		final_vector = final_vector + [(final_coordinates[j+2][0] - final_coordinates[i][0], final_coordinates[j+2][1] - final_coordinates[i+3][1])]
		

		final_vector = final_vector + [(final_coordinates[i+1][0] - final_coordinates[i][0], final_coordinates[i+1][1] - final_coordinates[i][1])]
		final_vector = final_vector + [(final_coordinates[i+2][0] - final_coordinates[i][0], final_coordinates[i+2][1] - final_coordinates[i][1])]
		final_vector = final_vector + [(final_coordinates[i+3][0] - final_coordinates[i][0], final_coordinates[i+3][1] - final_coordinates[i][1])]

		final_vector = final_vector + [(final_coordinates[i+2][0] - final_coordinates[i+1][0], final_coordinates[i+2][1] - final_coordinates[i+1][1])]
		final_vector = final_vector + [(final_coordinates[i+3][0] - final_coordinates[i+1][0], final_coordinates[i+3][1] - final_coordinates[i+1][1])]

		final_vector = final_vector + [(final_coordinates[i+3][0] - final_coordinates[i+2][0], final_coordinates[i+3][1] - final_coordinates[i+2][1])]

		final_vector = final_vector + [(final_coordinates[j+2][0] - final_coordinates[j+1][0], final_coordinates[j+2][1] - final_coordinates[j+1][1])]
		
		# init_vector_group = init_vector_group + [init_vector]

		# for item in init_vector_group:
		# print final_vector
		# print '\n\n'
		# final_group = final_group + [final_vector]
		# print final_vector,'\n'		
	
		sum_1 = 0
		sum_2 = 0
		sum_3 = 0
		sum_4 = 0
		strain_group = []

		
		for l in range(14):
			for m in range(l+1,15):
				

				a = np.array([(init_vector[l][0],init_vector[l][1]), (init_vector[m][0],init_vector[m][1])])
				b = np.array([final_vector[l][0],final_vector[m][0]])

				try:
					a1 = np.linalg.solve(a, b).tolist()

					b = np.array([final_vector[l][1],final_vector[m][1]])
					a2 =np.linalg.solve(a, b).tolist()
					strain_grain = a1 + a2
					
					# if flag == 1:
					# 	print a1,'\n'
						
				except:
					strain_grain = [0,0,0,0]
				# print a2, '\n'
				# print strain_grain
				strain_group = strain_group + [strain_grain]

		# for item in strain_group:
		# 	print item

		# print len(strain_group)
		# flag = 2
		for item in strain_group:
			if (item[0] > 3 or item[0] < -3) or (item[1] > 3 or item[1] < -3) or (item[2] > 3 or item[2] < -3) or (item[3] > 3 or item[3] < -3):
				item = [0,0,0,0]

			sum_1 = sum_1 + item[0]
			sum_2 = sum_2 + item[1]
			sum_3 = sum_3 + item[2]
			sum_4 = sum_4 + item[3]

		final_avg_strain = (sum_1/float(len(strain_group)),sum_2/float(len(strain_group)),sum_3/float(len(strain_group)),sum_4/float(len(strain_group)))
		# print final_strain, '\n'

		final_avg_group_strain = final_avg_group_strain + [final_avg_strain]

		i += 4
		j += 4
		
	# # print a1, '\n'
	# for item in final_avg_group_strain:
	# 	print item
	return final_avg_group_strain





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
	# print point
	init = init + [point]
	i = 0
	flag = 1

text_file.close()

#print coordinates



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


# print type(init[0])

# print type(final[0])
# print final


#print coordinates                                                     

init_coordinates, init_index = zip(*init)
final_coordinates, final_index = zip(*final)

# print init_coordinates

plot1 = plt.subplot(211)
plt.axis('equal')
plt.scatter(*zip(*init_coordinates))


plot2 = plt.subplot(212)
plt.axis('equal')
plt.scatter(*zip(*final_coordinates))


plot1.set_title('Initial EBSD Mapping')
plot2.set_title('Final EBSD Mapping')


#print final 




final_strain_group = strain(init_coordinates, final_coordinates, init_index)



'''



init_coordinates ,   final_coordinates,   init_index


'''


x1,y1 = zip(*final_coordinates)
z11, z12, z21, z22 = zip(*final_strain_group) 

# print len(z11), len(z22), len(z21), len(z12)
#print len(y1)
# print z11 
#print 'z1',z1
#print len(z1), len(x1)


x = np.array(x1)
y = np.array(y1)

# print final_strain_group
# print z11
# print z12
# print z22
# print z21

sum_11 = 0
sum_21 = 0
sum_12 = 0
sum_22 = 0

for i in range(len(z11)):
	sum_11 = sum_11 + z11[i]
	sum_21 = sum_21 + z21[i]
	sum_12 = sum_12 + z12[i]
	sum_22 = sum_22 + z22[i]

avg_strain_tensor = [float(sum_11)/len(z11),float(sum_12)/len(z11),float(sum_21)/len(z11),float(sum_22)/len(z11)]

txt   = 'epsilon_xx =' + str(round(avg_strain_tensor[0],3))
txt_1 = 'epsilon_xy =' + str(round(avg_strain_tensor[1],3))
txt_2 = 'epsilon_yy =' + str(round(avg_strain_tensor[3],3))
txt_3 = 'epsilon_yx =' + str(round(avg_strain_tensor[2],3))



plt.figtext(0.72, 0.29, txt)
plt.figtext(0.72, 0.25, txt_1)
plt.figtext(0.72, 0.21, txt_2)
plt.figtext(0.72, 0.17, txt_3)

plt.show()


# print avg_strain_tensor[0], avg_strain_tensor[1], avg_strain_tensor[2], avg_strain_tensor[3]
plot3 = plt.subplot(411)
plt.axis("equal")

zplot11 = np.array(z11)
zplot12 = np.array(z12)
zplot21 = np.array(z21)
zplot22 = np.array(z22)

# print zplot22, zplot11, zplot21, zplot12

# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')
rbf = scipy.interpolate.Rbf(x, y, zplot11, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=zplot11.min(),vmax=zplot11.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=zplot11)
plt.colorbar()


plot4 = plt.subplot(412)
plt.axis('equal')


# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')

rbf = scipy.interpolate.Rbf(x, y, zplot12, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=zplot12.min(),vmax=zplot12.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=zplot12)
plt.colorbar()

plot5 = plt.subplot(413)
plt.axis("equal")




# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')
rbf = scipy.interpolate.Rbf(x, y, zplot21, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=zplot21.min(),vmax=zplot21.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=zplot21)
plt.colorbar()



plot6 = plt.subplot(414)
plt.axis("equal")




# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')
rbf = scipy.interpolate.Rbf(x, y, zplot22, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=zplot22.min(), vmax=zplot22.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=zplot22)
plt.colorbar()


plt.figtext(0.82, 0.29, txt)
plt.figtext(0.82, 0.25, txt_1)
plt.figtext(0.82, 0.21, txt_2)
plt.figtext(0.82, 0.17, txt_3)

plot3.set_title('strain_xx contour plot')
plot4.set_title('strain_yx contour plot')
plot5.set_title('strain_xy contour plot')
plot6.set_title('strain_yy contour plot')

# plot4 = plt.subplot(414)
# plt.axis('equal')
# plt.scatter(*zip(*final))

# plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
#            extent=[x.min(), x.max(), y.min(), y.max()])
# plt.scatter(x, y, c=z)
# plt.colorbar()

plt.show()











