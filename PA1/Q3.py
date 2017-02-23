import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class UCB():
	def __init__(self):
		self.ucb()

	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return gaussian

	def ucb(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(np.random.normal(means[i],1,10000))
		self.trials()
	def trials(self):
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1000)]
		c=2
		for outer in range(2000):
			Q=[0 for i in range(10)]
			Qt=[100 for i in range(10)]
			count=[0 for i in range(10)]
			count=np.array(count)
			t=0
			for inner in range(1000):
				maxvalueE=Qt.index(max(Qt))
				t=t+1
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1

				Rt=self.arms[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+(Rt-Q[maxvalueE])/count[maxvalueE]
				for z in range(10):
					if count[z]!=0:
						Qt[z]=Q[z]+np.sqrt(np.log(t)/count[z])
					else:
						Qt[z]=100000
				reward[inner]=reward[inner]+Rt
		reward=np.array(reward)
		reward=reward/2000
		plt.plot(reward,'r')	
		plt.show()

if __name__=='__main__':
	obj=UCB()