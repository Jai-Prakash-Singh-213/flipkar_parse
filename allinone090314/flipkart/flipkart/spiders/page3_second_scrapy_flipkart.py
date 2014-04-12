# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import time
from lxml import html
import re
import ast

#page3_scrapy_myntra.py , page3_filedivision_myntra.py 


class DmozSpider(BaseSpider):
    name = "link_to_link"
    allowed_domains = ["flipkart.com"]

    def __init__(self, pth = None):
        pthdoc = pth.strip()[:-1]
        self.pth = pth
        

        f = open(pthdoc)
        line = f.readline().strip()
        f.close()
         
        line = ast.literal_eval(line) 

        self.target = line[0]
        self.catlink = line[1]
	self.cattitle = line[2]
	self.subcatlink = line[3]
	self.subcattitle = line[4]
	self.brandlink = line[5]
	self.brandtitle = line[6]
	
        f = open(pth)
        avalurls = f.read().strip().split("\n")
        self.start_urls = map(str.strip, avalurls)
        f.close()
    

    def parse(self, response):
        try:
            link = response.url

            page = response.body

            soup = BeautifulSoup(page, "html.parser")
             
            tree = html.fromstring(page)
             
            title = tree.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div/div/div[3]/div/h1/text()")
            title = str(title[0])
            
            sp = soup.find("span", attrs={"class":"fk-font-verybig pprice fk-bold"})
            sp = str(sp.get_text().encode("ascii", "ignore"))
            
            mrp = soup.find("span", attrs={"class":"price list old-price"})

            if mrp is not None:
                mrp = str(mrp.get_text().encode("ascii", "ignore"))

            else:
                mrp = sp

            size = tree.xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/a/div/div/text()")
            size = str(size)
       
            tag_vender = soup.find("a", attrs={"class":"pp-seller-badge-name fk-bold"})
            vender = str(tag_vender.get_text())

            tag_desc = soup.find("div", attrs={"id":"description"})
            desc = str(tag_desc)

            sku = "None"
            #tag_sku = tree.xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[5]/div/div/a/@href")
            tag_sku = soup.find("a", attrs={"class":"btn btn-orange btn-buy-big fk-buy-now fkg-pp-buy-btn"})

            if tag_sku is not None:
                #start = tag_sku[0].strip().find("=")
                #sku = str(tag_sku[0]).strip()[start+1:]
                sku = str(tag_sku.get("data-buy-listing-id"))

            image = tree.xpath("//*[@id='visible-image-small']/@src")
            image = str(image[0])

            colour = "None"
            
            tag_colour = soup.find("div", attrs={"class":"sectionImage paletteImage"})

            if tag_colour is not None:
	        try:
                    colour = tag_colour.find("div", attrs={"class":"multiselect-item"})
	            colour = str(colour.get("title"))
		except:
		    pass
            
            spec = soup.find("div", id="specifications")
            spec =  str(spec)

            metatitle = soup.find("title")
	    metatitle = str(metatitle.get_text())
	    
            metadisc = soup.find("meta", attrs = {"name":"Description"})
	    metadisc = str(metadisc.get("content"))

            date = str(time.strftime("%d:%m:%Y"))

            status = "None"

            filename = "%s.csv" %(self.pth[:-5])

            f = open(filename, "a+")
      
            fileline = [sku, title, self.catlink, sp, self.cattitle,  self.subcattitle, self.brandtitle, image, mrp,
                        colour, self.target, link, vender, metatitle, metadisc, size,
                        desc, spec, date, status]

            fileline = map(self.string_correction, fileline)
     
            

            print >>f,  ','.join(fileline)

            print fileline

            f.close()


        except:
           f = open("to_scrape_once_again_flipkart", "a+")
           print >>f, str(self.pth), str(response.url)
           f.close()




    def string_correction(self, x):
        return str(x).replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(",",  " ").strip()
