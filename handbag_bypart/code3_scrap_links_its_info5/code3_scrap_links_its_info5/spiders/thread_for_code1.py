import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import glob
import time

num_fetch_threads = 100
enclosure_queue = Queue()


def worker(i,q):
    while True:
        filepth = q.get()
        
        subprocess.call(['scrapy', 'crawl',  'collect_link_and_extract', '-a', 'filepath='+filepth])
	time.sleep(2)
        q.task_done()




def main(filepath):


    f = glob.glob(filepath+'/*.html')

    val = len(f)/6

    val1 = val*4
    val2 = val*5

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
    finishedtime =  time.strftime("%I:%M:%S")
    print '*** Done ***'
    print startime, ":", finishedtime

    

    return 0

    
if __name__=="__main__":
    filepath = "/home/desktop/flipkart/handbag_bypart/code2_scrolling/code2_scrolling/spiders/"
    main(filepath)
