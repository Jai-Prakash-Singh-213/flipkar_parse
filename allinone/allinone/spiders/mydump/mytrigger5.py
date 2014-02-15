from multiprocessing import Process, Queue
import code7_allinone5
import subprocess

num_fetch_threads = 20
enclosure_queue = Queue()


def main2(i, q):
    while True:
        pth_list2 = q.get()
        code7_allinone5.main(pth_list2)   

def main():
    #f = open("availdirthree")
    #dirthree = f.read().strip()
    #f.close()

    dirthree = "dirthree08022014"

    output = subprocess.check_output(["find", dirthree + "/women/",  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")
    
    val = len(pth_list)/20

    for i in range(num_fetch_threads):
        worker = Process(target=main2, args=(i, enclosure_queue,))
        worker.start()

    for l in range(val, len(pth_list), val):
        pth_list2 = pth_list[:l]
        enclosure_queue.put(pth_list2)
        pth_list = pth_list[l:]


    print '*** Main thread waiting'
    enclosure_queue.join()

    if l < len(pth_list):
        code7_allinone5.main(pth_list[l:])

  
    print '*** Done'


if __name__=="__main__":
    main()

