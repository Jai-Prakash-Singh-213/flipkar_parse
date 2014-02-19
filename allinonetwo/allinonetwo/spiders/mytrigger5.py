import code7_allinone5
from multiprocessing import Process, Queue
import multiprocessing
import logging
import subprocess
import profile

cd75 = code7_allinone5.main

num_fetch_threads = 10
enclosure_queue = Queue()
enqpt = enclosure_queue.put



def main2(i, q):
    qet =  q.get
    while True:
        cd75(qet())


def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()

    output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    length = len(pth_list)


    for i in xrange(num_fetch_threads):
        worker = Process(name = i, target = main2, args = (i, enclosure_queue,))
        #worker.daemon = True
        worker.start()

    for l in xrange(10, length, 10):
        enqpt(pth_list[:l])
        pth_list = pth_list[l:]


    try:
        enqpt(pth_list[l:])
    except:
        pass


if __name__=="__main__":
    profile.run("main()")
