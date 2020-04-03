import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy import stats

# declare number of particles used for object track estimation
particles = 100

# declare arrays
likelihood = np.empty(particles)     # calculate likelihood of estimate provided by the particle position
estimatedx = np.empty(observations)  # stores estimated x coordinate of the particle
estimatedy = np.empty(observations)  # stores estimated y coordinate of the particle

# initial particle position
particle_estimate = np.random.uniform(-0.5,1,(particles,2))

# particle filter 
i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles,2))                 # perturb previous particle position for fresh estimate
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-5*((m1[i]-am1*math.exp(xscale*particle_estimate[j,0]+particle_estimate[j,1]))**2))*math.exp(-5*((m2[i]-am2*math.exp(particle_estimate[j,0]+yscale*particle_estimate[j,1]))**2))  # calculate likelihood based on estimated particle position and observation
    j = j+1
  likelihood = likelihood/np.sum(likelihood)                                                         # normalize likelihood
  custmx = stats.rv_discrete(name='custmx', values=(particle_estimate[:,0]*10000000, likelihood))    # generate distribution from likelihood (x coordinate)
  particle_estimate[:,0] = custmx.rvs(size=particles)/10000000                                       # resample particles using generated likelihood (x coordinate)
  custmy = stats.rv_discrete(name='custmy', values=(particle_estimate[:,1]*10000000, likelihood))    # generate distribution from likelihood (y coordinate)
  particle_estimate[:,1] = custmy.rvs(size=particles)/10000000                                       # resample particles using generated likelihood (y coordinate)
  estimatedx[i] = np.mean(particle_estimate[:,0])                                                    # estimate particle x coordinate
  estimatedy[i] = np.mean(particle_estimate[:,1])                                                    # estimate particle y coordinate
  i= i+1

# plotting
plt.plot(x)                        # original x coordinate wrt t
plt.plot(estimatedx)               # estimated x coordinate wrt t
plt.show()
plt.plot(y)                        # original y coordinate wrt t
plt.plot(estimatedy)               # estimated y coordinate wrt t
plt.show()
plt.plot(x,y)                      # original path of the particle
plt.plot(estimatedx,estimatedy)    # estimated path of the particle
plt.show()
