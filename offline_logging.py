import csv
import time
import random
import os

name =str(time.strftime("%d-%m-%Y_%H-%M-%S") + '.csv')
line=[]
count = 0

def log_offline():# add params
    while(count<9):
        a = random.random()
        b = random.random()
        c=[a,b]
        #c=(log.get_rpm(),log.get_speed,.....)
        line.append(c)
        count=count+1


    with open(name,'a') as file:
        if(os.path.isfile(name) and os.path.getsize(name) > 0):
            wr = csv.writer(file,quoting=csv.QUOTE_ALL)
            for data in line:
                wr.writerow(data)
        else:
            wr = csv.writer(file,quoting=csv.QUOTE_ALL)
            wr.writerow(["RPM","Speed"])
            for data in line:
                wr.writerow(data)

    print(line)
    file.close()
