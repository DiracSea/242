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
    rs=crawler.crawler("ONE")
    crawler.writer(rs)
    end_time = time.time()
    total_time = end_time - start_time
    print("Sequential End, Time is: {}".format(total_time))
    
 

if __name__ == "__main__":
    main()