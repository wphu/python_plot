import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

data_file = open('01.40625-p.txt')
variable_name = data_file.readline()

data_all = np.loadtxt(data_file)
print(data_all.shape)
data_file.close()


data_file = open('01.40625-p.txt')
variable_name = data_file.readline()

list_segment_n_r = []
n_r = 0

while True:
    line = data_file.readline()
    if not line:
        break

    if line == '\n':
        list_segment_n_r.append(n_r)
        if n_r == 0:
            pass #print("dsfafsdfafs")
        n_r = 0
    else:    
        n_r = n_r + 1
    
print(len(list_segment_n_r))
data_file.close()


list_part_n_r = []
list_part_lines = []

n_r_pre = list_segment_n_r[0]
n_r_now = 0
lines = 0
for i in np.arange(1, len(list_segment_n_r), 1):
    n_r_now = list_segment_n_r[i]
    if n_r_now == 0:
        pass #print("00000000")
    if n_r_now == n_r_pre:
        lines = lines + n_r_pre
    else:
        list_part_n_r.append(n_r_pre)
        list_part_lines.append(lines)
        n_r_pre = n_r_now
        lines = n_r_pre
list_part_n_r.append(n_r_pre)
list_part_lines.append(lines)
print(list_part_n_r, list_part_lines)




fig=plt.figure(figsize=(10,8))
ax0 = fig.add_subplot(1,1,1)


n_r0 = 15
n_z0 = 166

r0 = data_all[0:n_r0*n_z0, 0]
z0 = data_all[0:n_r0*n_z0:, 1]
data0 = data_all[0:n_r0*n_z0:, 6]

r0 = np.reshape(r0, (n_r0, n_z0))
z0 = np.reshape(z0, (n_r0, n_z0))
data0 = np.reshape(data0, (n_r0, n_z0))

ax0.contourf(r0,z0,data0,antialiased=True, levels = 20)




r0 = data_all[0 + n_r0*n_z0:n_r0*n_z0 + n_r0*n_z0, 0]
z0 = data_all[0 + n_r0*n_z0:n_r0*n_z0 + n_r0*n_z0, 1]
data0 = data_all[0 + n_r0*n_z0:n_r0*n_z0 + n_r0*n_z0, 6]

r0 = np.reshape(r0, (n_r0, n_z0))
z0 = np.reshape(z0, (n_r0, n_z0))
data0 = np.reshape(data0, (n_r0, n_z0))

ax0.contourf(r0,z0,data0,antialiased=True, levels = 20)
ax0.set_aspect('equal', adjustable='box')
#plt.colorbar()
ax0.set_xlim(110.0, 250.0)
ax0.set_ylim(-150.0, 120.0)

plt.show()

figure_file_name = "fig.png"
fig.savefig(figure_file_name, dpi = 300)
