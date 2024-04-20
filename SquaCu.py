import threading
def sqCu(n):
    print(f"square{n}:{n**2}")
    print(f"cube{n}:{n**3}")
nums=[1,2,3,4]
threads=[threading.Thread(target=sqCu,args=(num,))for num in nums]  
[t.start()for t in threads]  
[t.join()for t in threads]
