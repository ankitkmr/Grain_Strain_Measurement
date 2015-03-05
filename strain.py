




def strain(init_coordinates, final_coordinates, init_index):

	x,y = zip(*init_coordinates)

	j = 1
	while (y[j] != y[0]):
		j += 1

	i = 0

	init_vector = []
	final_vector = []
	init_group = []
	final_group = []
	strain_grain = []
	strain_group = []
	final_group = []

	while (j <= len (init_coordinates)):
		init_vector = []
		final_vector = []

		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i][0], init_coordinates[j+1][1] - init_coordinates[i][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i][0], init_coordinates[j+2][1] - init_coordinates[i][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i][0], init_coordinates[j+1][1] - init_coordinates[i+1][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i][0], init_coordinates[j+2][1] - init_coordinates[i+1][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i][0], init_coordinates[j+1][1] - init_coordinates[i+2][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i][0], init_coordinates[j+2][1] - init_coordinates[i+2][1])]
		
		init_vector = init_vector + [(init_coordinates[j+1][0] - init_coordinates[i][0], init_coordinates[j+1][1] - init_coordinates[i+3][1])]
		init_vector = init_vector + [(init_coordinates[j+2][0] - init_coordinates[i][0], init_coordinates[j+2][1] - init_coordinates[i+3][1])]
		

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
		
		init_group = init_group + [init_vector]
		final_group = final_group + [final_vector]
				
'''



'''
	

		for l in range(14):
			for m in range(l+1,15):
				strain_grain = []

				a = np.array([(init_vector[l][0],init_vector[l][1]), (init_vector[m][0],init_vector[m][1])])
				b = np.array([final_vector[l][0],final_vector[m][0]])

				try:
					strain_grain[0],strain_grain[1] = np.linalg.solve(a, b)

					b = np.array([final_vector[l][1],final_vector[m][1]])
					strain_grain[2],strain_grain[3] =np.linalg.solve(a, b)
				except LinAlgError:
					strain_grain = [0,0,0,0]

				strain_group = strain_group + [strain_grain]

	sum_1 = []
	sum_2 = []
	sum_3 = []
	sum_4 = []
	
	for item in strain_group:
		sum_1 = sum_1 + item[0]
		sum_2 = sum_2 + item[1]
		sum_3 = sum_3 + item[2]
		sum_4 = sum_4 + item[3]

	final_strain = [sum_1/float(len(strain_group)),sum_2/float(len(strain_group)),sum_3/float(len(strain_group)),sum_4/float(len(strain_group))]
	final_group = final_group + [final_strain]


return final_group
























		