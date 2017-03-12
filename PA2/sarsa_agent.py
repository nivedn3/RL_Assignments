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

class s_agent(Agent):

	learningrate = 0.10
	gamma = 0.9
	epsilon = 0.1

	def agent_init(self,taskSpecString):

		self.numActions = 4
		self.numStates = 144
		self.qfunction = [self.numActions*[0.0] for i in range(self.numStates)]
		self.lastAction=Action()
		self.lastObs=Observation()

	def agent_start(self,Obs):
		State = Obs.intArray[0]
		action = self.epsilon_greedy(State)
		returnaction = Action()
		returnaction.intArray = [action]

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)	

		return returnaction

	def agent_step(self,Reward,Obs):

		new_state = Obs.intArray[0]
		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]

		new_action = self.epsilon_greedy(new_state)

		Q_sa = self.qfunction[last_state][last_action]
		Q_saprime = self.qfunction[new_state][new_action]

		Q_new = Q_sa + self.learningrate*( Reward + self.gamma*Q_saprime - Q_sa)
		
		#if not self.pause:
		self.qfunction[last_state][last_action] = Q_new

		returnaction = Action()
		returnaction.intArray = [new_action]

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)

		return returnaction

	def epsilon_greedy(self,state):

		if random.random() < self.epsilon:
			return random.randint(0,3)
		else:
			k=self.qfunction[state].index(max(self.qfunction[state]))
			return k



	def agent_end(self,Reward):

		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]
		Q_sa = self.qfunction[last_state][last_action]
		Q_new=Q_sa + self.learningrate * (Reward - Q_sa)

		#if not self.pause:
		self.qfunction[last_state][last_action] = Q_new

	def agent_cleanup(self):
		pass

	#def agent_message(self,Message):

		#if Message.startswith(""):

		#if Message.

if __name__ == "__main__":
	AgentLoader.loadAgent(s_agent())