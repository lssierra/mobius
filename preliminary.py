import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#############################################################################################
##INIT

#GRID coords

x_axe = np.linspace(-10,10,100)
y_axe = np.linspace(-10,10,100)
z_axe = np.linspace(-10,10,100)


#STRIPE coords
u = np.linspace(0,2*np.pi,100) #angle
v = np.linspace(-1,1,100) # disr=tance from cenral line on stripe




###################################################################################################
##mobius stripe

#COORDONATES

x = np.empty_like(x_axe)
y = np.empty_like(y_axe)
z = np.empty_like(z_axe)
R = 3


x = (R + v*np.cos(u/2))*np.cos(u)
y = (R + v*np.cos(u/2))*np.sin(u) 
z = v*np.sin(u/2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
ax.set_title('Surface Plot')
plt.show()