#!/usr/bin/python 


import urll_proxy
import os 
from bs4 import BeautifulSoup
import time 
import sys
from Queue import Queue
from threading import Thread

num_fetch_threads = 20
enclosure_queue = Queue()


def main2(i, q):
    while True:
        filename, brandname, catname, l = q.get()
        
        item_link = l
        page = urll_proxy.main(l)
        soup = BeautifulSoup(page)
        page.close()

        tag_h1 = soup.find("h1", attrs={"itemprop":"name"})
        item_title = str(tag_h1.get_text()).strip()

        try:
           tag_colour = soup.find("div", attrs={"class":"line extra_text bmargin10"})
           item_clour = str(tag_colour.get_text()).strip()
        except:
           item_clour = " No more colour"

        tag_img = soup.find("img", attrs={"id":"visible-image-small"})
        item_image = tag_img.get("src")

        tag_price = soup.find("span", attrs={"class":"fk-font-verybig pprice fk-bold"})
        item_price = str(tag_price.get_text()).strip()

        try:
           tag_mrp = soup.find("span", attrs={"id":"fk-mprod-list-id"})
           item_mrp = str(tag_discount.get_text()).strip()
        except:
           item_mrp = item_price


        tag_seller = soup.find("a", attrs={"class":"pp-seller-badge-name fk-bold"})
        item_seller = str(tag_seller.get_text()).strip()
         
        try:
            tag_sku = soup.find("a", attrs={"class":"btn btn-orange btn-buy-big fk-buy-now fkg-pp-buy-btn"})
            sku = str(tag_sku.get("href")).split("=")[-1].strip()
        except:
            sku = "not sku defined"

        size = []
        try:
            tag_multiselect = soup.find_all("div", attrs={"class":"multiselect-item"})
            
            for l in tag_multiselect:
                try: 
                    size.append(l.get_text())
                except:
                    pass
        except:
            pass

        if not size:
            size.append("No size defined")
        
        size2 = ' '.join(size) 

        del size[:]
        del size

        date = str(time.strftime("%d:%m:%Y")).strip()

        f = open(filename,"a+")
        print >>f, ','.join([date, catname, brandname,  item_title, item_price, 
                             item_image, item_clour, item_mrp, item_seller, item_link, sku, size2])
        f.close()



def main(pth):
    dirfour = "dirfour"  +  pth.split("/")[0].strip()[-8:]
    dirfour = dirfour + "/" +  "/".join(pth.split("/")[1:-1])

    catname = pth.split("/")[-2].split("-xx-")[1].strip()

    brandname = pth.split("/")[-1][:-3]

    filename = dirfour + "/" + pth.split("/")[-1].strip()

    if not os.path.exists(dirfour):
        os.makedirs(dirfour)
    
    f = open(pth)

    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()
   
    for l in f:
        l = l.strip()
        enclosure_queue.put((filename, brandname, catname, l))
	

    print '*** Main thread waiting'
    enclosure_queue.join()
    print '*** Done'



if __name__=="__main__":
    pth = "dirthree08022014/baby-kids/baby-care/baby-care-xx-maternity-care-xx-bnbcbl/Farlin.csv"

    main(pth)
