import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class Softmax():
	def __init__(self):
		self.reward_gaussians()

# Initialising the gaussian reward distributions with given mean values and calls the iterator

	def reward_gaussians(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(np.random.normal(means[i],1,10000))

#Temperature initialisation

		temp=[0.01,0.1,1]
		for count,i in enumerate(temp):
			self.trials(i,count)

# Plotting Section

		plt.ylabel('Average Reward')
		plt.legend(loc='upper right')
		plt.xlabel('Steps')
		plt.title('Softmax')
		plt.show()

# Softmax Implementation 

	def softmax(self,Q,Temp):
		Probability=[]
		sum=0
		for j in range(10):
			sum=sum+np.exp(Q[j]/Temp)
		for i in range(10):
			Probability.append(np.exp(Q[i]/Temp)/sum)
		return Probability


	def trials(self,T,counts):
		reward=[0 for i in range(1000)]
		arms=[i for i in range(10)]

# Loop for averaging over 2000 Bandit Problems

		for outer in range(2000):
			Q=[0 for i in range(10)]
			count=[0 for i in range(10)]

# Implemetation of 1000 steps

			for inner in range(1000):		
				Probability=self.softmax(Q,T)
				maxvalueE=choice(arms,p=Probability)
				count[maxvalueE]=count[maxvalueE]+1
				Return=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Return-Q[maxvalueE])/count[maxvalueE]
				reward[inner]=reward[inner]+Return
		reward=np.array(reward)

# Taking the average reward from 2000 runs
		
		reward=reward/2000
		color=['r','g','b']
		label="Temp="+str(T)
		plt.plot(reward,color[counts],label=str(label))

		
if __name__=='__main__':
	obj=Softmax()