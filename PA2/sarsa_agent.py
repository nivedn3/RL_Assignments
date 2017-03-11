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

	def agent_init(self,taskSpecString):


	def agent_start(self,Obs):
		State = Obs.intArray[0]
		action = self.epsilon_greedy(State)
		returnaction = Action()
		returnaction.intArray = action

		return returnaction

		self.lastaction = copy.deepcopy(returnaction)
		self.lastObs = copy.deepcopy(Obs)



	def agent_step(self,Reward,Obs):

		new_state = Obs.intArray[0]
		last_state = self.lastObs.intArray[0]
		last_action = self.lastaction.intArray[0]

		new_action = self.epsilon_greedy(new_state)

		Q_sa = self.qfunction[last_state][lastaction]
		Q_saprime = self.qfunction[new_state][new_action]

		Q_new = Q_sa + self.learningrate*( Reward + self.gamma*Q_saprime - Q_sa)
		
		self.lastaction = 



	def agent_end(self,Reward):

	def agent_cleanup(self):
		pass

	def agent_message(self,inMessage):


if __name__ == "__main__":
	AgentLoader.loadAgent(s_agent)