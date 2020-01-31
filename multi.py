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
    if queue.qsize() < thread: 
        return
    for i in range(thread):
        t = Thread(target=crawler.crawler, args=(queue.get(),))
        t.start()
    t.join() 

# def MultiProcessing(queue, processor, task): 
#     if queue.qsize() < processor: 
#         return

#     p = Pool(task)
#     for i in range(processor):
#         p.apply_async(crawler.crawler,args=(queue.get(),))
#     p.close    
#     p.join

def main(): 
    q = Queue()
    for i in range(150): 
        q.put("#LA")
        # q.put("#Irvine")
        # q.put("#Riverside")
        # q.put("#Chinese Food")
        # q.put("#beach")
        # q.put("#museum")

    start_time = time.time()    
    crawler.crawler(q.get())
    end_time = time.time()
    total_time = end_time - start_time
    
    MT = []
    # MP = []
    for i in range(1,51): 
        time.sleep(1)

        start_time = time.time()    
        MultiThread(q, i)
        end_time = time.time()
        total_time1 = end_time - start_time

        MT.append(total_time1)

    # for i in range(1,6): 
    #     time.sleep(1)

    #     start_time = time.time()    
    #     MultiProcessing(q, i, 8)
    #     end_time = time.time()
    #     total_time2 = end_time - start_time

    #     MP.append(total_time2)       
        
 
    print("Sequential End, Task is 1, Time is: {}".format(total_time))
    for i in range(len(MT)):
        print("MultiThread "+str(i+1)+" End, Task is: "+str(i+1)+" , Time is：{}".format(MT[i]))
    # for i in range(len(MP)):
    #     print("MultiProcessing "+str(i+1)+" End, Task is: 8, Time is：{}".format(MP[i]))

if __name__ == "__main__":
    main()