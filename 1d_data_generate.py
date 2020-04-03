import numpy as np
import math
import random
import matplotlib.pyplot as plt

sigmax = 0.02  # to model random perturbations in the object track
sigmam = 0.02  # to model noise in observations

observations = 500

# declare arrays
x = np.empty(observations)  # x coordinate of the object
m = np.empty(observations)  # observation corresponsind to object position

# path parameters 
ax =1.0
am = 0.4

# initial values
x[0] = 0
m[0] = ax*math.exp(x[0]) + random.gauss(0,sigmam)

i = 1
while i<observations:
  x[i] = ax*x[i-1] + random.gauss(0,sigmax)          # particle moves linearly with perturbations
  m[i] = ax*math.exp(x[i]) + random.gauss(0,sigmam)  # noisy observations are generated wrt each particle position
  i = i+1

# plot x coordinate wrt time
plt.plot(x)
plt.show()

# plot observed values wrt time
plt.plot(m)
plt.show()
