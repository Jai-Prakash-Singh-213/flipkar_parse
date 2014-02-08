#!/usr/bin/python 
import subprocess
import multiprocessing
import os
from Queue import Queue
from threading import Thread
import time
import urll_proxy
from bs4 import BeautifulSoup
import time
import sys
 

num_fetch_threads = 20
enclosure_queue = Queue()

def main3(i, q):
    while True:
        dirtwo, l = q.get()
	dirtwo = dirtwo + "/" + l.split("/")[3]

       
        if not os.path.exists(dirtwo):
            os.makedirs(dirtwo)

	filename = dirtwo + "/" + "-xx-".join(l.split("/")[3:-1]) + "-xx-bnbcbl.csv"

	f = open(filename, "a+")
        
	page = urll_proxy.main(l)
        soup = BeautifulSoup(page)
	page.close()

	tag_ul = soup.find("ul", attrs={"id":"brand"})
        tag_a = tag_ul.find_all("a")

	pos = 1
	for l in tag_a:
	    if l.get("href"):
	        brand_link = "http://www.flipkart.com"+str(l.get("href")).strip()
	        brand_name = str(l.span.get_text()).strip()
	        brand_count = str(l.find("span", attrs={"class":"count"}).get_text()).strip("()")
	        #print brand_link, brand_name, brand_count
		date = str(time.strftime("%d:%m:%Y"))
		print >>f, ','.join([date, str(pos), brand_name, brand_count, brand_link])
		pos = pos+1

	    
	
def main2(pth):

    dirtwo = "dirtwo" + pth.split("/")[0][:-8]

    f = open("availdirtwo", "a+")
    print >>f, dirtwo
    f.close()
    
    sub_dir =  pth.split("/")[1]

    dirtwo = dirtwo + "/" + sub_dir

    if not os.path.exists(dirtwo):
        os.makedirs(dirtwo)

    for i in range(num_fetch_threads):
        worker = Thread(target=main3, args=(i, enclosure_queue,))
	#worker.setDaemon(True)
	worker.start()

    f = open(pth)

    for l in f:
        enclosure_queue.put((dirtwo, l))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'


    

   
def main():
    f = open("availdir")
    dirone = f.read().strip()
    f.close()

    output = subprocess.check_output(["find",  dirone,  "-name",  "extract_brand_from_it.txt"])
    output =  output.strip().split("\n")


    for pth in output:
        p = multiprocessing.Process(target=main2,  args=(pth,))
	p.start()

    

if __name__=="__main__":
    main()
