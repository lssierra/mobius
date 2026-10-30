import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#############################################################################################
##INIT


#STRIPE coords
u = np.linspace(0,2*np.pi,1000) #angle
v = np.linspace(-1,1,100) # disr=tance from cenral line on stripe
print("u ",u.size,u.shape)
print("v ",v.size,v.shape)


###################################################################################################
##mobius stripe

#COORDONATES

x = np.empty((u.size,v.size))
y = np.empty((u.size,v.size))
z = np.empty((u.size,v.size))
R = 3
print("x ",x.size,x.shape)

for i in range(v.size):
    for j in range(u.size):
        x[j,i] = (R + v[i]*np.cos(u[j]/2))*np.cos(u[j])
        y[j,i] = (R + v[i]*np.cos(u[j]/2))*np.sin(u[j]) 
        z[j,i] = v[i]*np.sin(u[j]/2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='twilight')#, edgecolor='green')
ax.set_title('Surface Plot')
plt.show()