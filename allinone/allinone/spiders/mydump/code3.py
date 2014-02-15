import urll_proxy
from bs4 import BeautifulSoup 
import multiprocessing
import os
from Queue import Queue
from threading import Thread
import time

num_fetch_threads = 10
enclosure_queue = Queue()



def main3(i, q):
    while True:
        fpth, l = q.get()

        fpath_list = fpth.split("/")
        l_list = l.split("/")

        page = urll_proxy.main(l)
	html = page.read()
        soup = BeautifulSoup(html)

	tag_ul = soup.find("ul", attrs={"id":"brand"})
        
        try:
            tag_a = tag_ul.find_all("a")
	
	    for l2 in tag_a:
	        try:
	            if l2.get("href"):
	                brdl =  "http://www.flipkart.com" + l2.get("href")
	                brdn =  l2.span.get_text()
	                brdc =  l2.find("span", attrs={"class":"count"}).get_text()
                    
		        fdir = '/'.join(fpath_list[:-1]) + "/" + l_list[3]
                    
		        if not os.path.exists(fdir):
		            os.makedirs(fdir)

                        fhomepage = fdir + "/" + "8".join(l_list[3:-1]) + "8.csv"

                        f = open(fhomepage, "a+")
		        date = time.strftime("%H:%M:%S")
		        print  >>f, ','.join([date, brdn, brdc, brdl])
		        f.close()
                            
                        f2 = open(fpath_list[0] + "/availtoscroll", "a+")
                        print >>f2, fdir
                        f2.close()

		    else:
		        pass
	        except:
	            pass
        except:
            pass


        

def main2(fpth):
    

    for i in range(num_fetch_threads):
        worker = Thread(target=main3, args=(i, enclosure_queue,))
	#worker.setDaemon(True)
	worker.start()

    f = open(fpth)

    for l in f:
        enclosure_queue.put((fpth, l))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'
        



def main():

    starttime =  time.strftime("%H:%M:%S")

    dict_brand_to_extract = ['todaydir06022014/baby-kids/brand_to_extract.txt',
                             'todaydir06022014/men/brand_to_extract.txt',
			     'todaydir06022014/books-media/brand_to_extract.txt',
			     'todaydir06022014/more-stores/brand_to_extract.txt',
			     'todaydir06022014/electronics/brand_to_extract.txt',
			     'todaydir06022014/women/brand_to_extract.txt',
			     'todaydir06022014/home-kitchen/brand_to_extract.txt']

    for fpth in dict_brand_to_extract:
        p = multiprocessing.Process(target=main2, args=(fpth,))
	p.start()
    
    finishedtime =  time.strftime("%H:%M:%S")
    
    print (starttime, finishedtime)
        
    
if __name__=="__main__":
    main()    
