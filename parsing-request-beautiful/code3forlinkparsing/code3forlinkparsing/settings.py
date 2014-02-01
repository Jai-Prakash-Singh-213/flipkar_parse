# Scrapy settings for code3forlinkparsing project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'code3forlinkparsing'

SCRAPY_SETTINGS_MODULE = ["code3forlinkparsing.settings",
                          "code3forlinkparsing.spiders.project2.project2.spiders.settings.py", 
                          "code3forlinkparsing.spiders.project3.project3.spiders.settings.py"]

SPIDER_MODULES = ['code3forlinkparsing.spiders']
NEWSPIDER_MODULE = 'code3forlinkparsing.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'code3forlinkparsing (+http://www.yourdomain.com)'


#TELNETCONSOLE_HOST = '127.0.0.1' # defaults to 0.0.0.0 set so
#TELNETCONSOLE_PORT = '6000'      # only we can see it.
#TELNETCONSOLE_ENABLED = False
#COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent

#USER_AGENT = 'code3_scrap_links_its_info (+http://www.yourdomain.com)'



DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'code3forlinkparsing.proxymiddle.ProxyMiddleware': 100,
}
