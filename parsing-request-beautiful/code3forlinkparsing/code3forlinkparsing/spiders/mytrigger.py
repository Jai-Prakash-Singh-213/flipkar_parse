import subprocess
import sys
import os 

class mytrigger(object):
    def __init__(self, catlink):
        self.catlink = catlink
        self.currentdir = os.getcwd()
        self.code1(catlink) 
    
    def code1(self, catlink):
       
        fpath = self.currentdir  +"/code1_brandcollection/code1_brandcollection/spiders/page1_brandinfo.py"    

        self.output = subprocess.check_output(["python", fpath, catlink])
 
    def code2_scrolling(self):

        file_bn_bl = self.output.strip()
        cat = self.catlink.split("/")[-2]

	filepath = self.currentdir + "/code2_scrolling/code2_scrolling/spiders/thread_on_scrolling.py"

        output  = subprocess.check_output(["python", filepath, cat,  file_bn_bl])
        print self.output, cat
       

    

if __name__=="__main__":
    catlink = str(sys.argv[1]).strip()

    obj = mytrigger(catlink)

    obj.code2_scrolling()    
