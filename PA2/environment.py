import random
import inspect
import sys
from rlglue.environment.Environment import Environment
from rlglue.environment import EnvironmentLoader as EnvironmentLoader
from rlglue.types import Observation
from rlglue.types import Action
from rlglue.types import Reward_observation_terminal





class puddle_world(Environment):
	WORLD_WHITE=0
	WORLD_BLACK=-3
	WORLD_DARK_GREY=-2
	WORLD_GREY=-1
	Start_states=[[5,0],[6,0],[10,0],[11,0]]

	def env_init(self):
		self.map=[  [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 10],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,10 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-2 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-3 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 ,10 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-2 ,-2 ,-1 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ]  ]
		return 

	def env_start(self):

		State=random.randint(0,3)
		returnObs=Observation()
		#zero for all the 4 starting states
		self.presentCol=0
		self.presentRow=self.Start_states[State][0]
		returnObs.intArray=[self.calculateFlatState()]

		return returnObs

	def env_step(self,thisAction):

		assert len(thisAction.intArray)==1,"Expected 1 integer action."
		assert thisAction.intArray[0]>=0, "Expected action to be in [0,3]"
		assert thisAction.intArray[0]<4, "Expected action to be in [0,3]"

		self.updatePosition(thisAction.intArray[0])

		Obs=Observation()
		Obs.intArray=[self.calculateFlatState()]

		Reward=Reward_observation_terminal()
		Reward.r=self.calculateReward()
		Reward.o=theObs
		Reward.terminal=self.checkCurrentTerminal()

		return Reward

	def calculateFlatState(self):

		numrows=len(self.map)
		return self.presentCol* numrows + self.presentRow




		
