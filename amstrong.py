def ams(num):
    org=num
    rev=0
    while(num!=0):
        s=num%10
        rev+=pow(s,3)
        num=num//10
    if org==rev:
        return True
    else:
        return False
k=int(input("ente rthe number")) 
a=ams(k)
if a:
    print("ams") 
else:
    print("noooooo")          
