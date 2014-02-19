#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
<<<<<<< HEAD
import code6_allinone3
import logging
from Queue import Queue
from threading import Thread
import os 
from multiprocessing import Process, Queue


num_fetch_threads = 50
#enclosure_queue = Queue()

mp_enclosure_queue = multiprocessing.Queue()


=======
import code6_allinone2
import logging

mp_num_fetch_threads = 5
mp_enclosure_queue = multiprocessing.Queue()



>>>>>>> a0099e0a269d70bd87a7493005e633efedffbbb1
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )

def main2(i, q):
    while True:
<<<<<<< HEAD
        filename, brandname, catname, l = q.get()
        code6_allinone3.main(filename, brandname, catname, l)
=======
        pth = q.get()
	logging.debug(pth)
        code6_allinone.main(pth)
>>>>>>> a0099e0a269d70bd87a7493005e633efedffbbb1
        time.sleep(2)
        #q.task_done()
    
    

<<<<<<< HEAD
def main(pth_list):

    for i in range(num_fetch_threads):
        #worker = Thread(target=main2, args=(i, enclosure_queue,))
        #worker.setDaemon(True)
        worker = multiprocessing.Process(target=main2, args=(i, mp_enclosure_queue,))
        worker.start()


    for pth in pth_list:
        dirfour = "dirfour_3_"  +  pth.split("/")[0].strip()[-8:]
        dirfour = dirfour + "/" +  "/".join(pth.split("/")[1:-1])

        catname = pth.split("/")[-2].split("-xx-")[-2].strip()

        brandname = pth.split("/")[-1][:-3]

        filename = dirfour + "/" + pth.split("/")[-1].strip()

        try:
            if not os.path.exists(dirfour):
                os.makedirs(dirfour)
        except:
            pass

        f = open(pth)

        for l in f:
            l = l.strip()
            #enclosure_queue.put((filename, brandname, catname, l))
            mp_enclosure_queue.put((filename, brandname, catname, l))


    print '*** Main thread waiting'
    #enclosure_queue.join()
    f.close()
    print '*** Done'         

    
=======
def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()
      
    #output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    val = len(pth_list)/5
    val1 = val*2
    val2 = val*3

    pth_list = pth_list[val1:val2]

    #for i in range(mp_num_fetch_threads):
    #    worker = multiprocessing.Process(target=main2, args=(i, mp_enclosure_queue,))
	#worker.setDaemon(True)
    #	worker.start()

    #for pth in pth_list:
    #     mp_enclosure_queue.put(pth)
         
    for pth in pth_list:
        code6_allinone2.main(pth)

    


if __name__=="__main__":
    main()





>>>>>>> a0099e0a269d70bd87a7493005e633efedffbbb1
