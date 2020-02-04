'''
Created Date: Thursday, January 30th 2020, 11:17:28 am
Author: Longze SU
'''

import time
from multiprocessing import Pool, Queue
from threading import Thread, Lock
import csv
import os

import crawler
import query

# def MultiProcessing(queue, processor, task): 
#     if queue.qsize() < processor: 
#         return

#     p = Pool(task)
#     for i in range(processor):
#         p.apply_async(crawler.crawler,args=(queue.get(),))
#     p.close    
#     p.join
def MultiThread(queue, thread, max_tweets): 
    for i in range(thread):
        t = Thread(target=crawler.crawler, args=(queue.get(),max_tweets,))
        t.start()
    t.join() 

def genQueue(num): 
    queries = query.genQueries(num)
    q = Queue() 
    for i in queries: 
        q.put(i)
    return q

def main(): 
    thread_num = 16

    for i in range(2,0,-1): 
        q = genQueue(i)
        size = q.qsize()
        MT = []
        res = thread_num
        while q.qsize(): 
            if q.qsize() < thread_num:
                start_time = time.time() 
                MultiThread(q, q.qsize(), 50000) 
                end_time = time.time()

                total_time = end_time - start_time
                MT.append(total_time)

                res = res + thread_num
                print(str(res) + '\n')
                break

            start_time = time.time()    
            MultiThread(q, thread_num, 50000)
            end_time = time.time()
            total_time = end_time - start_time

            res = res + thread_num
            print(str(res) + '\n')
            MT.append(total_time)


        print("MultiThread "+str(thread_num)+" End, Task is: "+ str(size) + " , Time is：{}".format(sum(MT)))


if __name__ == "__main__":
    main()