import code7_allinone2
from multiprocessing import Process, Queue
import multiprocessing
import logging
import subprocess


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

num_fetch_threads = 50
enclosure_queue = multiprocessing.Queue()



def main2(i, q):
    while True:
        pth_list2 = q.get()
        logging.debug(('Starting:', multiprocessing.current_process().name))
        code7_allinone2.main(pth_list2)



def main():
    f = open("availdirthree")
    dirthree = f.read().strip()
    f.close()

    #output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    output = subprocess.check_output(["find", dirthree + "/women/",  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    length = len(pth_list)

    val = length/10

    mod = length % 10


    for i in range(num_fetch_threads):
        worker = Process(name = str(i), target=main2, args=(i, enclosure_queue,))
        #worker.setDaemon(True)
        worker.start()

    for l in range(val, length, val):
        pth_list2 = pth_list[ :l]
        enclosure_queue.put(pth_list2)
        pth_list = pth_list[l:]


    if mod != 0:
        code7_allinone2.main(pth_list[mod:])



if __name__=="__main__":
    main()
