import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys

class SF():
	def __init__(self):
		self.softmax()

	def softmax(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(np.random.normal(means[i],1,10000))
		self.trials()

	def pi(self,H):
		Probability=[]
		sum=0
		for j in range(10):
			sum=sum+np.exp(H[j])
		for i in range(10):
			Probability.append(np.exp(H[i])/sum)
		return Probability
	def trials(self):
		reward=[0 for i in range(1000)]
		alpha=2
		for outer in range(20):
			H=[0 for i in range(10)]
			arms=[i for i in range(10)]
			Return_mean=0
			for inner in range(1000):
				Pr=self.pi(H)				
				maxvalueE=choice(arms,p=Pr)
				Return=self.arms[maxvalueE][randint(0,9999)]
				reward[inner]=reward[inner]+Return
				#Return_mean=(Return_mean*(inner)+Return)/(inner+1)
				Return_mean=0
				H[maxvalueE]=H[maxvalueE]-alpha*(Return - Return_mean)*(1-Pr[maxvalueE])
				for i in range(10):
					if i!=maxvalueE:
						H[i]=H[i]-alpha*(Return - Return_mean)*Pr[i]
		reward=np.array(reward)
		reward=reward/20
		plt.plot(reward,'r')	
		plt.show()






if __name__=='__main__':
	obj=SF()