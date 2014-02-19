import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import glob
import time 
import sys

import logging
import multiprocessing




num_fetch_threads = 100
enclosure_queue = Queue()

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(i,q):
    while True:
        filepth, cat = q.get()
        filepth = filepth.strip()
        cat = cat.strip()

	currentdir = os.getcwd()

        codes = currentdir + "/code3_scrapy.py"
 
        logging.debug(['scrapy', 'runspider',  codes, '-a', 'filepath='+filepth, '-a', 'cat='+cat])
        #sys.exit()
        subprocess.call(['scrapy', 'runspider',  codes,  '-a', 'filepath='+filepth, '-a', 'cat='+cat])
	time.sleep(2)
        q.task_done()




def main2(filepath, f, cat):

        

    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    


    for filepth in f:
        enclosure_queue.put((filepth, cat))

    print '*** Main thread waiting ***'
    startime = time.strftime("%I:%M:%S")
    enclosure_queue.join()
    print '*** Done ***'
    finishedtime =  time.strftime("%I:%M:%S")
    print startime, ":", finishedtime
    

    return 0




def main():

    starttime = time.strftime("%H:%M:%S")
    #cat_dir = sys.argv[1].strip()
    currentdir = os.getcwd()
    f_avail_path = currentdir + "/avail_cat"

    f = open(f_avail_path)

    cat_dir = f.read().strip().split("\n")
    

    for cat in cat_dir:
        filepath = currentdir + "/brands_htmls/"+ cat

        f = glob.glob(filepath+'/*.html')

        print filepath+'/*.html'
        #print f

        val = len(f)/3

        val1 = val*0
        val2 = val*1

        '''for i in range(6):
             try:
                 f = f[ : val]
             except:
                 f = f[ : ]

             p = multiprocessing.Process(target = main2, args=(filepath, f ))
             f = f[val : ]
             p.start()'''
       

        f2 = f[val1:val2]

        main2(filepath, f2, cat)

    finishtime = time.strftime("%H:%M:%S")
    
    print (starttime, finishtime)


    
if __name__=="__main__":
  
    main() 
