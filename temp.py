
import numpy as np
import matplotlib.pyplot as plt
from random import random
import scipy.interpolate

init = []
final = []

a = float(raw_input("Enter the grain parameter for hexagonal grains\n"))

for i in range(7):
	for j in range(4):
		init = init + [(a + a*(3**0.5)*i, a + 3*j*a)]
		init = init + [(a - (3**0.5)*a/2 + a*(3**0.5)*i, a + a/2 + 3*j*a)]
		init = init + [(a - (3**0.5)*a/2 + a*(3**0.5)*i, a + 3*a/2 + 3*j*a)]
		init = init + [(a + a*(3**0.5)*i, a + 2*a + 3*j*a)]
		

plot1 = plt.subplot(211)
plt.axis('equal')
plt.scatter(*zip(*init))



for i in init:
	final = final + [(i[0] + random()/3 ,i[1] + random()/3)]

plot2 = plt.subplot(212)
plt.axis('equal')
plt.scatter(*zip(*final))


plot1.set_title('Initial EBSD Mapping')
plot2.set_title('Final EBSD Mapping')


#print final 

x1,y1 = zip(*final)
z1 = []
z2 = []

for i in range(len(final)):
	z1 = z1 + [((final[i])[0]- (init[i])[0])/a]
	z2 = z2 + [((final[i])[1]- (init[i])[1])/a]

#print len(y1)
#print z1 
#print 'z1',z1
#print len(z1), len(x1)


x = np.array(x1)
y = np.array(y1)
z_x = np.array(z1)
z_y = np.array(z2)

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
disp_xy = sum_xx/(a*len(init))
disp_yy = sum_yy/(a+len(init))
disp_yx = sum_yy/(a+len(init))

displacement_tensor = [disp_xx,disp_xy,disp_yy,disp_yx]
displacement_tensor_transpose = [disp_xx,disp_yx,disp_yy,disp_xy]
strain_tensor = []

for i in range(4):
	strain_tensor = strain_tensor + [0.5*(displacement_tensor[i] + displacement_tensor_transpose[i])]

txt = 'epsilon_xx =' + str(round(strain_tensor[0],3))
txt_1 = 'epsilon_xy =' + str(round(strain_tensor[1],3))
txt_2 = 'epsilon_yy =' + str(round(strain_tensor[2],3))
txt_3 = 'epsilon_yx =' + str(round(strain_tensor[3],3))



plt.figtext(0.72, 0.29, txt)
plt.figtext(0.72, 0.25, txt_1)
plt.figtext(0.72, 0.21, txt_2)
plt.figtext(0.72, 0.17, txt_3)

plt.show()



plot3 = plt.subplot(211)
plt.axis('equal')


# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 200), np.linspace(y.min(), y.max(), 200)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')
rbf = scipy.interpolate.Rbf(x, y, z_x, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=z_x.min(), vmax=z_x.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=z_x)
plt.colorbar()


plot4 = plt.subplot(212)
plt.axis('equal')


# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 200), np.linspace(y.min(), y.max(), 200)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
#zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='linear')
rbf = scipy.interpolate.Rbf(x, y, z_y, function='linear')
zi = rbf(xi, yi)

plt.imshow(zi, vmin=z_y.min(), vmax=z_y.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()])
plt.scatter(x, y, c=z_y)
plt.colorbar()


plt.figtext(0.82, 0.29, txt)
plt.figtext(0.82, 0.25, txt_1)
plt.figtext(0.82, 0.21, txt_2)
plt.figtext(0.82, 0.17, txt_3)

plot3.set_title('strain_xx contour plot')
plot4.set_title('strain_yy contour plot')

# plot4 = plt.subplot(414)
# plt.axis('equal')
# plt.scatter(*zip(*final))

# plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
#            extent=[x.min(), x.max(), y.min(), y.max()])
# plt.scatter(x, y, c=z)
# plt.colorbar()

plt.show()

