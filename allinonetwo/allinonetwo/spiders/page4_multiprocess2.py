#!/usr/bin/env python 
import profile
import subprocess
from scrapy import cmdline
import multiprocessing
from multiprocessing import Process
import time

# page4.py   page4_multiprocess.py page4_filedivision.py
#            page4_multiprocess2.py

cexc = cmdline.execute



def main2(pth):
        cexc(['scrapy',  'runspider', 'page4.py',   '-a',  'pth=%s' %(pth)])



def main(pth_list):

    for pth in pth_list:
       worker = Process(target=main2, args=(pth,))
       #worker.daemon = True 
       worker.start()
       time.sleep(6)

    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()



if __name__=="__main__":
    profile.run("main()")

