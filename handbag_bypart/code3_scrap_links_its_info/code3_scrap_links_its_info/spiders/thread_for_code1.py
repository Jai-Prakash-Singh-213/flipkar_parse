import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import glob

num_fetch_threads = 10
enclosure_queue = Queue()


def worker(i,q):
    while True:
        filepth = q.get()
        
        subprocess.call(['scrapy', 'crawl',  'collect_link_and_extract', '-a', 'filepath='+filepth])
	time.sleep(2)
        q.task_done()




def main(filepath):
    

    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    
    f = glob.glob(filepath+'/*.html') 


    for filepth in f:
        enclosure_queue.put(filepth)

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'
    

    return 0

    
if __name__=="__main__":
    filepath = "/home/desktop/flipkart/handbag_bypart/code2_scrolling/code2_scrolling/spiders/"
    main(filepath)
