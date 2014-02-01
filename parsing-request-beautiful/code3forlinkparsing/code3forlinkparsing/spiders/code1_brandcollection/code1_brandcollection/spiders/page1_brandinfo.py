from bs4 import BeautifulSoup
import urll_proxy
import time
import sys
import MySQLdb
import os
import shutil
import phan_proxy
import subprocess

def main(link):

    page = urll_proxy.main(link)
    soup = BeautifulSoup(page)
    tag_ul = soup.find_all("ul", attrs={"id":"brand"})

    cat_name = link.split("/")[-2].strip()
    
    currentdir = os.getcwd()

    currentdate = time.strftime("%d%m%Y")

    branddir = currentdir+"/brand_info_by_date/"+cat_name+currentdate

    if not os.path.exists(branddir):
        subprocess.check_output(['mkdir', '-p', branddir])
    
    fname = branddir+"/"+cat_name

    f = open(fname+"_bn_bc_bl.csv","a+")
    f2 = open(fname+"_brandname_brandlink.csv", "a+")

    tag_a = tag_ul[0].find_all("a")
     
    pos = 1
    for l in tag_a:
        brand_link = "http://www.flipkart.com"+str(l.get("href")).strip()
	brand_name = str(l.span.get_text()).strip()
	brand_count = str(l.find("span", attrs={"class":"count"}).get_text()).strip("()")
	date = str(time.strftime("%d/%m/%Y"))
        print >>f, ','.join([date, str(pos), brand_name, brand_count, brand_link])
	print >>f2, ','.join([brand_name, brand_link])
        pos = pos+1
       

    f.close()
    f2.close()
    print fname+"_brandname_brandlink.csv"

    #shutil.copy2(cat_name+"_bn_bl_bc.csv", cat_name+"_bn_bl_bc_old.csv")
    #os.remove(cat_name+"_bn_bl_bc.csv")
    







if __name__=="__main__":
    main(sys.argv[1])    

