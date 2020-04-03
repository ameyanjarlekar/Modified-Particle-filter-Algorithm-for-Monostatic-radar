import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy import stats

# declare number of particles used for object track estimation
particles = 100

# declare arrays
likelihood = np.empty(particles)   # calculate likelihood of estimate provided by the particle position
estimated = np.empty(observations) # stores estimated path of the particle

# initial particle position
particle_estimate = np.random.uniform(-0.5,1,(particles))

# particle filter 
i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles))            # perturb previous particle position for fresh estimate
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-5*((m[i]-ax*math.exp(particle_estimate[j]))**2))                # calculate likelihood based on estimated particle position and observation
    j = j+1
  likelihood = likelihood/np.sum(likelihood)                                                  # normalize likelihood
  custm = stats.rv_discrete(name='custm', values=(particle_estimate*10000000, likelihood))    # generate distribution from likelihood
  particle_estimate = custm.rvs(size=particles)/10000000                                      # resample particles using generated likelihood
  estimated[i] = np.mean(particle_estimate)                                                   # estimate particle location
  i= i+1

# plotting
plt.plot(x)          # original position
plt.plot(estimated)  # estimated position
plt.show()
