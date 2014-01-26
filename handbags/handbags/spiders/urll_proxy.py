# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

import base64
from random import choice
import urllib2


f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()


def main(link):
    ip = choice(ip_list)
    #ip = "194.141.252.102:8080"
    req = urllib2.Request(link)
    req.set_proxy(ip, 'http')
    response = urllib2.urlopen(req).read().strip()
    #print response
    return response


if __name__=="__main__":
    link = "'http://www.webserver.com/test'"
    main(link)
     
