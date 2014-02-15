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
from scrapy.spider import Spider


class DmozSpider(Spider):
    name = "spider75"

    allowed_domains = ["flipkart.com"]


    def __init__(self,  filename = None, brandname = None, catname = None , l = None ])):
        self.filename = filename
        self.brandname = brandname
        self.catname = catname
        self.start_urls = [l]       
   
        
    def parse(self, response):
        

        filename = self.filename
        brandname = self.brandname
        catname = self.catname

        item_link = response.url
        page = response.body

        soup = BeautifulSoup(page)

        try:

            tag_dis = soup.find("div", attrs={"id":"description"})

            if tag_dis:
                tag_dis = str(tag_dis).replace("\n","")

            tag_spec = soup.find("div", attrs={"id":"specifications"})

            if tag_spec:
                tag_spec = str(tag_spec).replace("\n","")

            tag_h1 = soup.find("h1", attrs={"itemprop":"name"})
            item_title = str(tag_h1.get_text()).strip()

            try:
                tag_colour = soup.find("div", attrs={"class":"line extra_text bmargin10"})
                item_clour = str(tag_colour.get_text()).strip()

            except:
                item_clour = "No more colour"

            tag_img = soup.find("img", attrs={"id":"visible-image-small"})
            item_image = tag_img.get("src")

            try:
                tag_price = soup.find("span", attrs={"class":"fk-font-verybig pprice fk-bold"})
                item_price = str(tag_price.get_text()).strip()
            except:
                tag_price = soup.find("div", attrs={"class":"prices"})
                item_price = str(tag_price.get_text()).strip().replace("\n", " ")


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
                f = open("newerrorfilescrapy", "a+")
                print >>f, "sku: " ,item_link
                f.close()
                sku = "not found on path"

            size = []
            try:
                tag_multiselect = soup.find_all("div", attrs={"class":"multiselect-item"})

                for l in tag_multiselect:
                    try:
                        size.append(str(l.get_text()))
                    except:
                        pass
            except:
                pass

            if not size:
                size.append("No size defined")

            size2 = ' '.join(size).replace("\n", " ")

            del size[:]
                del size

            date = str(time.strftime("%d:%m:%Y")).strip()

            f = open(filename,"a+")
            print >>f, ','.join([date, catname, brandname,  item_title, item_price,
                                 item_image, item_clour, item_mrp, item_seller, item_link, sku, size2, str(tag_dis), str(tag_spec)])
            f.close()

            return  [date, catname, brandname,  item_title, item_price,
                                 item_image, item_clour, item_mrp, item_seller, item_link, sku, size2, str(tag_dis), str(tag_spec)]

        except:
            f = open("newerrorfilescrapy", "a+")
            print >>f, item_link
            f.close()
                                                                                                                               
                                                                                                                              

