import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class SF():
	def __init__(self):
		self.reward_gaussians()

	def reward_gaussians(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(np.random.normal(means[i],1,10000))
		self.trials()

	def softmax(self,Q,Temp):
		Probability=[]
		sum=0
		for j in range(10):
			sum=sum+np.exp(Q[j]/Temp)
		for i in range(10):
			Probability.append(np.exp(Q[i]/Temp)/sum)
		return Probability
	def trials(self):
		reward=[0 for i in range(1000)]
		arms=[i for i in range(10)]

		for outer in range(2000):
			Q=[0 for i in range(10)]
			count=[0 for i in range(10)]

			for inner in range(1000):		
				Probability=self.softmax(Q,0.1)
				maxvalueE=choice(arms,p=Probability)
				count[maxvalueE]=count[maxvalueE]+1
				Return=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Return-Q[maxvalueE])/count[maxvalueE]
				reward[inner]=reward[inner]+Return
		reward=np.array(reward)
		reward=reward/2000
		plt.plot(reward,'r')	
		plt.show()






if __name__=='__main__':
	obj=SF()