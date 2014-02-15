#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
import code6_allinone3
import logging
from Queue import Queue
from threading import Thread
import os 

num_fetch_threads = 150
enclosure_queue = Queue()


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )

def main2(i, q):
    while True:
        filename, brandname, catname, l = q.get()
        code6_allinone3.main(filename, brandname, catname, l)
        time.sleep(2)
        q.task_done()
    
    

def main():
    #f = open("availdirthree")
    #dirthree = f.read().strip()
    #f.close()

    dirthree = "dirthree08022014"

    output = subprocess.check_output(["find", dirthree + "/women/",  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()


    for pth in pth_list:
        dirfour = "dirfour_2_"  +  pth.split("/")[0].strip()[-8:]
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
            enclosure_queue.put((filename, brandname, catname, l))

    print '*** Main thread waiting'
    enclosure_queue.join()
    f.close()
    print '*** Done'         


    


if __name__=="__main__":
    main()





