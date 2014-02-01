import base64
from random import choice
import subprocess
import sys
import os
import time

f = open("/home/desktop/proxy2")
ip_list = f.read().strip().split("\n")
f.close()


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        ip_port = choice(ip_list)
        #print ip_port
        #sys.exit()
        
        #ips = ip_port.split("@")[0].strip()
	#user_pass = ip_port.split("@")[1].strip()

	#subprocess.call(['export http_proxy=http://'+user_pass+'@'+ips], shell=True)
        #os.system("export http_proxy=http://"+user_pass+"@"+ips)
        #time.sleep(1)
        
        request.meta['proxy'] = "http://"+ip_port
        #proxy_user_pass = user_pass
        #encoded_user_pass = base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
