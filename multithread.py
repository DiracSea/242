# -*- coding: utf-8 -*
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
import clean

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

def MultiThreadOne(query, thread, max_tweets): 
    for i in range(thread):
        t = Thread(target=crawler.crawler, args=(query,max_tweets,))
        t.start()
    t.join() 

def genQueue(num): 
    queries = query.genQueries(num)
    q = Queue() 
    for i in queries: 
        q.put(i)
    return q

def test(): 
    threads = [5]
    MT = []; SEQ = []
    for t in threads: 
         
        start_time = time.time() 
        MultiThreadOne('California', t, 200) 
        end_time = time.time()
        MT.append(end_time-start_time)
        time.sleep(1)
        start_time = time.time() 
        crawler.crawler('California', t*200) 
        end_time = time.time()
        SEQ.append(end_time-start_time)

    for idx, (i, j) in enumerate(zip(MT, SEQ)): 
        print('Threads: '+str(threads[0])+': ')
        print('Multithread is: {}'.format(i))
        print('Seriel is: {}'.format(j))

def main(): 
    thread_num = 16

    #for i in range(2,0,-1): 
    i = 1
    q = genQueue(i)
    size = q.qsize()
    MT = []
    res = thread_num
    while q.qsize(): 
        if q.qsize() < thread_num:
            start_time = time.time() 
            MultiThread(q, q.qsize(), 1000) 
            end_time = time.time()

            total_time = end_time - start_time
            MT.append(total_time)

            res = res + thread_num
            print(str(res) + '\n')
            break

        start_time = time.time()    
        MultiThread(q, thread_num, 1000)
        end_time = time.time()
        total_time = end_time - start_time

        res = res + thread_num
        print(str(res) + '\n')
        MT.append(total_time)


    print("MultiThread "+str(thread_num)+" End, Task is: "+ str(size) + " , Time is: {}".format(sum(MT)))


if __name__ == "__main__":
    test()
    e1 = clean.errNum('result', 'samples.json')
    clean.cleaning('result', 'samples.json')
    e2 = clean.errNum('result', 'samples.json')
    print(e1)
    print(e2)
    