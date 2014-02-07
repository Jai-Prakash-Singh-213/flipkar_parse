#!/usr/bin/python

import urll_proxy
from bs4 import BeautifulSoup
import time

def main():
    date = time.strftime("%d%m%Y")

    link = "http://www.flipkart.com/"

    page = urll_proxy.main(link)
    html = page.read()
    soup = BeautifulSoup(html)
    page.close()

    tag_menu = soup.find_all("li", attrs={"class":"menu-l0"})
    
    dict_menu_links = {}
    
    for l in tag_menu:
        menu =  l.get("data-key")

        tag_menu_item = l.find_all("li", attrs={"class":"menu-item"})
        
	dict_menu_links[menu] = []

        for l2 in tag_menu_item:
            try:
               l2 = "http://www.flipkart.com" + l2.a.get("href")
               dict_menu_links[menu].append(l2)
            except:
                pass

    return  dict_menu_links



if __name__=="__main__":
    main()



    
