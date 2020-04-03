import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# scaling constants
sigmax = 0.02      # to model random perturbations in the xcoordinate of object track 
sigmay = 0.02      # to model random perturbations in the ycoordinate of object track 
sigmaz = 0.02      # to model random perturbations in the zcoordinate of object track 
xscale = 2         # constants for generating observation
yscale = 3         # constants for generating observation
zscale = 4         # constants for generating observation
sigmam1 = 0.03     # to model noise in observation1
sigmam2 = 0.04     # to model noise in observation2
sigmam3 = 0.02     # to model noise in observation3

observations = 100           # total number of states

# declare arrays
x = np.empty(observations)    # actual x coordinate of the particle
y = np.empty(observations)    # actual y coordinate of the particle
z = np.empty(observations)    # actual z coordinate of the particle
m1 = np.empty(observations)   # stores observation1
m2 = np.empty(observations)   # stores observation2
m3 = np.empty(observations)   # stores observation3

# constants for generating data
ax =1.0
ay =0.5
az =0.7
mx =1.2
my =1.1
mz =1.4

# initial conditions
x[0] = 0.0
y[0] = 0.0
z[0] = 0.0
m1[0] = mx*math.exp(xscale*x[0]+yscale*y[0]+z[0]) + random.gauss(0,sigmam1)
m2[0] = my*math.exp(xscale*x[0]+y[0]+zscale*z[0]) + random.gauss(0,sigmam2)
m3[0] = mz*math.exp(x[0]+yscale*y[0]+zscale*z[0]) + random.gauss(0,sigmam3)

i = 1
while i<observations:
  x[i] = 0.01*i                                                                  # generate data (xcoordinate)
  y[i] = ay*(x[i]**2) + random.gauss(0,sigmay)                                   # generate data (ycoordinate) 
  z[i] = az*z[i-1] + random.gauss(0,sigmaz)                                      # generate data (zcoordinate)
  m1[i] = mx*math.exp(xscale*x[i]+yscale*y[i]+z[i]) + random.gauss(0,sigmam1)    # generate observation1
  m2[i] = my*math.exp(xscale*x[i]+y[i]+zscale*z[i]) + random.gauss(0,sigmam2)    # generate observation2
  m3[i] = mz*math.exp(x[i]+yscale*y[i]+zscale*z[i]) + random.gauss(0,sigmam3)    # generate observation3
  i = i+1

# plotting
plt.plot(x)     # plot actual x coordinate of the particle wrt time
plt.show()
plt.plot(y)     # plot actual y coordinate of the particle wrt time
plt.show()
plt.plot(z)     # plot actual z coordinate of the particle wrt time
plt.show()
plt.plot(x,y)   # plot actual path in x-y
plt.show()
plt.plot(y,z)   # plot actual path in y-z
plt.show()
plt.plot(x,z)   # plot actual path in x-z
plt.show()

# show the actual path of the particle in 3D
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x, y, z, 'blue')
plt.show()
