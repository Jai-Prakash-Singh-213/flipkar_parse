import random
import urllib2



def main(url):
    #f = open("/home/keshu/Desktop/procxies/proxy_http_auth.txt")
    f = open("/home/user/Desktop/proxy5")
    file_pass_ip = f.read().strip().split('\n')
    f.close()

    while True:
        try:
            pass_ip = random.choice(file_pass_ip).strip()
            print pass_ip
            pass_ip = "vinku:india123@" + pass_ip
            proxy = urllib2.ProxyHandler({'http': 'http://'+pass_ip})
            auth = urllib2.HTTPBasicAuthHandler()
            opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
            conn = urllib2.urlopen(url)
            return conn
        except:
            pass



if __name__=="__main__":
    conn = main("http://python.org")
    conn.close()
