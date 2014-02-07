import code1_allinone
import multiprocessing
import os
import time 
from Queue import Queue
from threading import Thread
import time
import urll_proxy
from bs4 import BeautifulSoup
import threading

num_fetch_threads = 20
enclosure_queue = Queue()



def mystrip(x):
    return x.strip()



def main4(directory, sub_link):
    
    page = urll_proxy.main(sub_link)
    html = page.read()
    soup = BeautifulSoup(html)
    page.close()
 
    link_split = sub_link.split("/")[-2]

    if re.search(".*~brand", link.split("/")[-2]):
        filename = directory + "/sub_link_its_already_brand_.txt"
	f = open(filename, "a+")
	print >>f, link
	f.close()

    if soup.find("ul", attrs={"id":"brand"}):
        filename = directory + "/sublink_extract_brand_from_it.txt"
	f = open(filename, "a+")
	print >>f, link
	f.close()


    
def main3(i, q):
    while True:
        directory, link = q.get()

        page = urll_proxy.main(link)
        html = page.read()
        soup = BeautifulSoup(html)
        page.close()

	if soup.find("ul", attrs={"id":"brand"}):
	    filename = directory + "/extract_brand_from_it.txt"
	    f = open(filename, "a+")
	    print >>f, link
	    f.close()

	link_split = link.split("/")[-2]
        
	if re.search(".*~brand", link.split("/")[-2]):
	    filename = directory + "/its_already_brand_.txt"
	    f = open(filename, "a+")
	    print >>f, link
	    f.close()

        tag_nav = soup.find("div", attrs={"class":"nav-section-cat-list"})

	if tag_nav:
	    for  l in tag_nav:
	        try:
		    sub_link = "http://www.flipkart.com" + l.get("href")
	            t = threading.Thread(target=main4, args=(directory, sub_link))
		    t.start()
	        except:
	            pass




def main2(dte, menu, links_list):
    directory = dte + "/" + menu

    if not os.path.exists(directory):
        os.makedirs(directory)
     
    for i in range(num_fetch_threads):
        worker = Thread(target=main3, args=(i, enclosure_queue,))
	#worker.setDaemon(True)
	worker.start()

    for link in links_list:
        enclosure_queue.put((directory, link))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'
    
        



def main():
    #dict_menu_links = code1_allinone.main()
    
    #f = open("dict_menu_links", "a+")
    #print >>f, dict_menu_links
    #f.close()

    dat = time.strftime("dir%d%m%Y")
    
    f = open("availdir", "a+")
    print >>f, dat
    f.close()

    f = open("dict_menu_links")
    dict_menu_links = eval(f.read().strip())
    f.close()
 
    for menu, links_list in dict_menu_links.items():
        p = multiprocessing.Process(target=main2, args=(dte, menu, links_list))
	p.start()

    


if __name__=="__main__":
    main()
    
