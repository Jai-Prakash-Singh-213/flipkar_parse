#!/usr/bin/env python 

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
import time
import os
from scrapy.spider import Spider


class DmozSpider(Spider):
    name = "collect_link_and_extract"

    allowed_domains = ["flipkart.com"]


    def __init__(self, pth = None):
           
        fpth = pth 

        pth = pth.split("/")

        self.dirfour = "dirfour_s_%s%s%s" %( pth[0][-8:], "/", "/".join(pth[1:-1]))

	self.catname = pth[-2].split("-xx-")[-2]

	self.brandname = pth[-1][:-3]

        if not os.path.exists(self.dirfour):
            os.makedirs(self.dirfour)
       
        self.f = open(self.dirfour + "/" + pth[-1], "a+")
       
        f2 = open(fpth)
        self.start_urls = f2.read().strip().split("\n")        
        f2.close()
     

    def __del__(self):
        self.f.close()   
    
    
    def parse(self, response):
       
        infodict = {}

        sel = Selector(response)
        spth  = sel.xpath
        
        infodict["itemlink"] =  response.url
        
        infodict["date"] = time.strftime("%d:%m:%Y")

        title = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div/h1/text()").extract()
        infodict["title"] = title

        titleimg   = spth("//*[@id='visible-image-small']/@src").extract()
        infodict["titleimg"] = titleimg

        colour = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div/div[2]/a/div/div/@title").extract()
        infodict["colour"] = colour

        size   = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/a/div/div/text()").extract()
        infodict["size"] = size

        mrp = spth("//*[@id='fk-mprod-list-id']/text()").extract()
        infodict["mrp"] = mrp


        sp = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/span/text()").extract()
        infodict["sp"] = sp

        sku  = spth("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[5]/div/div/a/@href").extract()
        infodict["sku"] = sku

        desc = spth("//*[@id='description']").extract()
        infodict["desc"] = desc


        spec  = spth("//*[@id='specifications']").extract()
        infodict["spec"] = spec

        seller   = sel.xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div[3]/div[3]/div[2]/div/div/a/text()").extract()
        infodict["seller"] = seller

        print >>self.f, infodict

        infodict.clear()
