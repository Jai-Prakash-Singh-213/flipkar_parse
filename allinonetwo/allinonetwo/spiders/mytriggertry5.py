#!/usr/bin/env python 
import code7_allinonetry5
from multiprocessing import Process, Queue
import multiprocessing
import logging
import subprocess
import profile
import threading 
from threading import Thread
from Queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

cd72 = code7_allinonetry5.main

num_fetch_threads = multiprocessing.cpu_count()*4
enclosure_queue = multiprocessing.Queue()
enclosure_queue = multiprocessing.JoinableQueue()

#enclosure_queue = Queue()
enqp = enclosure_queue.put_nowait




def main2(i, q):
    qget = q.get
    for pth_list2 in iter( qget, None ):
        cd72(pth_list2)
        qtaskdone = q.task_done

    qtaskdone()

        


def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()

    output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    length = len(pth_list)

    val = length/10

    val1 = val * 0
    val2 = val * 1


    pth_list = pth_list[val1 : val2]

    length = len(pth_list) / 10

    val = length / 10
    mod = length % 10    


    procs = []


    for i in xrange(num_fetch_threads):
        procs.append(Process(name = str(i), target=main2, args=(i, enclosure_queue,)))
        procs[-1].daemon = True
        procs[-1].start()
        #worker = Thread(target=main2, args=(i, enclosure_queue,))
        #worker.setDaemon(True)
        #worker.start()


    for l in xrange(val, length, val):
        enqp( pth_list[:l] )
        pth_list = pth_list[l:]


    if mod:
        enqp(pth_list[mod:])


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
    profile.run('main()')
    #main()
