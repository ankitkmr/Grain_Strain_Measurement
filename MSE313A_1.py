
import numpy as np
import matplotlib.pyplot as plt
from random import random

init = []
final = []


for i in range(1,11):
	for j in range(1,11):
		init = init + [(i,j)]

plot1 = plt.subplot(211)
plt.axis('equal')
plt.scatter(*zip(*init))


for i in range(1,11):
	for j in range(1,11):
		final = final + [(i + random()/5 ,j + random()/5)]

plot2 = plt.subplot(212)
plt.axis('equal')
plt.scatter(*zip(*final))

plot1.set_title('Initial EBSD Mapping')
plot2.set_title('Final EBSD Mapping')

sum_xx = 0
sum_yy = 0

for i in range(100):
	sum_xx = sum_xx - ((init[i])[0] - (final[i])[0])
	sum_yy = sum_yy - ((init[i])[1] - (final[i])[1])

"""
Since the grain side lenght is assumed to be one unit xy displacement is the same as xx displacement 
and yx is the same as yy displacement
"""
disp_xx = sum_xx/100
disp_xy = sum_xx/100
disp_yy = sum_yy/100
disp_yx = sum_yy/100

displacement_tensor = [disp_xx,disp_xy,disp_yy,disp_yx]
displacement_tensor_transpose = [disp_xx,disp_yx,disp_yy,disp_xy]
strain_tensor = []

for i in range(4):
	strain_tensor = strain_tensor + [0.5*(displacement_tensor[i] + displacement_tensor_transpose[i])]

txt = 'epsilon_xx =' + str(round(strain_tensor[0],3))
txt_1 = 'epsilon_xy =' + str(round(strain_tensor[1],3))
txt_2 = 'epsilon_yy =' + str(round(strain_tensor[2],3))
txt_3 = 'epsilon_yx =' + str(round(strain_tensor[3],3))

plt.figtext(0.67, 0.29, txt)
plt.figtext(0.67, 0.25, txt_1)
plt.figtext(0.67, 0.21, txt_2)
plt.figtext(0.67, 0.17, txt_3)

plt.axis('equal')
plt.show()
