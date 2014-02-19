#!/usr/bin/env python
# -*-coding:utf-8 -*

from scrapy.spider import BaseSpider
from scrapy.selector import Selector

class DmozSpider(BaseSpider):
    name = "laststep"
    allowed_domains = ["flipkart.com"]

    def __init__(self, urlfile = None):
       
        f2 = open(urlfile)
        self.start_urls = f2.read().strip().split("\n")
	f2.close()
        
        self.f = open("laststep.txt", "a+")
               
 
    def __del__(self):
        self.f.close()


    def parse(self, response):
        
        infodict = {}

        sel = Selector(response)
        spth  = sel.xpath 
        
        title = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div/h1/text()").extract()
        #title = ' '.join(map(str , title)).replace("\n", " ").strip()
        infodict["title"] = title

	titleimg   = spth("//*[@id='visible-image-small']/@src").extract()
        #titleimg = '  '.join(map(str , titleimg)).replace("\n", " ").strip()
        infodict["titleimg"] = titleimg 

	colour = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div/div[2]/a/div/div/@title").extract()
        #colour = ' '.join(map(str , colour)).replace("\n", " ").strip()
        infodict["colour"] = colour 

	size   = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/a/div/div/text()").extract()
        #size  = ' '.join(map(str , size)).replace("\n", " ").strip()
        infodict["size"] = size

        mrp = spth("//*[@id='fk-mprod-list-id']/text()").extract()
        #mrp = ' '.join(map(str , mrp)).replace("\n", " ").strip()
        infodict["mrp"] = mrp


	sp = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/span/text()").extract()
        #sp = ' '.join(map(str , sp)).replace("\n", " ").strip()
        infodict["sp"] = sp

	sku  = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[5]/div/div/a/@href").extract()
        #sku = ' '.join(map(str , sku)).replace("\n", " ").strip()
        infodict["sku"] = sku

	desc = spth("//*[@id='description']").extract()
        #desc = ' '.join(map(str , desc)).replace("\n", " ").strip()
        infodict["desc"] = desc 

	spec  = spth("//*[@id='specifications']").extract()
        #spec = ' '.join(map(str , spec)).replace("\n", " ").strip()
        infodict["spec"] = spec

        seller   = sel.xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[3]/div[2]/div/div/a/text()").extract()
        #seller  = ' '.join(map(str , seller)).replace("\n", " ").strip()  
        infodict["seller"] = seller

	#print >>self.f,  ','.join([title, titleimg, colour, size,  mrp, sp, sku, desc, spec, seller])
        print >>self.f, infodict

        infodict.clear()
        

           

