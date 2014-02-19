#!/usr/bin/env python 
import profile
import subprocess
from scrapy import cmdline
import multiprocessing
from multiprocessing import Process
import time

# page4.py   page4_multiprocess.py page4_filedivision.py
#            page4_multiprocess2.py


num_fetch_threads = multiprocessing.cpu_count()*20
enclosure_queue = multiprocessing.JoinableQueue()

enqp = enclosure_queue.put_nowait

def main2(i, q):
    qget = q.get
    qtaskdone = q.task_done
    cexc = cmdline.execute     

    for pth in iter( qget, None ):
        cexc(['scrapy',  'runspider', 'page4.py',   '-a',  'pth=%s' %(pth)])
        time.sleep(i + 2)
        qtaskdone()

    qtaskdone()



def main(pth_list):


    procs = []

    for i in xrange(num_fetch_threads):
        procs.append(Process(name = str(i), target=main2, args=(i, enclosure_queue,)))
        #procs[-1].daemon = True
        procs[-1].start()

    for pth in pth_list:
        enqp(pth)
        

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'

    for p in procs:
        enqp( None )

    enclosure_queue.join()


    for p in procs:
        p.join()

    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()


if __name__=="__main__":
    profile.run("main()")

