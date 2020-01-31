'''
Created Date: Thursday, January 30th 2020, 11:17:28 am
Author: Longze SU
'''

import crawler
import time
from multiprocessing import Pool 
from threading import Thread, Lock
import queue



def MultiThread(queue): 
    for i in range(4):
        t = Thread(target=crawler.crawler, args=(queue.get(),))
        t.start()
    t.join() 

def main(): 
    q = queue.Queue()

    q.put("#LA")
    q.put("#Irvine")
    q.put("#Riverside")
    q.put("#Chinese Food")
    q.put("#beach")
    q.put("#museum")
    start_time = time.time()    
    # crawler.crawler("#LA")
    # # crawler.writer(rs)
    # crawler.crawler("#beach")
    # # crawler.writer(rs)
    # crawler.crawler("#Chinese Food")
    # end_time = time.time()
    # total_time = end_time - start_time

    # start_time = time.time()
    # # rs=crawler.crawler("#LA")
    # t1 = threading.Thread(target=crawler.crawler,args=("#LA",))
    # t2 = threading.Thread(target=crawler.crawler,args=("#beach",))  
    # t3 = threading.Thread(target=crawler.crawler,args=("#Chinese Food",))  
    # t1.start()
    # t2.start()
    # t3.start()

    # # 等待两个子线程结束再结束主线程
    # t1.join()
    # t2.join()
    # t3.join()
    MultiThread(q)

    end_time = time.time()
    total_time1 = end_time - start_time

    #print("Sequential End, Time1 is: {}".format(total_time))
    print("MultiThread End, Time2 is：{}".format(total_time1))
 

if __name__ == "__main__":
    main()