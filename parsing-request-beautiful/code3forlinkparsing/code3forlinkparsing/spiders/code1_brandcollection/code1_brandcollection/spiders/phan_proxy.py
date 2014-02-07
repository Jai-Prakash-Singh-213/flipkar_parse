from selenium import webdriver
from random import choice


def main(link):
    f2 = open("/home/desktop/proxy_auth.txt")
    proxy_list = f2.read().strip().split("\n")
    f2.close()


    ip_port = choice(proxy_list).strip()

    user_pass = ip_port.split("@")[0].strip()
    prox = "--proxy=%s"%ip_port.split("@")[1].strip()

    service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http',]
    print service_args

    #service_args = [prox, '--proxy-type=http',]
    driver = webdriver.PhantomJS(service_args =service_args)
    
    driver.get(link)

    page = driver.page_source

    driver.delete_all_cookies()
    driver.close()
    
    return page



if __name__=="__main__":
    link = "http://www.flipkart.com/bags-wallets-belts/bags/laptop-bags/pr?p[0]=facets.ideal_for[]%3DWomen&p[1]=facets.brand%255B%255D%3DDigiFlip&sid=reh%2Cihu%2Cq4f"
    main(link)
