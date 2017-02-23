import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class Bandit():
	def __init__(self):
		self.bandit()

	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return list(gaussian)
	def bandit(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(self.gaussian(means[i]))
		self.trials()
	def trials(self):
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1000)]
		for outer in range(2000):
			Q=[0 for i in range(10)]
			count=[0 for i in range(10)]
			for inner in range(1000):
				maxvalue=Q.index(max(Q))
				maxvalueE=epsilon_greedy(maxvalue)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1
				Return=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Return-Q[maxvalueE])/count[maxvalueE]
				reward[inner]=reward[inner]+Return
		reward=[i/2000 for i in reward]
		print reward
		plt.plot(reward,'r')	
		plt.show()


def epsilon_greedy(maxvalue):
	if random.random()<=0.1:
		maxvalueE=randint(0,9)
	else:
		maxvalueE=maxvalue
	return maxvalueE



if __name__=='__main__':
	obj=Bandit()




