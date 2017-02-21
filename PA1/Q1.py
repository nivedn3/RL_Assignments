import numpy as np
from random import randint
from numpy.random import choice
import matplotlib.pyplot as plt
class Bandit():
	def __init__(self):
		self.bandit()

	def gaussian(self,offset):
		g=np.random.normal(offset,1,1000)
		return g

	def bandit(self):
		print "tt"
		self.a=[]
		means=[0.2,-0.8,1.5,0.4,1.2,-1.5,-0.1,-1.0,0.8,-0.5]
		for i in range(10):
			self.a.append(self.gaussian(means[i]))
		self.trials()

	def trials(self):
		print "tt"
		armcount=[0 for i in range(10)]	
		reward=[0 for i in range(1,1001)]
		for j in range(2000):
			Q=[0 for i in range(10)]
			count=[0 for i in range(10)]
			
			Reward=[0 for i in range(1001)]
			for i in range(1,1001):
				arm=[j for j in range(10)]
				maxvalue=Q.index(max(Q))
				del arm[maxvalue]
				k=[maxvalue,arm[randint(0,8)]]
				p=[0.9,0.1]

				maxvalueE=choice(k,p=p)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1

				Rt=self.a[maxvalueE][randint(0,999)]
				Q[maxvalueE]=Q[maxvalueE]+1/count[maxvalueE]*(Rt-Q[maxvalueE])
				Reward[i]=(Rt+Reward[i-1])/i;
			reward=[x+y for x,y in zip(reward,Reward)]
			
		reward=[i/2000 for i in reward]
		plt.plot(reward,'r')	
		print armcount
		

		armcount=[0 for i in range(10)]
		reward=[0 for i in range(1001)]
		for j in range(2000):
			Q=[0 for i in range(10)]	
			count=[0 for i in range(10)]
			Reward=[0 for i in range(1001)]

			for i in range(1,1001):
				#a=[j for j in range(10)]
				maxvalueE=Q.index(max(Q))
				#del a[maxvalue]

				#k=[maxvalue,a[randint(0,8)]]
				#p=[1,0]

				#maxvalueE=choice(k,p=p)
				count[maxvalueE]=count[maxvalueE]+1
				armcount[maxvalueE]=armcount[maxvalueE]+1

				Rt=self.a[maxvalueE][randint(0,999)]
				Q[maxvalueE]=Q[maxvalueE]+1/count[maxvalueE]*(Rt-Q[maxvalueE])
				Reward[i]=(Rt+Reward[i-1])/i
			reward=[x+y for x,y in zip(reward,Reward)]
		#plt.hist(reward,1000,normed=True)
		reward=[i/2000 for i in reward]
		plt.plot(reward,'g')
		print armcount
		plt.show()

if __name__=='__main__':
	obj=Bandit()




