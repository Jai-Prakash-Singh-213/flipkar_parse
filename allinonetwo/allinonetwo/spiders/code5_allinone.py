#!/usr/bin/python 

from selenium import webdriver
from bs4 import BeautifulSoup
from random import choice 
import time


def main(dirthree, brandname, brandlink):
    dirthree = dirthree.strip()
    brandname = brandname.strip()
    brandlink = brandlink.strip()

    #f2 = open("/home/user/Desktop/proxy_http_auth.txt")
    f2 = open("/home/desktop/proxy_auth.txt")
    proxy_list = f2.read().strip().split("\n")
    f2.close()
    
    loop = True
    while loop is  True:

        ip_port = choice(proxy_list).strip()

        user_pass = ip_port.split("@")[0].strip()
        prox = "--proxy=%s"%ip_port.split("@")[1].strip()
        service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http', '--load-images=no']
        driver = webdriver.PhantomJS(service_args = service_args)

        driver.get(brandlink)
        
        if str(driver.current_url).strip() == "about:blank":
            loop = True

        else:
            loop = False



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
    print driver.current_url
    print page

    driver.delete_all_cookies()
    driver.close()


    filename = dirthree + "/" + brandname + ".csv"
    f = open(filename, "a+")

    soup = BeautifulSoup(page)
    tag_a = soup.find_all("a", attrs={"class":"fk-display-block"})

    
    
    for link in tag_a:
        link = link.get("href")
        if link != "#":
	    link = "http://www.flipkart.com" + str(link).strip()
	    print >>f, link

    f.close()


if __name__=="__main__":

    dirthree = "dirthree08022014/men/beauty-and-personal-care/beauty-and-personal-care-xx-personal-care-appliances-xx-bnbcbl"
    brandname = "Elchim"
    brandlink = "http://www.flipkart.com/beauty-and-personal-care/personal-care-appliances/pr?p%5B0%5D=facets.ideal_for%255B%255D%3DMen&p%5B1%5D=sort%3Dpopularity&p%5B2%5D=facets.brand%255B%255D%3DElchim&sid=t06%2C79s"
    main(dirthree, brandname, brandlink)






    
    
