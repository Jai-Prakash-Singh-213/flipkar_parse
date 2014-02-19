#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
import code6_allinone2
import logging
import os
from threading import Thread
from Queue import Queue
import time


num_fetch_threads = 30
enclosure_queue = Queue()



logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                                        )

def main2(i, q):
    while True:
        filename, brandname, catname, l = q.get()
        logging.debug((filename, brandname, catname, l))
        code6_allinone2.main(filename, brandname, catname, l)
        time.sleep(2)
        q.task_done()


def main(pth_list):


    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()



    for pth  in pth_list:
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
        
        f.close()


    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'

