import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats

# declare number of particles used for object track estimation
particles = 500

# declare arrays
likelihood = np.empty(particles)      # calculate likelihood of estimate provided by the particle position
estimatedx = np.empty(observations)   # stores estimated x coordinate of the particle
estimatedy = np.empty(observations)   # stores estimated y coordinate of the particle
estimatedz = np.empty(observations)   # stores estimated z coordinate of the particle

# initial particle position
particle_estimate = np.random.uniform(-0.5,1,(particles,3))

i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles,3))                # perturb previous particle position for fresh estimate
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-2*((m1[i]-mx*math.exp(xscale*particle_estimate[j,0]+yscale*particle_estimate[j,1]+particle_estimate[j,2]))**2))*math.exp(-2*((m2[i]-my*math.exp(xscale*particle_estimate[j,0]+particle_estimate[j,1]+zscale*particle_estimate[j,2]))**2))*math.exp(-2*((m3[i]-mz*math.exp(particle_estimate[j,0]+yscale*particle_estimate[j,1]+zscale*particle_estimate[j,2]))**2))    # calculate likelihood based on estimated particle position and observation
    j = j+1
  likelihood = likelihood/np.sum(likelihood)                                                        # normalize likelihood
  custmx = stats.rv_discrete(name='custmx', values=(particle_estimate[:,0]*10000000, likelihood))   # generate distribution from likelihood (x coordinate)
  particle_estimate[:,0] = custmx.rvs(size=particles)/10000000                                      # resample particles using generated likelihood (x coordinate)
  custmy = stats.rv_discrete(name='custmy', values=(particle_estimate[:,1]*10000000, likelihood))   # generate distribution from likelihood (y coordinate)
  particle_estimate[:,1] = custmy.rvs(size=particles)/10000000                                      # resample particles using generated likelihood (y coordinate)
  custmz = stats.rv_discrete(name='custmz', values=(particle_estimate[:,2]*10000000, likelihood))   # generate distribution from likelihood (z coordinate)
  particle_estimate[:,2] = custmz.rvs(size=particles)/10000000                                      # resample particles using generated likelihood (z coordinate)
  estimatedx[i] = np.mean(particle_estimate[:,0])                                                   # estimate particle x coordinate
  estimatedy[i] = np.mean(particle_estimate[:,1])                                                   # estimate particle y coordinate
  estimatedz[i] = np.mean(particle_estimate[:,2])                                                   # estimate particle z coordinate
  i= i+1

# plotting
plt.plot(x)                            # original x coordinate wrt t
plt.plot(estimatedx)                   # estimated x coordinate wrt t
plt.show()
plt.plot(y)                            # original y coordinate wrt t
plt.plot(estimatedy)                   # estimated y coordinate wrt t
plt.show()
plt.plot(z)                            # original z coordinate wrt t
plt.plot(estimatedz)                   # estimated z coordinate wrt t
plt.show()
plt.plot(x,y)                          # actual path of the particle in xy plane
plt.plot(estimatedx,estimatedy)        # estimated path of the particle in xy plane 
plt.show()
plt.plot(x,z)                          # actual path of the particle in xz plane
plt.plot(estimatedx,estimatedz)        # estimated path of the particle in xz plane
plt.show()
plt.plot(y,z)                          # actual path of the particle in yz plane
plt.plot(estimatedy,estimatedz)        # estimated path of the particle in yz plane
plt.show()

# show the path of the particle in 3D
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x, y, z, 'blue')                             # actual path
ax.plot3D(estimatedx, estimatedy, estimatedz, 'red')   # estimated path
plt.show()
