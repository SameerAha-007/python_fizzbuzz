from threading import *
import time

# Create a stop flag
stop_flag = False

def signal_state():
   global stop_flag
   while not stop_flag:
      time.sleep(5)
      print("Traffic Police Giving GREEN Signal")
      event.set()
      time.sleep(10)
      print("Traffic Police Giving RED Signal")
      event.clear()
   print("Signal state stopped")

def traffic_flow():
   global stop_flag
   num = 0
   while num < 10 and not stop_flag:
      print("Waiting for GREEN Signal")
      event.wait()
      print("GREEN Signal ... Traffic can move")
      while event.is_set() and not stop_flag:
         num += 1
         print("Vehicle No:", num, " Crossing the Signal")
         time.sleep(2)
      print("RED Signal ... Traffic has to wait")
   print("Traffic flow stopped")

event = Event()
t1 = Thread(target=signal_state)
t2 = Thread(target=traffic_flow)
t1.start()
t2.start()

# Let the threads run for a certain amount of time, then stop them
time.sleep(30)  # Adjust this time as needed to observe the behavior
stop_flag = True
t1.join()
t2.join()
print("Both threads have been stopped")
