import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class UCB():
	def __init__(self):
		self.gaussian_rewards()

# Function which returns the gaussian reward distribution 
	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return gaussian

# Initialising the gaussian reward distributions with given mean values and calls the iterator

	def gaussian_rewards(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(np.random.normal(means[i],1,10000))
		self.trials()

# UCB algorithm in steps of 1000 averaged over 2000 trials.

	def trials(self):
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1000)]
		Confidence_bound=2
		for outer in range(2000):
			Q=[0 for i in range(10)]
			Qt=[100 for i in range(10)]
			#initially pulling each arm once
			count=[1 for i in range(10)]
			count=np.array(count)
			t=0
			for k in range(10):
				Q[k]=self.arms[k][randint(0,9999)]
			for inner in range(1,1000):
				maxvalueE=Qt.index(max(Qt))
				t=t+1
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1
				Rt=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Rt-Q[maxvalueE])/count[maxvalueE]
				for z in range(10):
						Qt[z]=Q[z]+Confidence_bound*np.sqrt(np.log(t)/count[z])
				reward[inner]=reward[inner]+Rt
		reward=np.array(reward)
		reward=reward/2000

# Plotting Section

		plt.plot(reward,'r')
		plt.ylabel('Average Reward')
		plt.xlabel('Steps')
		plt.title('UCB with c=2')	
		plt.show()

if __name__=='__main__':
	obj=UCB()