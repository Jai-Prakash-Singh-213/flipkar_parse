#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
import os
import sys
from scrapy import cmdline


mp_num_fetch_threads = 100
mp_enclosure_queue = multiprocessing.Queue()
mep =  mp_enclosure_queue.put




def main2(i, q):
    qget = q.get
    cexc = cmdline.execute
    while True:
        pth = qget()
        cexc(['scrapy',  'runspider', 'code6s_allinone.py',   '-a',  'pth=%s' %(pth)])
    
    

def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()


    output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    for i in range(mp_num_fetch_threads):
        worker = multiprocessing.Process(target=main2, args=(i, mp_enclosure_queue,))
	#worker.setDaemon(True)
	worker.start()

    for pth in pth_list:
         mep(pth)
         


if __name__=="__main__":
    main()





