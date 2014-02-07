# Scrapy settings for code1_brandcollection project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'code1_brandcollection'

SPIDER_MODULES = ['code1_brandcollection.spiders']
NEWSPIDER_MODULE = 'code1_brandcollection.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'code1_brandcollection (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'code1_brandcollection.proxymiddle.ProxyMiddleware': 100,
}
