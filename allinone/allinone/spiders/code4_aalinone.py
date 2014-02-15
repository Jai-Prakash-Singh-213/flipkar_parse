#!/usr/bin/python 
import subprocess
from Queue import Queue
import multiprocessing
import time
import logging
from threading import Thread
import os
import code5_allinone
import sys


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

mp_num_fetch_threads = 5
mp_enclosure_queue = multiprocessing.Queue()

num_fetch_threads = 20
enclosure_queue = Queue()


def main3(i2, q2):
    while True:
        dirthree, line = q2.get()

	brandname = line.split(",")[2].strip()
	brandlink = line.split(",")[4].strip()

	logging.debug((dirthree, brandname, brandlink))

        code5_allinone.main(dirthree, brandname, brandlink)

	q2.task_done()

        


def main2(i, q):
    while True:
        pth = q.get()
        logging.debug(pth)

        dirthree = "dirthree_men_" + pth.split("/")[0][-8:] + "/" + "/".join(pth.split("/")[1:-1]) + "/" + pth.split("/")[-1][:-4]

        f = open("availdirthree","w")
        print >>f,  "dirthree_men_" + pth.split("/")[0][-8:]
        f.close()

        if not os.path.exists(dirthree):
            os.makedirs(dirthree)


        f = open(pth)

        for i in range(num_fetch_threads):
            worker2 = Thread(target=main3, args=(i, enclosure_queue,))
            worker2.setDaemon(True)
            worker2.start()



        for line in f:
            enclosure_queue.put((dirthree, line))

        print '*** Main thread waiting'
        enclosure_queue.join()
        print '*** Done'




def main():

    startime =   time.strftime("%H:%M:%S")

    f = open("availdirtwo")
    dirtwo = f.read().strip()
    f.close()

    #output = subprocess.check_output(["find",  dirtwo , "-name",  "*.csv"])
    output = subprocess.check_output(["find",  dirtwo + "/men/",  "-name",  "*.csv"])
    output = output.strip().split("\n")

    #print output
    #sys.exit()

    #output2 = subprocess.check_output(["find",  dirtwo+"/men/", "-name",  "*.csv"])
    #output2 = output2.strip().split("\n")

    #output.extend(output2)
    #print output
    #sys.exit()

    for i in range(mp_num_fetch_threads):
        worker = multiprocessing.Process(target=main2, args=(i, mp_enclosure_queue,))
        #worker.setDaemon(True)
        worker.start()

    for pth in output:
        mp_enclosure_queue.put(pth)


    finshtime = time.strftime("%H:%M:%S")

    print (startime, finshtime)



if __name__=="__main__":
    main()
                 
