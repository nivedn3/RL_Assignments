import random
import inspect
import sys
from rlglue.environment.Environment import Environment
from rlglue.environment import EnvironmentLoader as EnvironmentLoader
from rlglue.types import Observation
from rlglue.types import Action
from rlglue.types import Reward_observation_terminal





class puddle_world(Environment):

	WORLD_GOAL = 10
	Start_states=[[5,0],[6,0],[10,0],[11,0]]
	Action_probab = 0.1
	self.g=0

	def env_init(self):
		self.map=[  [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, self.g],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , self.g , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-2 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-3 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 , self.g ,-1 , 0 , 0, 0 ],
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
		Obs.intArray=[self.rolloutstate()]

		Reward=Reward_observation_terminal()
		Reward.r=self.current_reward()
		Reward.o=Obs
		Reward.terminal=self.goalcheck()

		return Reward

	def env_cleanup(self):
		pass

	def env_message(self,Message):

		if Message.startswith("set-goalstates"):
			self.g = Message.split(" ")[1]


	#getting the state after making the 2-d list to 1-d
	def rolloutstate(self):

		numrows=len(self.map)
		return self.presentCol* numrows + self.presentRow

	#updating the position
	def updatePosition(self,thisAction):

		#To account for the action stochasticity 
		if random.random() < Action_probab :
			thisAction = random.randint(0,3)

		column = self.presentCol
		row = self.presentRow

		#move down
		if(thisAction == 0):
			column=column + 1;

		#move right
		if(thisAction == 1):
			row=row + 1
		
		#move up
		if(thisAction == 2):
			column=column - 1
		#move down
		if(thisAction == 3):
			row=row - 1

		self.presentCol,self.presentRow = self.finalcheck(column,row)

	#finalising the position after checking whether the agent goes out of bounds
	def finalcheck(self,column,row):
		
		if (row < 0 || row >= len(self.map)):
			return column,self.presentRow

		if (column < 0 || column >= len(self.map[0]))
			return self.presentCol,row

	def current_reward(self):

		return self.map[self.presentRow][self.presentCol]

	#Checking if the current position is the goal state 
	def goalcheck(self):

		if self.map[self.presentRow][self.presentCol] == 10:
			return True

		else:
			return False 

if __name_ == "__main__":
	EnvironmentLoader.loadEnvironment(puddle_world)

