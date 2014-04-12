#!/usr/bin/env python 
import ast
import phan_proxy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from urlparse import urlparse
from lxml import html
from bs4 import BeautifulSoup
import logging
import time
import multiprocessing
import os 


logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

num_fetch_threads = 100
enclosure_queue = multiprocessing.JoinableQueue()




def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")

    except WebDriverException:
        pass




def driver_scroller(driver):
    height = 0
    loop = True

    while loop is True:
        logging.debug("scrolling...")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 15).until( ajax_complete,  "Timeout waiting for page to load")
        time.sleep(2)
        heightnow = driver.execute_script("return $(document ).height();")
        WebDriverWait(driver, 15).until( ajax_complete,  "Timeout waiting for page to load")
        time.sleep(2)
        
        if heightnow == height:
            loop = False

        else:
            height = heightnow
            loop = True

    return driver




def sub_scroller(driver):
    loop = True
    while loop is True:
        try:
            print "clicking..."
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[5]/div[3]").click()

            WebDriverWait(driver, 15).until( ajax_complete,  "Timeout waiting for page to load")
            time.sleep(1)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            WebDriverWait(driver, 15).until( ajax_complete,  "Timeout waiting for page to load")
            time.sleep(1)

        except WebDriverException:
            return driver




def main(line, directory):

    line = ast.literal_eval(line)
    
    line = map(str.strip, line)
    menu = line[0]
    submnlink = line[1]
    submntitle = line[2]
    catlink = line[3]
    cattitle = line[4]
    brandlink = line[-2]
    brandtitle = line[-1]
    start = brandtitle.find("(")
    brandtitle = brandtitle[:start].strip()

    dirtwo = "%s/%s/%s/%s/%s" %(directory, menu, submntitle, cattitle, brandtitle)

    try:
        os.makedirs(dirtwo)

    except:
        pass

    filedoc = "%s/%s.doc" %(dirtwo, brandtitle)
    filedocx = "%s/%s.docx" %(dirtwo, brandtitle)

    f2 = open(filedoc, "a+")
    f3 = open(filedocx, "a+")

    driver = phan_proxy.main(brandlink)
    
    driver = driver_scroller(driver)

    driver = sub_scroller(driver)

    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")
    
    tag_product = soup.find("div", attrs={"id":"products"})
    
    tag_product_a = tag_product.find_all("a", attrs={"class":"pu-image fk-product-thumb "})


    for al in tag_product_a:
        itemlink = "%s%s" %("http://www.flipkart.com", str(al.get("href").strip()))
        print >>f2, [menu, submnlink, submntitle, catlink, cattitle, brandlink, brandtitle, itemlink]
        print >>f3, itemlink
	print [menu, submnlink, submntitle, catlink, cattitle, brandlink, brandtitle, itemlink]

    driver.delete_all_cookies()
    driver.quit()
    
    f2.close()
    f3.close()




def mainthread2(i, q):
    for line, directory in iter(q.get, None):
        try:

            main(line, directory)
            logging.debug((line, directory))

        except:
            f2 = open("page2_seconf_scrolling_error_filpkart.txt", "a+")
            print >>f2, line
            f2.close()

        time.sleep(2)
        q.task_done()

    q.task_done()




def mainthread():
    f = open("to_extractfilpkart")
    directory = f.read().strip()
    f.close()

    filename = "%s/%s" %(directory, "f_mn_smnl_smnt_ctl_ctl_bl_bt.txt")

    f = open(filename)

    procs = []

    for i in range(num_fetch_threads):
        #procs.append(Thread(target=mainthread2, args=(i, enclosure_queue,)))
        procs.append(multiprocessing.Process(target=mainthread2, args=(i, enclosure_queue,)))
        #worker.setDaemon(True)
        procs[-1].start()

    for line in f:
        enclosure_queue.put((line, directory))

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'

    for p in procs:
        enclosure_queue.put(None)

    enclosure_queue.join()

    for p in procs:
        p.join()


    f.close()




if __name__=="__main__":
    line = "['men', 'http://www.flipkart.com/watches/men?otracker=hp_nmenu_sub_men_1_Watches', 'Watches', 'http://www.flipkart.com/watches/watch-accessories/pr?sid=r18,trt', 'Watch Accessories', 'http://www.flipkart.com/watches/watch-accessories/pr?p%5B0%5D=facets.brand%255B%255D%3DEssart&sid=r18%2Ctrt', 'Essart (34)']"
 
    directory = "dirflipkart09032014"
    #main(line, directory)

    mainthread()

