import threading
import time
def print_time(threadname,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s %s" % (threadname,time.ctime(time.time()) ))
try:
	t1 = threading.Thread(target=print_time, args=("Thread-1:",2,))
	t2 = threading.Thread(target=print_time, args=("Thread-2:",3,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done!")

except:
    print("Something went wrong.")