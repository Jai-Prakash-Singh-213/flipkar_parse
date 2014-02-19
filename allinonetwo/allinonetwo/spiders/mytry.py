import sys
import os
import subprocess
import time
from scrapy import cmdline

def main():
    #os.environ.get("export SCRAPY_SETTINGS_MODULE=allinone.settings")
    #sys.path.append("/home/desktop/flipkart/allinone/")
    #os.environ.get("export PYTHONPATH=/home/desktop/flipkart/allinone/")
    #output = subprocess.check_output(['scrapy',  'crawl', 'collect_link_and_extract',   '-a',  'pth=dirthree08022014/women/womens-footwear/womens-footwear-xx-sports-shoes-xx-bnbcbl/ZEMgear.csv'])
    #time.sleep(2)
    #q.task_done()

    cmdline.execute(['scrapy',  'crawl', 'collect_link_and_extract',   '-a',  'pth=dirthree08022014/women/womens-footwear/womens-footwear-xx-sports-shoes-xx-bnbcbl/ZEMgear.csv'])



if __name__=="__main__":
    main()
