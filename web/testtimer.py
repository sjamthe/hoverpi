import time
from threading import Timer

def print_time(args): 
	while(1):
		print("From print_time", args, time.time())
		time.sleep(1)

def print_some_times():
	on = True
	t = Timer(2, print_time,[on])
	t.start()
	print ("Timer started",time.time())
	time.sleep(10)
	on = False
	t.cancel()
	print ("stopped",on, time.time())

print_some_times()
