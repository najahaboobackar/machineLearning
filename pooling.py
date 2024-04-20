import numpy as np
import threading
def mx_pl(image,pool_size,output,i,j):
    p_h,p_w=pool_size
    polR=image[i*p_h:(i+1)*p_h,j*p_w:(j+1)*p_w]
    output[i,j]=np.max(polR)
def min_pl(image,pool_size,output,i,j):
    p_h,p_w=pool_size
    polR=image[i*p_h:(i+1)*p_h,j*p_w:(j+1)*p_w]
    output[i,j]=np.min(polR)  
def app_po(image,pool_size,poolfunc):
    h,w=image.shape
    p_h,p_w=pool_size
    o_h=h//p_h
    o_w=w//p_w
    pol_img=np.zeros((o_h,o_w))
    threads=[]
    for i in range(o_h):
        for j in range(o_w):
            t=threading.Thread(target=poolfunc,args=(image,pool_size,pol_img,i,j))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()  
    return pol_img    
image=np.array([[1,2,3],[2,3,4],[3,5,6]])
pool_size=(2,2)
print(image)
print("after maxpool")   
print(app_po(image,pool_size,mx_pl))
print("after minpool")
print(app_po(image,pool_size,min_pl))

