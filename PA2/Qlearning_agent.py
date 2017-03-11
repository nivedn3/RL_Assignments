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

def q_agent(Agent):

	def agent_init(self,taskSpecString):



	def agent_start(self,Obs):


	def agent_step(self,Reward,Obs):


	def agent_end(self,Reward):

	def agent_cleanup(self):
		pass

	def agent_message(self,inMessage):


if __name__ == "__main__":
	AgentLoader.loadAgent(s_agent)