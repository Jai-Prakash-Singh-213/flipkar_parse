#!/usr/bin/env python
import subprocess 
import multiprocessing
from multiprocessing import Process
#import page4_multiprocess
import page4_multiprocess2
import profile

# page4.py   page4_multiprocess.py page4_filedivision.py
#            page4_multiprocess2.py

def main2(pth_list):
    #page4_multiprocess.main(pth_list)
    page4_multiprocess2.main(pth_list)



def main():
    f = open("availdirthree.txt")
    dirthree = f.read().strip()
    f.close()

    output = subprocess.check_output(["find", dirthree,  "-name",  "*.csv"])
    pth_list = output.strip().split("\n")

    length =  len(pth_list)

    for i  in xrange(200,  length, 200):
        startval = i - 200
        worker = Process(name = i, target=main2, args=(pth_list[startval : i],))        
        #worker.daemon = True
	worker.start()
	worker.join()

    if i < length:
        worker = Process(name = i, target=main2, args=(pth_list[i : ],))
        #worker.daemon = True
	worker.start()
        worker.join()

    print "Finished everything...."
    print "num active children:", multiprocessing.active_children()


if __name__=="__main__":
    profile.run("main()")
