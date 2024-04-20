import csv
with open("area.csv",'r') as fileo:
    red=csv.reader(fileo)
    for i in red:
        print(i)
with open('area.csv','w') as fil:
    wr=csv.writer(fil)
    wr.writerow(["i  "])        
