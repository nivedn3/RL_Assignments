#To compute the average number of steps as well as the average reward
import multiprocessing 
import rlglue.RLGlue as RLGlue
import sys
import matplotlib.pyplot as plt


#def q_experiment():
#	for i in



RLGlue.RL_init()

'''for i in range(100):
	RLGlue.RL_episode(0)
	print RLGlue.RL_return()
'''
#q_experiment()


'''

avg_steps_a = []
avg_reward_a = []
RLGlue.RL_env_message("set-start-state 0");
for i in range (100):
	num_of_steps = 0
	reward = 0 
	for j  in range(50):
		RLGlue.RL_episode(0)
		num_of_steps = num_of_steps + RLGlue.RL_num_steps()
		reward = reward + RLGlue.RL_return()
	avg_reward_a.append(reward/50)
	avg_steps_a.append(num_of_steps/50)
'''
'''
avg_steps_b = []
avg_reward_b = []
RLGlue.RL_env_message("set-start-state 1");
for i in range (100):
	num_of_steps = 0
	reward = 0 
	for j  in range(50):
		RLGlue.RL_episode(0)
		num_of_steps = num_of_steps + RLGlue.RL_num_steps()
		reward = reward + RLGlue.RL_return()
	avg_reward_b.append(reward/50)
	avg_steps_b.append(num_of_steps/50)
'''

avg_steps_c = []
avg_reward_c = []
RLGlue.RL_env_message("set-start-state 2");
for i in range (50):
	num_of_steps = 0
	reward = 0 
	j = 0
	jobs = []
	while j < 20:
		
		#p=multiprocessing.Process(target=RLGlue.RL_episode,args=(100000,))
		#jobs.append(p)
		#p.start
		RLGlue.RL_episode(100000)
		j =  j+1
		if RLGlue.RL_return() == 0:
			j = j-1
		else:
			num_of_steps = num_of_steps + RLGlue.RL_num_steps()
			reward = reward + RLGlue.RL_return()

		print RLGlue.RL_return()
	avg_reward_c.append(reward/50)
	avg_steps_c.append(num_of_steps/50)


file=open("values.txt",'w')
file.write(str(avg_steps_c))
file.write("                                    ")
file.write(str(avg_reward_c))




plt.plot(avg_steps_a,'r')
plt.ylabel('Average_Steps')
plt.xlabel('Number of 20 episode runs')
plt.title('Average_steps of A')	
plt.show()

plt.plot(avg_reward_a,'r')
plt.ylabel('Average_Reward')
plt.xlabel('Number of 20 episode runs')
plt.title('Average_Reward of A')	
plt.show()

'''
plt.plot(avg_steps_b,'r')
plt.ylabel('Average_Steps')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_steps of B')	
plt.show()

plt.plot(avg_reward_b,'r')
plt.ylabel('Average_Reward')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_reward of B')	
plt.show()

'''
'''
plt.plot(avg_steps_c,'r')
plt.ylabel('Average_Steps')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_steps of C')	
plt.show()

plt.plot(avg_reward_c,'r')
plt.ylabel('Average_Reward')
plt.xlabel('Number of 50 episode runs')
plt.title('Average_reward of C')	
plt.show()'''






