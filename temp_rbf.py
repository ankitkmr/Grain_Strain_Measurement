

from matplotlib.backends.backend_pdf import PdfPages

plot1 = plotGraph(tempDLstats, tempDLlabels)
plot2 = plotGraph(tempDLstats_1, tempDLlabels_1)
plot3 = plotGraph(tempDLstats_2, tempDLlabels_2)
plot4 = plotGraph(tempDLstats_2, tempDLlabels_2)

pp = PdfPages('foo.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.close()























# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.interpolate

# # Generate data:
# x, y, z = 10 * np.random.random((3,10))

# # Set up a regular grid of interpolation points
# xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
# xi, yi = np.meshgrid(xi, yi)

# # Interpolate
# rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
# zi = rbf(xi, yi)

# plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
#            extent=[x.min(), x.max(), y.min(), y.max()])
# plt.scatter(x, y, c=z)
# plt.colorbar()
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.interpolate

# # Generate data: for N=1e6, the triangulation hogs 1 GB of memory
# N = 1000000
# x, y = 10 * np.random.random((2, N))
# rho = np.sin(3*x) + np.cos(7*y)**3

# # Set up a regular grid of interpolation points
# xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
# xi, yi = np.meshgrid(xi, yi)

# # Interpolate; there's also method='cubic' for 2-D data such as here
# zi = scipy.interpolate.griddata((x, y), rho, (xi, yi), method='linear')

# plt.imshow(zi, vmin=rho.min(), vmax=rho.max(), origin='lower',
#            extent=[x.min(), x.max(), y.min(), y.max()])
# plt.colorbar()
# plt.show()