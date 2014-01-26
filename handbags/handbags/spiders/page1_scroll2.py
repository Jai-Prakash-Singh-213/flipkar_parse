#!/usr/bin/env python 

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-




from selenium import webdriver
from random import choice
import time
from selenium.webdriver.common.action_chains import  ActionChains

f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()



class scroller():

    allowed_domains = ["flipkart.com"]
    start_urls = "http://www.flipkart.com/bags-wallets-belts/bags/hand-bags/pr?sid=reh%2Cihu%2Cm08"

    def __init__(self):
        ip_port = choice(ip_list)
        prox = "--proxy=%s"%ip_port
        service_args = [prox,'--proxy-type=http',]
        self.driver = webdriver.PhantomJS(service_args =service_args)
        self.driver = webdriver.PhantomJS()
        self.start_urls = "http://www.flipkart.com/bags-wallets-belts/bags/hand-bags/pr?sid=reh%2Cihu%2Cm08"
        self.parse()

    def __del__(self):
        self.driver.close()


     
    def parse(self):   
        driver = self.driver
	start_urls = self. start_urls
           
        driver.get(start_urls)
        

        for i in range(0,60):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            print "scrolling"
      
        loop = True
        while loop is True:
            #elem = self.driver.execute_script("window.scrollBy(0,-450)", "");
	    #menu = driver.find_element_by_xpath("//*[@id='show-more-results']")
	    #hover = ActionChains(driver).move_to_element(menu)
	    #hover.perform()
	    #menu.click()
	    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  
            #elem = self.driver.execute_script("window.scrollBy(0,-450)", "");
	    #time.sleep(2)
	    #print "wating for click...."
            #driver.find_element_by_id("show-more-results").click()
	    #time.sleep(2)
	    #print "clicked----"
	    #print "scrolling down...."
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    #time.sleep(2)
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
 
        
        self.page = driver.page_source
        
        f = open("pag1_body.html","w+")
	print >>f, self.page.encode("ascii","ignore")
	f.close()
        print self.page

        return self.page



def main():
    obj = scroller()



if __name__=="__main__":
    main()
