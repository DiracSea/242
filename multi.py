'''
Created Date: Thursday, January 30th 2020, 11:17:28 am
Author: Longze SU
'''

import crawler
import time
from multiprocessing import Pool, Queue
from threading import Thread, Lock
import queue
import sys



def MultiThread(queue, thread): 
    for i in range(thread):
        t = Thread(target=crawler.crawler, args=(queue.get(),))
        t.start()
    t.join() 

def MultiProcessing(queue, processor): 
    p = Pool()
    for i in range(processor):
        p.apply_async(crawler.crawler,args=(queue.get(),))
    p.close    
    p.join

def main(): 
    q = Queue()
    for i in range(100): 
        q.put("#LA")
        q.put("#Irvine")
        q.put("#Riverside")
        q.put("#Chinese Food")
        q.put("#beach")
        q.put("#museum")

    start_time = time.time()    
    crawler.crawler(q.get())
    end_time = time.time()
    total_time = end_time - start_time
    
    MT = []
    MP = []
    for i in range(1,8): 
        start_time = time.time()    
        MultiThread(q, i)
        end_time = time.time()
        total_time1 = end_time - start_time

        start_time = time.time()    
        MultiProcessing(q, i)
        end_time = time.time()
        total_time2 = end_time - start_time

        MT.append(total_time1)
        MP.append(total_time2)       
        
 
    print("Sequential End, Time is: {}".format(total_time))
    for i in range(len(MT)-1):
        print("MultiThread "+str(i+1)+" End, Time is：{}".format(MT[i]))
        print("MultiProcessing "+str(i+1)+" End, Time is：{}".format(MP[i]))

if __name__ == "__main__":
    main()