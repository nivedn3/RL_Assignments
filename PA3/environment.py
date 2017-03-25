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
	a=0
	b=0
	c=10

	def env_init(self):
		self.map=[  [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, self.a],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , self.b , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-2 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-3 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 ,-2 ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-3 ,-2 , self.c ,-1 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-2 ,-2 ,-2 ,-1 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ],
					[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 ]  ]
		
		return  "VERSION RL-Glue-3.0 PROBLEMTYPE episodic DISCOUNTFACTOR 0.9 OBSERVATIONS INTS (0 143) ACTIONS INTS (0 3) REWARDS (0 -1 -2 -3 10.0) EXTRA n" 

	def env_start(self):

		State=random.randint(0,3)
		returnObs=Observation()
		#zero for all the 4 starting states
		self.presentCol=0
		self.presentRow=self.Start_states[State][0]
		returnObs.intArray=[self.rolloutstate()]

		return returnObs

	def env_step(self,thisAction):

		print thisAction.intArray[0]
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

		if Message.startswith("set-start-state"):
			k = int(Message.split(" ")[1])
			if k == 0:
				self.a = 10
				self.b = 0
				self.c = 0
			if k == 1:
				self.b = 10
				self.c = 0
				self.a = 0
			if k == 2:
				self.c = 10
				self.b = 0
				self.a = 0
		print self.a, self.b, self.c
	#getting the state after making the 2-d list to 1-d
	def rolloutstate(self):

		numrows=len(self.map)
		return self.presentCol* numrows + self.presentRow

	#updating the position
	def updatePosition(self,thisAction):

		#To account for the action stochasticity 
		if random.random() < self.Action_probab :
			thisAction = random.randint(0,3)

		column = self.presentCol
		row = self.presentRow

		#move right
		if(thisAction == 0):
			column=column + 1

		#move down
		if(thisAction == 1):
			row=row + 1
		
		#move left
		if(thisAction == 2):
			column=column - 1
		#move up
		if(thisAction == 3):
			row=row - 1

		self.presentCol,self.presentRow = self.finalcheck(column,row)

		if random.random() < 0.5:
			if self.presentCol < len(self.map[0])-1:
				self.presentCol = self.presentCol + 1

	#finalising the position after checking whether the agent goes out of bounds
	def finalcheck(self,column,row):
		
		if (row < 0 or row >= len(self.map)):
			return column,self.presentRow

		if (column < 0 or column >= len(self.map[0])):
			return self.presentCol,row

		return column,row

	def current_reward(self):

		return self.map[self.presentRow][self.presentCol]

	#Checking if the current position is the goal state 
	def goalcheck(self):

		if self.map[self.presentRow][self.presentCol] == 10:
			return True

		else:
			return False 


if __name__ == "__main__":
	EnvironmentLoader.loadEnvironment(puddle_world())

