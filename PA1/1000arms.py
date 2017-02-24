import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys
import multiprocessing 
from multiprocessing import Process
import copy_reg
import types

class UCB():
	def __init__(self):
		self.gaussian_rewards()

# Function which returns the gaussian reward distribution 

	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return gaussian

# Mean of reward distribution has been sampled using the randint function

	def gaussian_rewards(self):
		self.arms=[]
		means=np.random.randint(-50,50,1000)
		for i in range(1000):
			self.arms.append(np.random.normal(means[i],1,10000))
		self.iter()

# 10000 Iterations of the arms 
	def trials(self,reward,result):
#Confidence bound=2
		Confidence_bound=2

		Q=[0 for i in range(1000)]
		Qt=[100 for i in range(1000)]
		count=[1 for i in range(1000)]
		count=np.array(count)
		t=0
		for k in range(1000):
			Q[k]=self.arms[k][randint(0,9999)]
		for inner in range(1,10000):
			maxvalueE=Qt.index(max(Qt))
			t=t+1
			count[maxvalueE]=count[maxvalueE]+1
			Rt=self.arms[maxvalueE][randint(0,9999)]
			Q[maxvalueE]=Q[maxvalueE]+(Rt-Q[maxvalueE])/count[maxvalueE]
			for z in range(1000):
				if count[z]!=0:
					Qt[z]=Q[z]+Confidence_bound*np.sqrt(np.log(t)/count[z])
				else:
					Qt[z]=100000
			reward[inner]=reward[inner]+Rt
		result.put(reward)

# Running the 1000 bandit problem for averaging

	def iter(self):
		armcount=[0 for i in range(1000)]	
		reward=[0 for i in range(10000)]

# Instead of Threading multiprocessing has been used to use the 4 cores effectively

		result=multiprocessing.Queue()
		jobs=[]
		for i in range(1000):
			p=Process(target=self.trials,args=(reward,result))
			jobs.append(p)
			p.start()
		final_reward=np.array([0 for i in range(10000)])
		for i in range(1000):
			final_reward=final_reward+np.array(result.get())


# ERROR has been commited here as the final_reward is to be divided by 1000 instead of 2
		final_reward=final_reward/2

# Plottig Section
		plt.plot(final_reward,'r')
		plt.ylabel('Average Reward')
		plt.xlabel('Steps')
		plt.title('UCB with c=2,1000 arms')	
		plt.show()

if __name__=='__main__':


	def _pickle_method(m):
		if m.im_self is None:
			return getattr, (m.im_class, m.im_func.func_name)
		else:
			return getattr, (m.im_self, m.im_func.func_name)

	copy_reg.pickle(types.MethodType, _pickle_method)
	obj=UCB()