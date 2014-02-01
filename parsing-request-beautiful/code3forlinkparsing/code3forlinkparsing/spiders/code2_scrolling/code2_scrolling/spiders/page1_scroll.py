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
import subprocess

f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()

f2 = open("/home/desktop/proxy_auth.txt")
proxy_list = f2.read().strip().split("\n")
f2.close()

class DmozSpider(BaseSpider):
    name = "page1_scroll"

    allowed_domains = ["flipkart.com"]


    def __init__(self, brand_and_url = None,  cat = None, *args, **kwargs):
         
	self.cat = cat

        brand_and_url = brand_and_url.split(",")

        self.brand = brand_and_url[0].strip()
        
        
        self.start_urls = [brand_and_url[1].strip()]

        ip_port = choice(proxy_list).strip()

        user_pass = ip_port.split("@")[0].strip()
        prox = "--proxy=%s"%ip_port.split("@")[1].strip()

        service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http', '--load-images=no']

        self.driver = webdriver.PhantomJS(service_args = service_args)
    
        

    def __del__(self):
        self.driver.delete_all_cookies()
        self.driver.close()

   
    def parse(self, response):   
        driver = self.driver
        brand = self.brand
        
        f = open("page1_link_crawling", "a+") 
        print >>f, ','.join([brand,str(response.url).strip()])
	f.close()

        driver.get(str(response.url))
        

        for i in range(0,30):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            print "scrolling"



        loop = True
        while loop is True:
            try:
                print "clicking..."
                driver.find_element_by_xpath("//*[@id='show-more-results']").click()
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            except:
                loop = False


        page = driver.page_source

        soup = BeautifulSoup(page)

        tag_a = soup.find_all("a", attrs={"class":"fk-display-block"})
        
	currentdate = time.strftime("%d%m%Y")

        currentdir = os.getcwd()
        
	filename = brand+".html"

        fdir =  currentdir + "/brands_htmls/" + self.cat + currentdate
        

	if not os.path.exists(fdir):
	    subprocess.check_output(['mkdir', '-p', fdir])    

	filename = fdir + "/" + brand + ".html"
         
        f = open(filename,"a+")

        for link in tag_a:
            link = str(link.get("href").strip())
            link = "http://www.flipkart.com"+link
            print >>f, link

        f.close()
        
	f = open("page1_link_crawled", "a+")
	print >>f, ','.join([brand,str(response.url).strip()])
        f.close()

        return True
