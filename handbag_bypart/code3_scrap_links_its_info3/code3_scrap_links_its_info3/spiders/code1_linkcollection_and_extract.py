#!/usr/bin/env python 

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from selenium import webdriver
from random import choice
import time
from selenium.webdriver.common.action_chains import  ActionChains
from bs4 import BeautifulSoup
import re
import os
import  subprocess
import sys


class DmozSpider(BaseSpider):
    name = "collect_link_and_extract"

    allowed_domains = ["flipkart.com"]


    def __init__(self, filepath = None,  *args, **kwargs):

        self.brandname = filename = filepath.split('/')[-1].strip().split(".")[0]

        output = subprocess.check_output(["cat", filepath])	

        self.start_urls = output.strip().split("\n")        
   
        
    def parse(self, response):
        
        brandname = self.brandname

        page = response.body
        soup = BeautifulSoup(page)

        tag_h1 = soup.find("h1", attrs={"itemprop":"name"})
        item_title = str(tag_h1.get_text()).strip()

        tag_colour = soup.find("div", attrs={"class":"line extra_text bmargin10"})
        try:
           item_clour = str(tag_colour.get_text()).strip()
        except:
           item_clour = None

        tag_img = soup.find("img", attrs={"id":"visible-image-small"})
        item_image = tag_img.get("src")

        tag_discount = soup.find("span", attrs={"id":"fk-mprod-list-id"})
        try:
           item_discount = str(tag_discount.get_text()).strip()
        except:
           item_discount = "No Discount"

        tag_price = soup.find("span", attrs={"class":"fk-font-verybig pprice fk-bold"})
        item_price = str(tag_price.get_text()).strip()

        tag_seller = soup.find("a", attrs={"class":"pp-seller-badge-name fk-bold"})
        item_seller = str(tag_seller.get_text()).strip()
         
        date = str(time.strftime("%d/%m/%Y")).strip()

        link = str(response.url).strip()
         
        currentdate = time.strftime("-%d-%m-%Y")

        currentdir = os.getcwd()

        filename = brandname+".csv"

        fdir =  currentdir + "/item_details_csv/" + currentdate

        if not os.path.exists(fdir):
            subprocess.check_output(['mkdir', '-p', fdir])

        filename = fdir + "/" + brandname + ".csv"

        f = open(filename,"a+")

        
        print >>f, ','.join([date, item_title, item_price, item_image, item_clour, item_discount, item_seller, link])
        f.close()    
