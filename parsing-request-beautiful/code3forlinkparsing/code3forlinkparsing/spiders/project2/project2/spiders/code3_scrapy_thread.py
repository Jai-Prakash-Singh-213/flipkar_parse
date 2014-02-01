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
        filepth = q.get().strip()

	currentdir = os.getcwd()

        codes = currentdir + "/project2/project2/spiders/code3_scrapy.py"
 
        logging.debug(['scrapy', 'runspider',  codes, '-a', 'filepath='+filepth])
        #sys.exit()
        subprocess.call(['scrapy', 'runspider',  codes,  '-a', 'filepath='+filepth])
	time.sleep(2)
        q.task_done()




def main2(filepath, f):

        

    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    


    for filepth in f:
        enclosure_queue.put(filepth)

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
        print f

        val = len(f)/6

        val1 =  val*1
        val2 = val*2
       
        main2(filepath, f) 

    finishtime = time.strftime("%H:%M:%S")
    
    print (starttime, finishtime)


    
if __name__=="__main__":
  
    main() 
