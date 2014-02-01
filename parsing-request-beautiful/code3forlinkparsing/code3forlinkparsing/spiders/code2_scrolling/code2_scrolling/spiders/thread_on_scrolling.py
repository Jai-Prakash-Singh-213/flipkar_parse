import subprocess
from Queue import Queue
from threading import Thread
import time
import os
import sys


num_fetch_threads = 50
enclosure_queue = Queue()


def worker(i,q):
    while True:
        cat, brand_and_url = q.get()

        currentdir = os.getcwd()

        filepath = currentdir + "/code2_scrolling/code2_scrolling/spiders/page1_scroll.py"

        subprocess.call(['scrapy', 'runspider', filepath, '-a', 'brand_and_url='+ brand_and_url, '-a',  'cat='+cat])

	time.sleep(2)
        q.task_done()



    

def main(cat, filename):

    currentdate = time.strftime("%d%m%Y")

    f = open("avail_cat","a+")
    print >>f, cat + currentdate
    f .close()
    

    
    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    
    f = open(filename)
 
    for brand_url_string in f:
        brand_url_string = brand_url_string.strip()
        enclosure_queue.put((cat, brand_url_string))

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'
    
    

    return 0

    
if __name__=="__main__":
    
    main(sys.argv[1], sys.argv[2])
