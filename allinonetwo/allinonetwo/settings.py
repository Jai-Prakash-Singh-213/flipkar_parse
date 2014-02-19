# Scrapy settings for allinonetwo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'allinonetwo'

SPIDER_MODULES = ['allinonetwo.spiders']
NEWSPIDER_MODULE = 'allinonetwo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'allinonetwo (+http://www.yourdomain.com)'


WEBSERVICE_ENABLED = False
TELNETCONSOLE_ENABLED  = False


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'allinonetwo.proxymiddle.ProxyMiddleware': 100,
}

