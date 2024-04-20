def sl(string):
    return string[2:5]
def rev(string):
    return string[::-1]
def concate(sr1, string):
    return sr1+string
def main():
    k=input("enter the name")
    a=sl(k)
    b=rev(k)
    d=concate("najah",k)
    print(a ,end="\n")
main()    