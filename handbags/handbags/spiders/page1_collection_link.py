#-*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re 
import MySQLdb
import time
import sys


def matching(item_name, brand_name_list):
     for value in brand_name_list:
         match = re.search(value, item_name)
         if match:
	     return value 



def main():
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","flipkart")
    cursor = db.cursor()
    cursor.execute( "create table if not exists position_brand_itemname_itemprice_itemlinks (\
                    id int(11) not null auto_increment, date varchar(45),\
		    position varchar(20), brand  varchar(255), item_name varchar(100),\
                    item_price  varchar(255), item_link varchar(255),PRIMARY KEY (id, item_name));") 
     
    brand_file = open("page1_brandname")
    brand_name_list = brand_file.read().split("\n")
    brand_file.close()

    f = open("pag1_body.html")
    html = f.read().encode("ascii","ignore")
    
    soup = BeautifulSoup(html)
    
    tag_a = soup.find_all("a", attrs={"class":"fk-display-block"})

    date = str(time.strftime("%d/%m/%Y"))

    urls_list = []

    tag_price = soup.find_all("span", attrs={"class":"fk-font-17 fk-bold"})
     
   
    for l, p in zip(tag_a, tag_price):
        item_name = str(l.get_text()).strip()
	brand = matching(item_name, brand_name_list)
	item_link = "http://flipkart.com"+str(l.get("href"))
        item_price = p.get_text().strip()

	urls_list.append(item_link)

        value = date, tag_a.index(l)+1, brand, item_name, item_price, item_link

        sql = """insert into position_brand_itemname_itemprice_itemlinks (date, position, brand, item_name, item_price, item_link) values ("%s", "%s", "%s", "%s", "%s", "%s")"""%(value)
        cursor.execute(sql)
	db.commit()

    f.close()
    db.close()
    
    return  urls_list 

    
if __name__=="__main__":
    urls_list = main()
