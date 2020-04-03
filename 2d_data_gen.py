import numpy as np
import math
import random
import matplotlib.pyplot as plt

# scaling constants
sigmax = 0.02        # to model random perturbations in the xcoordinate of object track 
sigmay = 0.02        # to model random perturbations in the ycoordinate of object track
xscale = 2           # constants for generating observation
yscale = 3           # constants for generating observation
sigmam1 = 0.05       # to model noise in observation1
sigmam2 = 0.04       # to model noise in observation2

observations = 100           # total number of states

# declare arrays
x = np.empty(observations)   # actual x coordinate of the particle
y = np.empty(observations)   # actual y coordinate of the particle
m1 = np.empty(observations)  # stores observation1
m2 = np.empty(observations)  # stores observation2

# constants for generating data
ax =1.0
ay =1.0
am1 = 0.4
am2 = 0.7

# initial conditions
x[0] = 0.0
y[0] = 0.0
m1[0] = am1*math.exp(xscale*x[0]+y[0]) + random.gauss(0,sigmam1)
m2[0] = am2*math.exp(x[0]+yscale*y[0]) + random.gauss(0,sigmam2)

i = 1
while i<observations:
  x[i] = 0.01*i                                                    # generate data (xcoordinate)
  y[i] = ay*(x[i])**2 + random.gauss(0,sigmay)                     # generate data (ycoordinate)
  m1[i] = am1*math.exp(xscale*x[i]+y[i]) + random.gauss(0,sigmam1)  # generate observation1
  m2[i] = am2*math.exp(x[i]+yscale*y[i]) + random.gauss(0,sigmam2)  # generate observation2
  i = i+1

# plotting
plt.plot(x)   # plot actual x coordinate of the particle wrt time
plt.show()
plt.plot(y)   # plot actual y coordinate of the particle wrt time
plt.show()
plt.plot(x,y) # plot x-y coordinate of the particle
plt.show()
