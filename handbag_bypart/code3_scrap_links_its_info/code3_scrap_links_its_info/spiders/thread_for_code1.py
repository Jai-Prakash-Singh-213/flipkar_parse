import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import glob
import time 
import sys

import logging




num_fetch_threads = 5
enclosure_queue = Queue()

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(i,q):
    while True:
        filepth = q.get().strip()
        fpath = "/home/desktop/flipkart/handbag_bypart/code3_scrap_links_its_info/code3_scrap_links_its_info/spiders/"     
        logging.debug(['scrapy', 'runspider',  fpath+'code1_linkcollection_and_extract.py', '-a', 'filepath='+filepth])
        #sys.exit()
        subprocess.call(['scrapy', 'runspider',  fpath+'code1_linkcollection_and_extract.py' , '-a', 'filepath='+filepth])
	time.sleep(2)




def main(filepath):

    f = glob.glob(filepath+'/*.html')
    
    val = len(f)/6

    val1 = val*0
    val2 = val*1

    f = f[val1:val2]

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

    
if __name__=="__main__":
    #cat_dir = sys.argv[1].strip()
    f = open("/home/desktop/flipkart/handbag_bypart/avail_cat")
    cat_dir = f.read().strip().split("\n")
    for cat in cat_dir:
        filepath = "/home/desktop/flipkart/handbag_bypart/brands_htmls/"+ cat
        main(filepath)
