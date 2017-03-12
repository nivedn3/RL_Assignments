import rlglue.RLGlue as RLGlue
import sys
import matplotlib.pyplot as plt

RLGlue.RL_init()

avg_steps_a = []
avg_reward_a = []
RLGlue.RL_env_message("set-start-state 0");
for i in range (40):
	num_of_steps = 0
	reward = 0 
	for j  in range(50):
		RLGlue.RL_episode(0)
		num_of_steps = num_of_steps + RLGlue.RL_num_steps()
		reward = reward + RLGlue.RL_return()
	avg_reward_a.append(reward/50)
	avg_steps_a.append(num_of_steps/50)


file=open("values_lam=0.3_c.txt",'w')
file.write(str(avg_steps_a))
file.write("                                    ")
file.write(str(avg_reward_a))

plt.plot(avg_steps_a,'r')
plt.ylabel('Average_Steps')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_steps of C')	
plt.show()

plt.plot(avg_reward_a,'r')
plt.ylabel('Average_Reward')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_Reward of C')	
plt.show()


