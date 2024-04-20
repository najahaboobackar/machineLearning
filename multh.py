import threading
def TH(inputf,outf,filfunc):
    with open(inputf,"r") as inp, open(outf,"w") as outfg:
        for line in inp:
            fil=filfunc(line)
            if fil:
                outfg.write(fil)
def chr(line):
    return ''.join(filter(str.isalpha, line))
def num(line):
    return ''.join(filter(str.isdigit,line))
def spe(line):
    return ''.join(filter(lambda x:not x.isalnum(),line))
i1="inp.csv"
o1="out.csv"
o2="outc.csv"
o3="outn.csv"
thread1=threading.Thread(target=TH,args=(i1,o1,spe))
thread2=threading.Thread(target=TH,args=(i1,o2,chr))
thread3=threading.Thread(target=TH,args=(i1,o3,num))  
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()      

