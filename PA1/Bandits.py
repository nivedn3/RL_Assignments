import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class Bandits():
	def __init__(self):
		self.gaussian_rewards()

# Function which returns the gaussian reward distribution 
	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return list(gaussian)

# Initialising the gaussian reward distributions with given mean values and calls the iterator

	def gaussian_rewards(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(self.gaussian(means[i]))
		# Epsilon values
		epsilon=[0.1,0]
		optimal=[]
		for count,i in enumerate(epsilon):
			optimal.append(self.trials(i,count))	

		# Plotting Section	
		plt.ylabel('Average Reward')
		plt.legend(loc='upper right')
		plt.xlabel('Steps')
		plt.title('Epsilon Greedy')	
		plt.show()

		label="epsilon="+str(epsilon[0])
		plt.plot(optimal[0],'r',label=str(label))
		label="epsilon="+str(epsilon[1])
		plt.plot(optimal[1],'g',label=str(label))
		plt.ylabel('Optimal Action %')
		plt.legend(loc='upper right')
		plt.xlabel('Steps')
		plt.title('Epsilon Greedy')	
		plt.show()

	def trials(self,eps,counts):
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1000)]
		optimal_action=[0 for i in range(1000)]
		for outer in range(2000):
			Q=[0 for i in range(10)]
			count=[0 for i in range(10)]
			for inner in range(1000):
				maxvalue=Q.index(max(Q))
				maxvalueE=epsilon_greedy(maxvalue,eps)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1
				Return=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Return-Q[maxvalueE])/count[maxvalueE]
				reward[inner]=reward[inner]+Return
				if maxvalueE == 2:
					optimal_action[inner]=optimal_action[inner]+1
		reward=[i/2000 for i in reward]
		color=['r','g']
		label="epsilon="+str(eps)
		plt.plot(reward,color[counts],label=str(label))
		optimal_action=np.array(optimal_action)
		optimal_percent=optimal_action/20
		return optimal_percent

# Returns the arm to be pulled after considering the epsilon probability for exploration

def epsilon_greedy(maxvalue,epsilon):
	if random.random()<=epsilon:
		maxvalueE=randint(0,9)
	else:
		maxvalueE=maxvalue
	return maxvalueE

if __name__=='__main__':
	obj=Bandits()




