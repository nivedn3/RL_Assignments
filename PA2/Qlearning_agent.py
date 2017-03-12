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

class q_agent(Agent):

	learningrate=
	gamma=

	def agent_init(self,taskSpecString):

	def agent_start(self,Obs):
		State = Obs.intArray[0]
		action = self.epsilon_greedy(State)
		
		returnaction = Action()
		returnaction.intArray = action

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)	

		#might need to return something
		return returnaction

	def agent_step(self,Reward,Obs):

		new_state = Obs.intArray[0]
		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]



		Q_sa = self.qfunction[last_state][last_action]
		Q_saprime = self.maxim(new_state)

		Q_new = Q_sa + self.learningrate*( Reward + self.gamma*Q_saprime - Q_sa)
		
		if not self.pause:
			qfunction[last_state][last_action] = Q_new

		#To be taken
		new_action = self.epsilon_greedy(new_state)

		returnaction = Action()
		returnaction.intArray = new_action

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)

		return returnaction

	def agent_end(self,Reward):

		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]
		Q_sa = self.qfunction[last_state][last_action]
		new_Q_sa=Q_sa + self.sarsa_stepsize * (reward - Q_sa)
		
		if not self.pause:
			qfunction[last_state][last_action] = Q_new
		else:

	def maxim(self,state):
		return max(self.qfunction[state])

	def epsilon_greedy(self,state):
		if random.random() < self.epsilon:
			return random.randint(0,3)
		else:

			k=self.qfunction[state].index(max(self.qfunction[state]))
			return k


	def agent_cleanup(self):
		pass

	def agent_message(self,Message):
		
		if Message.startswith(""):






if __name__ == "__main__":
	AgentLoader.loadAgent(s_agent)