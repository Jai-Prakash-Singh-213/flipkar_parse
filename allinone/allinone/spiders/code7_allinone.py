#!/usr/bin/env python 

import subprocess
import multiprocessing
import time
import code6_allinone
import logging

mp_num_fetch_threads = 20
mp_enclosure_queue = multiprocessing.Queue()



logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
		                        )

def main2(i, q):
    while True:
        pth = q.get()
	logging.debug(pth)
        code6_allinone.main(pth)
        time.sleep(2)
        #q.task_done()
    
    

def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()

    output = subprocess.check_output(["find", dirthree + "/women/bags-wallets-belts",  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    for i in range(mp_num_fetch_threads):
        worker = multiprocessing.Process(target=main2, args=(i, mp_enclosure_queue,))
	#worker.setDaemon(True)
	worker.start()

    for pth in pth_list:
         mp_enclosure_queue.put(pth)
         


    


if __name__=="__main__":
    main()





