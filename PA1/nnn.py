from multiprocessing import Process
import time
def func():
	print "Nothing"
	time.sleep(5)

if __name__=="__main__":
	jobs=[]
	for i in range(2000):
		p=Process(target=func)
		jobs.append(p)
		p.start()
