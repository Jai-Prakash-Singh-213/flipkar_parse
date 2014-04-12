import phan_proxy
from bs4 import BeautifulSoup
from lxml import html
import req_proxy
import time
from threading import Thread
from Queue import Queue
import logging
import os 


logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
 
num_fetch_threads = 100
enclosure_queue = Queue()




def main2(mn_sbml_sbml, filename):
    menu = mn_sbml_sbml[0]
    submenulink = mn_sbml_sbml[1]
    submenutitle =  mn_sbml_sbml[2]
 
    page = req_proxy.main(submenulink)
    
    soup = BeautifulSoup(page)
    
    tag_cat = soup.find("div", attrs={"class":"nav-section first-section"})

    tag_cat_link = []

    if tag_cat is not None:
        tag_cat_link = tag_cat.find_all("a")

    f = open(filename, "a+")

    for l in tag_cat_link:
        cattitle = str(l.get("title")).strip()
	catlink = "%s%s" %("http://www.flipkart.com", str(l.get("href")).strip())
        print >>f, [menu, submenulink, submenutitle, catlink, cattitle]
        logging.debug([menu, submenulink, submenutitle, catlink, cattitle])

    f.close()




def mainthread2(i, q):
    for mn_sml_smt, filename in iter(q.get, None):
        try:

            main2(mn_sml_smt, filename)
            logging.debug([mn_sml_smt, filename])

        except:
            f2 = open("page1_first_error_filpkart.txt", "a+")
            print >>f2, mn_sml_smt
            f2.close()

        time.sleep(2)
        q.task_done()

    q.task_done()
       



def mainthread(menu_subl_subt):
    f = open("to_extractfilpkart")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "f_mn_smnl_smnt_ctl_ctl.txt")

    procs = []

    for i in range(num_fetch_threads):
        procs.append(Thread(target=mainthread2, args=(i, enclosure_queue,)))
        #procs.append(multiprocessing.Process(target=part_threading2, args=(i, enclosure_queue,)))
	#worker.setDaemon(True)
	procs[-1].start()

    for mn_sml_smt in menu_subl_subt:
        enclosure_queue.put((mn_sml_smt, filename))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'

    for p in procs:
        enclosure_queue.put(None)

    enclosure_queue.join()

    for p in procs:
        p.join()

    print "Finished everything...."




def main():
    directory = "dirflipkart%s" %(time.strftime("%d%m%Y"))

    try:
        os.makedirs(directory)
    except:
        pass

    f = open("to_extractfilpkart", "w+")
    f.write(directory)
    f.close()

    f2 = open("extractedflipkart", "a+")
    f2.write(directory)
    f2.close()
    
    link = "http://www.flipkart.com/"
    driver = phan_proxy.main(link)
    
    page = driver.page_source
 
    #soup = BeautifulSoup(page, "html.parser")
    soup = BeautifulSoup(page)
    tag_menu = soup.find_all("li", attrs={"class":"menu-l0  "})


    menu_subl_subt = []

    for menu in tag_menu:
        menutitle = menu.get("data-key")
        submenu = menu.find_all("li", attrs={"class":"heading"})
	submenu_new = menu.find_all("li", attrs={"class":"new-heading"})

	submenu.extend(submenu_new)

	for l in submenu:
	    submenutitle = str(l.get_text()).strip()
	    submenulink = "%s%s" %("http://www.flipkart.com", str(l.a.get("href")).strip())

	    menu_subl_subt.append([menutitle, submenulink, submenutitle])
    
    driver.delete_all_cookies()
    driver.quit()
    
    mainthread(menu_subl_subt)



if  __name__=="__main__":
    main()

    #mn_sbml_sbml = ["more-stores",  "http://www.flipkart.com//sports-fitness/outdoor-adventure/motorsports/pr?sid=dep,nlv,2hj&otracker=hp_nmenu_sub_more-stores_0_Motorsports",  "Motorsports"]
    #mn_sbml_sbml = ["baby-kids",  "http://www.flipkart.com/kids-clothing?otracker=hp_nmenu_sub_baby-kids_0_Kids%20Clothing",  "Kids Clothing"]
    #main2(mn_sbml_sbml)
