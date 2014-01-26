

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


from random import choice
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup

from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import re
from selenium import selenium
import time
import sys

f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()



class DmozSpider(BaseSpider):
    name = "page1_scroll"

    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/bags-wallets-belts/bags/hand-bags/pr?sid=reh%2Cihu%2Cm08"]

    def __init__(self):
        ip_port = choice(ip_list)
        prox = "--proxy=%s"%ip_port
        service_args = [prox,'--proxy-type=http',]
        self.driver = webdriver.PhantomJS(service_args =service_args)
        self.driver = webdriver.PhantomJS()
        

    def __del__(self):
        self.driver.close()


     
    def parse(self, response):   
        driver = self.driver
        driver.get(str(response.url))
        

        for i in range(0,60):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            print "scrolling"

        time.sleep(2)

        #    elem = self.driver.execute_script("window.scrollBy(0,-450)", "");
        #    elem = driver.find_element_by_xpath("//*[@id='show-more-results']")
        #    wait = WebDriverWait(driver, 5)
        #    wait.until(lambda driver: driver.execute_script("window.scrollBy(0,-450)", ""))
        #    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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


        
        self.page = self.driver.page_source
        f = open("pag1_body.html","w+")
	print >>f, self.page.encode("ascii","ignore")
	f.close()
        print self.page
        return self.page
