import random
import sys
import copy
import pickle
from rlglue.agent.Agent import Agent
from rlglue.agent import AgentLoader as AgentLoader
from rlglue.types import Action
from rlglue.types import Observation
from rlglue.utils import TaskSpecVRLGLUE3
from random import Random
import numpy as np 
import random

class q_agent(Agent):

	learningrate=0.1
	gamma=0.9
	epsilon=0.1
	lamda = 0.3
	#Next  is 0.9 
	lastAction=Action()
	lastObs=Observation()

	def agent_init(self,taskSpecString):

		self.numActions = 4
		self.numStates = 144
		self.qfunction = [self.numActions*[0.0] for i in range(self.numStates)]
		#x coordinate
		self.phi1 = np.array([i for i in range(12)])
		#y coordinate 
		self.phi2 = np.array([i for i in range(12)])




		#self.theta = np.array([ for i in range(4)])
		self.thetax = np.array([[random.random(),random.random(),random.random(),random.random()] for i in range(12)])
		self.thetay = np.array([[random.random(),random.random(),random.random(),random.random()] for i in range(12)])
		self.thetaxy = np.array([[[random.random(),random.random(),random.random(),random.random()] for i in range(12)] for j in range(12)])

		
		self.ex = np.array([0 for i in range(12)])
		self.ey = np.array([0 for i in range(12)])
		self.exy = np.array([[0 for i in range(12)] for j in range(12)])

		self.lastAction=Action()
		self.lastObs=Observation()


	def agent_start(self,Obs):
		State = Obs.intArray[0]
		action = self.epsilon_greedy(State)
		returnaction = Action()
		returnaction.intArray = [action]
		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)	

		#might need to return something
		return returnaction

	def agent_step(self,Reward,Obs):

		new_state = Obs.intArray[0]
		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]
		

		x=self.phi1[last_state % 12]
		y=self.phi2[(last_state-last_state % 12)/12]

		#Replacing traces 
		self.ex[x] = 1
		self.ey[y] = 1
		self.exy[x][y] = 1

		delta = Reward - self.thetax[x][last_action] - self.thetay[y][last_action] - self.thetaxy[x][y][last_action]




		x1=self.phi1[new_state % 12]
		y1=self.phi2[(new_state-new_state % 12)/12]

		#maxa = max(self.thetax[x1][0] + self.thetay[y1][0],self.thetax[x1][1] + self.thetay[y1][1],self.thetax[x1][2] + self.thetay[y1][2],self.thetax[x1][3] + self.thetay[y1][3] )
		#delta = delta  + self.gamma*maxa

		alpha = 0.1
		

		if random.random() < self.epsilon:
			new_action = random.randint(0,3)
		else:
			#k=self.qfunction[state].index(max(self.qfunction[state]))
			new_action = np.argmax([self.thetax[x1][0] + self.thetay[y1][0] + self.thetaxy[x1][y1][0],self.thetax[x1][1] + self.thetay[y1][1] + self.thetaxy[x1][y1][1],self.thetax[x1][2] + self.thetay[y1][2] + self.thetaxy[x1][y1][2],self.thetax[x1][3] + self.thetay[y1][3] + self.thetaxy[x1][y1][3]])

			#print k
		#print Reward,self.thetax,self.thetay
		
		delta = delta  + self.gamma*(self.thetax[x1][new_action]+self.thetay[y1][new_action] + self.thetaxy[x1][y1][new_action])

		self.thetax[x][last_action] = self.thetax[x][last_action] +  alpha*delta*self.ex[x]
		self.thetay[y][last_action] = self.thetay[y][last_action] +  alpha*delta*self.ey[y]
		self.thetaxy[x][y][last_action] = self.thetaxy[x][y][last_action] + alpha*delta*self.exy[x][y]

		self.ex = self.gamma*self.lamda*self.ex
		self.ey = self.gamma*self.lamda*self.ey
		self.exy = self.gamma*self.lamda*self.exy
		

		'''

		for i in range(4):

		Q_sa = self.qfunction[last_state][last_action]
			



		x1=self.phi1[new_state % 12]
		y1=self.phi2[(new_state-new_state % 12)/12]
		Q_saprime = max(np.dot(self.theta[0],[[x1],[y1]]),np.dot(self.theta[1],[[x1],[y1]]),np.dot(self.theta[2],[[x1],[y1]]),np.dot(self.theta[3],[[x1],[y1]]))

		#ALPHA NOT DECIDED
		alpha=0.1
		x=self.phi1[last_state % 12]
		y=self.phi2[(last_state-last_state % 12)/12]
		self.theta[last_action][0] = self.theta[last_action][0] + alpha*(Reward + self.gamma*Q_saprime - Q_sa) * x
		self.theta[last_action][1] = self.theta[last_action][1] + alpha*(Reward + self.gamma*Q_saprime - Q_sa) * y
		#print last_state % 12 ,last_state
		print Reward
		print self.theta
		#print self.qfunction
		#print Reward
		#Q_new = Q_sa + self.learningrate*( Reward + self.gamma*Q_saprime - Q_sa)
		'''
		#if not self.pause:

		#self.qfunction[last_state][last_action] = np.dot(self.theta[last_action],[[x],[y]])   

		#To be taken
		#new_action = self.epsilon_greedy(new_state)

		returnaction = Action()
		returnaction.intArray = [new_action]

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)

		return returnaction

	def agent_end(self,Reward):

		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]
		

		x=self.phi1[last_state % 12]
		y=self.phi2[(last_state-last_state % 12)/12]

		self.ex[x] = 1
		self.ey[y] = 1
		self.exy[x][y] = 1

		delta = Reward - self.thetax[x][last_action] - self.thetay[y][last_action]
		alpha = 0.1
		self.thetax[x][last_action] = self.thetax[x][last_action] +  alpha*delta*self.ex[x]
		self.thetax[y][last_action] = self.thetax[y][last_action] +  alpha*delta*self.ey[y]
		self.thetaxy[x][y][last_action] =  self.thetaxy[x][y][last_action] + alpha*delta*self.exy[x][y]


		#print Reward,self.thetax,self.thetay


	def maxim(self,state):
		return max(self.qfunction[state])

	def epsilon_greedy(self,state):
		if random.random() < self.epsilon:
			return random.randint(0,3)
		else:
			k=self.qfunction[state].index(max(self.qfunction[state]))
			#print k
			return k


	def agent_cleanup(self):
		pass

	def agent_message(self,Message):
		pass


if __name__ == "__main__":
	AgentLoader.loadAgent(q_agent())