import threading
import os
def thredDis():
    th_name=threading.current_thread().name
    pro=os.getpid()
    print(f"thread={th_name}:processid={pro}")
def worker():
    thredDis()
threads=[]
for i in range(3):
    t=threading.Thread(target=worker,name=f"thread-{i}")
    threads.append(t)
    t.start()  
for  t in threads:
    t.join()          
