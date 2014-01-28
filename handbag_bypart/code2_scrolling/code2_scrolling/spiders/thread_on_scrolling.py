import subprocess
from Queue import Queue
from threading import Thread
import time

num_fetch_threads = 5
enclosure_queue = Queue()


def worker(i,q):
    while True:
        brand_and_url = q.get()
        
        subprocess.call(['scrapy', 'crawl',  'page1_scroll', '-a', 'brand_and_url='+brand_and_url])
	time.sleep(2)
        q.task_done()

    

def main():
    filename = "/home/desktop/flipkart/handbag_bypart/code1_brandcollection/code1_brandcollection/spiders/page1_brandname_brandlink"


    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        #t.setDaemon(True)
        t.start()
    
    f = open(filename)
 
    for brand_url_string in f:
        brand_url_string = brand_url_string.strip()
        enclosure_queue.put(brand_url_string)

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'


    
        
   

    
if __name__=="__main__":
    main()
