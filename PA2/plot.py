import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

steps3= [5.54, 8.2, 9.26, 7.3, 7.96, 8.4, 8.6, 9.9, 9.36, 9.8, 9.34, 9.96, 9.72, 9.36, 9.3, 9.42, 9.3, 9.84, 9.88, 9.44, 9.86, 9.72, 9.84, 9.72, 9.74, 9.72, 9.6, 9.76, 9.92, 9.76, 9.2, 9.78, 9.02, 9.84, 9.82, 9.76, 9.66, 9.78, 9.82, 9.5]
steps5= [4.54, 8.04, 9.08, 9.38, 9.2, 9.88, 9.8, 9.56, 10.0, 9.74, 9.94, 9.84, 9.44, 9.86, 8.9, 9.9, 9.58, 9.86, 9.48, 9.82, 9.9, 9.54, 9.82, 9.6, 8.84, 9.8, 9.78, 9.2, 8.78, 9.8, 9.54, 9.88, 9.9, 9.18, 9.44, 9.76, 9.4, 9.4, 9.52, 9.88]
steps9=[6.66, 8.48, 8.98, 8.88, 9.14, 8.9, 8.84, 9.66, 9.16, 9.42, 9.68, 9.1, 9.38, 9.66, 9.66, 9.58, 9.56, 9.52, 9.1, 9.76, 9.48, 9.56, 9.62, 9.16, 9.6, 9.68, 9.72, 9.38, 9.18, 9.7, 9.52, 9.58, 9.7, 9.5, 9.48, 9.64, 9.38, 9.14, 9.54, 9.56]
steps99=[7.34, 7.18, 8.32, 8.34, 8.88, 9.4, 9.06, 9.72, 9.48, 9.44, 9.14, 9.56, 8.96, 9.32, 9.48, 9.44, 9.2, 8.9, 9.24, 9.68, 9.26, 9.38, 9.74, 9.5, 9.58, 9.94, 9.78, 9.64, 9.64, 9.84, 9.78, 9.4, 9.3, 9.62, 9.78, 9.76, 9.68, 9.52, 9.56, 9.52]
label="lambda="+str(0.3)
plt.plot(steps3,'r',label=str(label))
label="lambda="+str(0.5)
plt.plot(steps5,'g',label=str(label))
label="lambda="+str(0.99)
plt.plot(steps99,'b',label=str(label))
label="lambda="+str(0.9)
plt.plot(steps9,'c',label=str(label))
plt.ylabel('Steps of 50 episodes')
plt.legend(loc='upper right')
plt.xlabel('Average_Reward')
plt.title('Comparing lambda for goal A')	
plt.show()
