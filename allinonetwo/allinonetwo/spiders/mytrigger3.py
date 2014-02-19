import code7_allinone3
from multiprocessing import Process, Queue
import multiprocessing
import logging
import subprocess
import profile

cd73 = code7_allinone3.main

num_fetch_threads = 20
enclosure_queue = Queue()
enqpt = enclosure_queue.put



def main2(i, q):
    qet =  q.get
    while True:
        cd73(qet())


def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()

    #output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    output = subprocess.check_output(["find", dirthree + "/women/",  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    length = len(pth_list)

    val = length / 50

    mod = length % 50

    for i in range(num_fetch_threads):
        worker = Process(name = i, target = main2, args = (i, enclosure_queue,))
        #worker.daemon = True
        worker.start()

    for l in xrange(val, length, val):
        enqpt(pth_list[:l])
        pth_list = pth_list[l:]


    if mod != 0:
        enqpt(pth_list[mod:])


if __name__=="__main__":
    profile.run("main()")
