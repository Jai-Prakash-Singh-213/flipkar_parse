import subprocess
from Queue import Queue
from threading import Thread
import time
import os


num_fetch_threads = 5
enclosure_queue = Queue()


def worker(i,q):
    while True:
        brand_and_url = q.get()
        
        subprocess.call(['scrapy', 'crawl',  'page1_scroll', '-a', 'brand_and_url='+brand_and_url])
	time.sleep(2)
        q.task_done()



def remain_link():
    f = open("page1_link_crawled")
    links_crawled = f.read().strip().split("\n")
    f.close()

    f = open("page1_link_crawling")
    links_crawling =  f.read().strip().split("\n")
    f.close()

    print len(links_crawling)
    print len(links_crawled)
    

    avail_link = list(set(links_crawling) - set(links_crawled))
    
    print avail_link
    
    if avail_link:
        
	f = open("page1_avail_link","w+")
	print >>f, '\n'.join(avail_link)
	f.close()

	main("page1_avail_link")
    
    else:
        return 0

    

def main(filename):
    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()
    
    f = open(filename)
 
    for brand_url_string in f:
        brand_url_string = brand_url_string.strip()
        enclosure_queue.put(brand_url_string)

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'
    
    remain_link()
    if os.path.isfile("page1_link_crawled"):
        print "page1_link_crawled: removed"
        os.remove("page1_link_crawled")
    
    if os.path.isfile("page1_link_crawling"):
        print "page1_link_crawling: removed"
        os.remove("page1_link_crawling")

    if os.path.isfile("page1_avail_link"):
        print "page1_avail_link: removed"
        os.remove("page1_avail_link")
    

    return 0

    
if __name__=="__main__":
    filename = "/home/desktop/flipkart/handbag_bypart/code1_brandcollection/code1_brandcollection/spiders/page1_brandname_brandlink2"
    main(filename)
