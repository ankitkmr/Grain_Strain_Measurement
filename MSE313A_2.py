
import numpy as np
import matplotlib.pyplot as plt
from random import random

init = []
final = []

a = float(raw_input("Enter the grain parameter for hexagonal grains\n"))

for i in range(7):
	for j in range(4):
		init = init + [(a + a*(3**0.5)*i, a + 3*j*a)]
		init = init + [(a - (3**0.5)*a/2 + a*(3**0.5)*i, a + a/2 + 3*j*a)]
		init = init + [(a - (3**0.5)*a/2 + a*(3**0.5)*i, a + 3*a/2 + 3*j*a)]
		init = init + [(a + a*(3**0.5)*i, a + 2*a + 3*j*a)]
		
# print type(init[0])
# print init[0]

plot1 = plt.subplot(211)
plt.axis('equal')
plt.scatter(*zip(*init))



for i in init:
	final = final + [(i[0] + random()/2 ,i[1] + random()/2)]

# print type(final[0])
# print final[0]

plot2 = plt.subplot(212)
plt.axis('equal')
plt.scatter(*zip(*final))


plot1.set_title('Initial EBSD Mapping')
plot2.set_title('Final EBSD Mapping')

sum_xx = 0
sum_yy = 0

for i in range(len(init)):
	sum_xx = sum_xx - ((init[i])[0] - (final[i])[0])
	sum_yy = sum_yy - ((init[i])[1] - (final[i])[1])

"""
Since the grain side lenght is assumed to be one unit xy displacement is the same as xx displacement 
and yx is the same as yy displacement
"""
disp_xx = sum_xx/(a*len(init))
#disp_xy = sum_xx/(a*len(init))
disp_yy = sum_yy/(a+len(init))
#disp_yx = sum_yy/(a+len(init))

displacement_tensor = [disp_xx,0,disp_yy,0]
displacement_tensor_transpose = [disp_xx,0,disp_yy,0]
strain_tensor = []

for i in range(4):
	strain_tensor = strain_tensor + [0.5*(displacement_tensor[i] + displacement_tensor_transpose[i])]

txt = 'epsilon_xx =' + str(round(strain_tensor[0],3))
#txt_1 = 'epsilon_xy =' + str(round(strain_tensor[1],3))
txt_2 = 'epsilon_yy =' + str(round(strain_tensor[2],3))
#txt_3 = 'epsilon_yx =' + str(round(strain_tensor[3],3))


plt.figtext(0.67, 0.29, txt)
#plt.figtext(0.67, 0.25, txt_1)
plt.figtext(0.67, 0.21, txt_2)
#plt.figtext(0.67, 0.17, txt_3)

plt.show()


