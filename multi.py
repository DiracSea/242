'''
Created Date: Thursday, January 30th 2020, 11:17:28 am
Author: Longze SU
'''

import crawler
import time
from multiprocessing import Pool 
import threading


def main():
    start_time = time.time()    
    rs=crawler.crawler("#LA")
    crawler.writer(rs)
    rs=crawler.crawler("#beach")
    crawler.writer(rs)
    end_time = time.time()
    total_time = end_time - start_time

    start_time = time.time()
    rs=crawler.crawler("#LA")
    t1 = threading.Thread(target=crawler.writer,args=(rs,))
    t2 = threading.Thread(target=crawler.crawler,args=("#beach",)) 
    t1.start()
    t2.start()

    # 等待两个子线程结束再结束主线程
    t1.join()
    t2.join()

    end_time = time.time()
    total_time1 = end_time - start_time

    print("Sequential End, Time1 is: {}".format(total_time))
    print("MultiThread End, Time2 is：{}".format(total_time1))
 

if __name__ == "__main__":
    main()