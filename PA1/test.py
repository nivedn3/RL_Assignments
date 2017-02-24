import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
import random
import sys
import multiprocessing 
from multiprocessing import Process,Array
import copy_reg
import types





class Bandits():
	rew=[0 for i in range(1000)]
	def __init__(self):
		self.gaussian_rewards()

	def gaussian(self,mean):
		gaussian=np.random.normal(mean,1,10000)
		return list(gaussian)

	def gaussian_rewards(self):
		self.arms=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.arms.append(self.gaussian(means[i]))
		self.trials()

	def iteration(self,reward,result):
		
		Q=[0 for i in range(10)]
		count=[0 for i in range(10)]
		for inner in range(1000):
			maxvalue=Q.index(max(Q))
			maxvalueE=epsilon_greedy(maxvalue)
			count[maxvalueE]=count[maxvalueE]+1
			Return=self.arms[maxvalueE][randint(0,9999)]
			Q[maxvalueE]=Q[maxvalueE]+(Return-Q[maxvalueE])/count[maxvalueE]
			reward[inner]=reward[inner]+Return
			
		result.put(reward)
		

	def trials(self):
		armcount=[0 for i in range(10)]	
		reward=[0 for i  in   range(1000)]
		#reward=Array('d',reward)
		#print (reward[:])
		#for outer in range(2000):
		#	self.iteration()
		
		'''proc=[]
		for i in range(2000):
			p=Process(target=self.iteration,args=())
			proc.append(p)
		for p in  proc:
			p.start()
			p.join()'''
		tests=[i for i in range(10)]
		result=multiprocessing.Queue()
		jobs=[]
		for i in range(1000):
			p=Process(target=self.iteration,args=(reward,result))
			jobs.append(p)
			p.start()

		final=np.array([0 for i in range(1000)])
		for i in range(1000):
			#resultd.append(result.get())
			final=final+np.array(result.get())

		#print len()
		print final
		


def epsilon_greedy(maxvalue):
	if random.random()<=0.1:
		maxvalueE=randint(0,9)
	else:
		maxvalueE=maxvalue
	return maxvalueE

if __name__=='__main__':
	def _pickle_method(m):
		if m.im_self is None:
			return getattr, (m.im_class, m.im_func.func_name)
		else:
			return getattr, (m.im_self, m.im_func.func_name)

	copy_reg.pickle(types.MethodType, _pickle_method)
	obj=Bandits()




