import urll_proxy
from bs4 import BeautifulSoup 
import os
import re
import time
import shutil

from Queue import Queue
from threading import Thread
import time
import threading

num_fetch_threads = 100

enclosure_queue = Queue() 




def main4(todatdir_menu, sub_link):
    
    page = urll_proxy.main(str(sub_link).strip())
    html = page.read()
    soup = BeautifulSoup(str(html))
    print page.geturl()
    page.close()

    link_split = sub_link.strip().split("/")
    #print menu + "__" + "__".join(link_split[3:-1])

    #shutil.rmtree(todatdir_menu)

    if re.search(r'[\w]*~brand', link_split[-2]):

        filename = todatdir_menu + "/sublink_alreadybrand.txt"
        f = open(filename, "a+")
        print >>f , sub_link
        f.close()

    elif soup.find_all("ul", attrs={"id":"brand"}):

        filename = todatdir_menu + "/sublink_brand_to_extract.txt"
        f = open(filename, "a+")
        print >>f , sub_link
        f.close()

    else:
        print "pass from main4"

    

def main3(todatdir_menu, tag_nav):
    
    for l2 in tag_nav: 
       try:
           sub_link =  "http://www.flipkart.com" + str(l2.get("href"))
           t = threading.Thread(target=main4, args=(todatdir_menu, sub_link))
           t.start()

       except:
           pass

 
        

def main2(i, q):
    while True:
        todaydir, menu, l = q.get()
 
        page = urll_proxy.main(str(l).strip())
        html = page.read()
        soup = BeautifulSoup(str(html))
        print page.geturl()
        page.close()

        link_split = l.strip().split("/")
        #print menu + "__" + "__".join(link_split[3:-1])

        todatdir_menu = todaydir + "/" + menu

        #shutil.rmtree(todatdir_menu)

        if not os.path.exists(todatdir_menu):
            os.makedirs(todatdir_menu)

        if re.search(r'[\w]*~brand', link_split[-2]):

            filename = todatdir_menu + "/alreadybrand.txt"

            f = open(filename, "a+")
            print >>f , l
            f.close()

        elif soup.find_all("ul", attrs={"id":"brand"}):

            filename = todatdir_menu + "/brand_to_extract.txt"
            f = open(filename, "a+")
            print >>f , l
            f.close()

        elif soup.find_all("div", attrs={"class":"nav-section-cat-list"}):
   
            tag_nav = soup.find_all("div", attrs={"class":"nav-section-cat-list"})

            main3(todatdir_menu, tag_nav[0])

        else:
            print "pass"

        time.sleep(2)
        q.task_done()



    

def main():

    #startime = time.strftime("%I%M%S")
    startime = time.strftime("%d%m%Y")

    todaydir = "todaydir" + startime

    if not os.path.exists(todaydir):
        os.makedirs(todaydir)

    f = open("code1_dict_menu_link.txt")
    
    dict_menu_link = eval(f.read())
    f.close()
    
    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        #worker.setDaemon(True)
        worker.start()


    for menu, allink in dict_menu_link.items():
        for l in allink:
            enclosure_queue.put((todaydir, menu, l))
        

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'
 
         



if __name__=="__main__":
    main()
