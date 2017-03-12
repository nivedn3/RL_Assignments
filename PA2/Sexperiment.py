#To compute the average number of steps as well as the average reward

import rlglue.RLGlue as RLGlue
import sys

#def q_experiment():
#	for i in



RLGlue.RL_init()
RLGlue.RL_episode(5000)
print RLGlue.RL_return()
#q_experiment()
