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
		
		self.states = [[5000,7999],[10000,11999]]
		
		return  "VERSION RL-Glue-3.0 PROBLEMTYPE episodic DISCOUNTFACTOR 0.9 OBSERVATIONS INTS (0 144000000) ACTIONS INTS (0 3) REWARDS (0 -1 -2 -3 10.0) EXTRA n" 

	def env_start(self):


		k = random.randint(0,1)
		State = random.randint(self.states[k][0],self.states[k][1])
		returnObs=Observation()
		#zero for all the 4 starting states
		self.presentCol=random.randint(0,999)
		#self.presentCol = 10900
		self.presentRow = State
		returnObs.intArray=[self.rolloutstate()]

		return returnObs

	def env_step(self,thisAction):

		#print thisAction.intArray[0]
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

		#print self.presentRow,self.presentCol,Reward.r
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

	#getting the state after making the 2-d list to 1-d already converted it into 12*12 grid 
	def rolloutstate(self):

		return self.presentRow/1000 * 12 + self.presentCol/1000

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
			if self.presentCol < 11999:
				self.presentCol = self.presentCol + 1
		#print self.presentCol,self.presentRow

	#finalising the position after checking whether the agent goes out of bounds
	def finalcheck(self,column,row):
		
		if (row < 0 or row >= 11999):
			return column,self.presentRow

		if (column < 0 or column >= 11999):
			return self.presentCol,row

		return column,row

	def current_reward(self):

		for i in range(3):
			if self.presentCol > 2999 + i*1000 and self.presentCol < 4000 + i*1000:
				if self.presentRow > 1999 + i*1000 and self.presentRow < 9000 - i*1000: 
					return (-1 - i) 

			if self.presentRow > 1999 + i*1000 and self.presentRow < 3000 + i*1000:
				if self.presentCol > 2999 + i*1000 and self.presentCol < 9000 - i*1000:
					return (-1 - i) 

			if self.presentRow > 7999 - i*1000 and self.presentRow < 9000 - i*1000:
				if self.presentCol > 2999 + i*1000 and self.presentCol < 8000 - i*1000  :
					return (-1 - i)

			if self.presentCol > 7999 - i*1000 and self.presentCol < 9000 -i*1000:
				if self.presentRow > 2999 + i*1000 and self.presentRow < 7000 - i*1000 :
					return (-1 - i)  
	
		if self.presentCol > 6999 and self.presentCol < 8000:
			if self.presentRow > 5999 and self.presentRow < 9000 :
				return -1
	
		if self.presentCol > 5999 and self.presentCol < 7000:
			if self.presentRow > 4999 and self.presentRow < 8000 :
				return -2
	
		#Reward
		if self.presentCol > 10999 :
			if self.presentRow < 1000:
				return 10 

		return 0 
	#Checking if the current position is the goal state 
	def goalcheck(self):


		# Only A goal state 
		if self.presentCol > 10999 :
			if self.presentRow < 1000:
				return True  

		return False 


if __name__ == "__main__":
	EnvironmentLoader.loadEnvironment(puddle_world())

