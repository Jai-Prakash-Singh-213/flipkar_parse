#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
import code6_allinonetry5
import logging
import os
from threading import Thread
from Queue import Queue
import time


cde65 = code6_allinonetry5.main

num_fetch_threads = 20
enclosure_queue = Queue()
enqp = enclosure_queue.put_nowait




def main2(i, q):
    qdone = q.task_done

    for filename, brandname, catname, l in iter( q.get, None ):
        cde65(filename, brandname, catname, l)
        qdone()

    qdone()


def main(pth_list):

    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()


    for pthmain  in pth_list:

        pth = pthmain.split("/")

        dirfour = "dirfour_try5_"  +  pth[0].strip()[-8:]
        dirfour = dirfour + "/" +  "/".join(pth[1:-1])

        catname = pth[-2].split("-xx-")[-2].strip()

        brandname = pth[-1][:-3]

        filename = dirfour + "/" + pth[-1].strip()

        try:
            os.makedirs(dirfour)
        except:
            pass
        
        f = open(pthmain)

                              
        for l in f:
            l = l.strip()
            enqp((filename, brandname, catname, l))

        f.close()

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'

