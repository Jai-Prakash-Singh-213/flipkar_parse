import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import glob
import time
import sys

num_fetch_threads = 50
enclosure_queue = Queue()


def worker(i,q):
    while True:
        filepth = q.get()
        fpath = "/home/desktop/flipkart/handbag_bypart/code3_scrap_links_its_info6/code3_scrap_links_its_info6/spiders/"
    
        subprocess.call(['scrapy', 'runspider',  fpath+'code1_linkcollection_and_extract.py', '-a', 'filepath='+filepth])
	time.sleep(2)
        q.task_done()




def main(filepath):


    f = glob.glob(filepath+'/*.html')
    print f

    val = len(f)/6

    val1 = val*5
    val2 = val*6

    f = f[val1:]
    

    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    
    


    for filepth in f:
        enclosure_queue.put(filepth)

    print '*** Main thread waiting ***'
    startime = time.strftime("%I:%M:%S")
    enclosure_queue.join()
    finishedtime =  time.strftime("%I:%M:%S")
    print '*** Done ***'
    print startime, ":", finishedtime

    

    return 0

    
if __name__=="__main__":
    cat_dir = sys.argv[1].strip()
    filepath = "/home/desktop/flipkart/handbag_bypart/brands_htmls/"+ cat_dir

    main(filepath)
