from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import sys
import page1_collection_link
from bs4 import BeautifulSoup 



class DmozSpider(BaseSpider):
    name = "page2_bag_info"
    allowed_domains = ["flipkart.com"]
    start_urls = page1_collection_link.main()


    def parse(self, response):
        page = response.body
        soup = BeautifulSoup(page)

        tag_h1 = soup.find("h1", attrs={"itemprop":"name"})
	item_title = str(tag_h1.get_text()).strip()

	tag_colour  = soup.find("div", attrs={"class":"line extra_text bmargin10"})
        try:
	    item_clour = str(tag_colour.get_text()).strip()
        except:
	    item_clour = None

	tag_img  = soup.find("img", attrs={"id":"visible-image-small"})
	item_image = tag_img.get("src")

	tag_discount  = soup.find("span", attrs={"id":"fk-mprod-list-id"})
	try:
	    item_discount = str(tag_discount.get_text()).strip()
	except:
	    item_discount = "No Discount"

	tag_price  = soup.find("span", attrs={"class":"fk-font-verybig pprice fk-bold"})
	item_price = str(tag_price.get_text()).strip()

	tag_seller  = soup.find("a", attrs={"class":"pp-seller-badge-name fk-bold"})
	item_seller = str(tag_seller.get_text()).strip()

	f = open("page2_hand_bag_info", "a+")
	print >>f, ','.join([item_title,item_clour, item_image, item_discount, item_price, item_seller])
	f.close()






