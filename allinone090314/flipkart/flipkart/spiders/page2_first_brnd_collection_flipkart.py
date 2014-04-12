import req_proxy
import ast
from urlparse import urlparse
from bs4 import BeautifulSoup
import time
from threading import Thread
from Queue import Queue
import logging
import os
from lxml import html
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

num_fetch_threads = 100
enclosure_queue = multiprocessing.JoinableQueue()




def main2(line, catlink, filename2):
     menu = line[0].strip()
     submnlink  = line[1].strip()
     submntitle = line[2].strip()
     catlink = line[-2].strip()
     cattitle = line[-1].strip()

     page = req_proxy.main(catlink)

     soup = BeautifulSoup(page)

     tag_brand = soup.find("ul", attrs={"id":"brand"})

     tag_brand_a = []

     if tag_brand is not None:
         tag_brand_a = tag_brand.find_all("a")

     f = open(filename2, "a+")

     for al in tag_brand_a:
         brandlink =  "%s%s" %("http://www.flipkart.com", str(al.get("href")).strip())
         brandtitle = str(al.get_text()).replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
         print >>f,  [menu, submnlink, submntitle, catlink, cattitle, brandlink, brandtitle]
         logging.debug([menu, submnlink, submntitle, catlink, cattitle, brandlink, brandtitle])

     f.close()



def main(line, filename2):
    line = ast.literal_eval(line)
   
    catlink = line[-2].strip()
    
    parsed = urlparse(catlink)

    if len(parsed.path) < 1:
        pass 

    else:
        main2(line, catlink, filename2)




def mainthread2(i, q):
    for line, filename2 in iter(q.get, None):
        try:

            main(line, filename2)
            logging.debug(line)

        except:
            f2 = open("page2_first_error_filpkart.txt", "a+")
            print >>f2, line
            f2.close()

        time.sleep(2)
        q.task_done()

    q.task_done()




def mainthread():
    f = open("to_extractfilpkart")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "f_mn_smnl_smnt_ctl_ctl.txt")
    filename2 = "%s/%s" %(directory, "f_mn_smnl_smnt_ctl_ctl_bl_bt.txt")    

    f = open(filename)

    procs = []

    for i in range(num_fetch_threads):
        #procs.append(Thread(target=mainthread2, args=(i, enclosure_queue,)))
        procs.append(multiprocessing.Process(target=mainthread2, args=(i, enclosure_queue,)))
        #worker.setDaemon(True)
        procs[-1].start()

    for line in f:
        enclosure_queue.put((line, filename2))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'

    for p in procs:
        enclosure_queue.put(None)

    enclosure_queue.join()

    for p in procs:
        p.join()
        
     
    f.close()

    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()
   


if __name__=="__main__":
    line = "['women', 'http://www.flipkart.com/watches/women?otracker=hp_nmenu_sub_women_0_Watches', 'Watches', 'http://www.flipkart.com/watches/watch-accessories/pr?sid=r18,trt', 'Watch Accessories']"

    #main(line) 
    mainthread()
