'''
Created Date: Thursday, January 30th 2020, 11:17:28 am
Author: Longze SU
'''

import crawler
import time
from multiprocessing import Pool, Queue
from threading import Thread, Lock
import csv
import os
 

# def MultiProcessing(queue, processor, task): 
#     if queue.qsize() < processor: 
#         return

#     p = Pool(task)
#     for i in range(processor):
#         p.apply_async(crawler.crawler,args=(queue.get(),))
#     p.close    
#     p.join
def MultiThread(queue, thread): 
    for i in range(thread):
        t = Thread(target=crawler.crawler, args=(queue.get(),))
        t.start()
    t.join() 

def getQuery(dir,file): 
    res = []
    with open(os.path.join(dir,file), 'r') as f:
        reader = csv.reader(f) 
        for line in reader: 
            res.append(line[0])
    return res

def main(): 
    dir_name = 'file'
    file_name = 'query1.csv'
    queries = getQuery(dir_name, file_name)
    q = Queue()
    for i in queries: 
        q.put(i)
    size = len(queries)
    MT = []
    # MP = []
    while q.qsize(): 

        start_time = time.time()    
        MultiThread(q, 5)
        end_time = time.time()
        total_time = end_time - start_time
        time.sleep(1)
        start_time = time.time() 
        MultiThread(q, 5)
        end_time = time.time()
        total_time1 = end_time - start_time 

        MT.append(total_time+total_time1)


    print("MultiThread 5 End, Task is: +"str(size)"+ , Time is：{}".format(sum(MT)))


if __name__ == "__main__":
    main()