import multiprocessing
import os
import sys


def fun1():
    currentdir = os.getcwd()

    #paith_appaned = currentdir + "/project2/project2/spiders/settings.py"
    #sys.path.append(path_appaned)

    requireddir = currentdir + "/code3_scrapy_thread.py"
    command = " python " + requireddir

    os.system(command)




def fun2():
    currentdir = os.getcwd()
    
    path_appaned = currentdir + "/project2/project2/spiders/settings.py"
    sys.path.append(path_appaned)
    
    requireddir = currentdir + "/project2/project2/spiders/code3_scrapy_thread.py"
    command = " python " + requireddir
    
    os.system(command)


def fun3():
    currentdir = os.getcwd()

    path_appaned = currentdir + "/project3/project3/spiders/settings.py"
    sys.path.append(path_appaned)

    requireddir = currentdir + "/project3/project3/spiders/code3_scrapy_thread.py"
    command = " python " + requireddir

    os.system(command)






def main():

    p1 = multiprocessing.Process(target=fun1)
    p2 = multiprocessing.Process(target=fun2)
    p3 = multiprocessing.Process(target=fun3)    


    p1.start()
    p2.start()
    p3.start()

if __name__=="__main__":
    main()
