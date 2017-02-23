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
		g=np.random.normal(mean,1,10000)
		return g

	def bandit(self):
		print "tt"
		self.a=[]
		means=[0.2,-0.8,1.55,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.a.append(np.random.normal(0,1,10000)+means[i])
		self.trials()



	def trials(self):
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1000)]
		c=0
		v=0
		for z in range(2000):
			Q=[0 for i in range(10)]
			#Q=np.array(Q)
			count=[0 for i in range(10)]
			count=np.array(count)
			for op in range(1000):
				maxvalue=Q.index(max(Q))
				
				k=[maxvalue,randint(0,9)]

				if random.random()<0.1:
					maxvalueE=randint(0,9)
				else:
					maxvalueE=maxvalue
				#maxvalueE=choice(k,p=p)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1

				Rt=self.a[maxvalueE][randint(0,9999)]
				print Rt
				#print Rt

				Q[maxvalueE]=Q[maxvalueE]+1/count[maxvalueE]*(Rt-Q[maxvalueE])
				reward[op]=reward[op]+Rt
				
		reward=np.array(reward)
		reward=reward/2000
		plt.plot(reward,'r')	
		print armcount
		print reward
		print v
		plt.show()
		
	
		'''armcount=[0 for i in range(10)]
		reward=[0 for i in range(1001)]
		for j in range(2000):
			Q=[0 for i in range(10)]
			#Q=np.array(Q)	
			count=[0 for i in range(10)]
			count=np.array(count)
			Reward=[0 for i in range(1001)]

			for i in range(1000):
				#a=[j for j in range(10)]
				maxvalueE=Q.index(max(Q))
				#del a[maxvalue]

				#k=[maxvalue,a[randint(0,8)]]
				#p=[1,0]

				#maxvalueE=choice(k,p=p)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1

				Rt=self.a[maxvalueE][randint(0,9999)]
				Q[maxvalueE]=Q[maxvalueE]+1/count[maxvalueE]*(Rt-Q[maxvalueE])
				#Reward[i]=(Rt+(i-1)*Reward[i-1])/i
				reward[i]=reward[i]+Rt
			#reward=[x+y for x,y in zip(reward,Reward)]
		#plt.hist(reward,1000,normed=True)
		reward=np.array(reward)
		reward=reward/2000
		plt.plot(reward,'g')
		print armcount'''
		

if __name__=='__main__':
	obj=Bandit()




