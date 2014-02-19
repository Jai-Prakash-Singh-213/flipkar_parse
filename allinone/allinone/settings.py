# Scrapy settings for allinone project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'allinone'

SPIDER_MODULES = ['allinone.spiders']
NEWSPIDER_MODULE = 'allinone.spiders'

WEBSERVICE_ENABLED = False
TELNETCONSOLE_ENABLED  = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'allinone (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'allinone.proxymiddle.ProxyMiddleware': 100,
}
