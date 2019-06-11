import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

data_file = open('01.40625-p.txt')
variable_name = data_file.readline()
data_all = np.loadtxt(data_file)

n_row    = data_all.shape[0]
n_column = data_all.shape[1]
print(n_row, n_column) 

n_r = 15
n_z = 300 #int(n_row / n_r)

r = data_all[:, 0]
z = data_all[:, 1]

r_min = r.min()
r_max = r.max()
z_min = z.min()
z_max = z.max()
print(r_min, r_max, z_min, z_max)

ri = np.linspace(r_min, r_max, 200)
zi = np.linspace(z_min, z_max, 200)

R, Z = np.meshgrid(ri, zi)

data = griddata((r, z), data_all[:, 6], (R, Z))


fig=plt.figure(figsize=(10,8))

ax0 = fig.add_subplot(1,1,1)
ax0.contourf(R,Z,data,antialiased=True, levels = 20)
ax0.set_aspect('equal', adjustable='box')
#plt.colorbar()
ax0.set_xlim(110.0, 250.0)
ax0.set_ylim(-150.0, 120.0)

plt.show()

figure_file_name = "fig_griddata.png"
fig.savefig(figure_file_name, dpi = 100)
