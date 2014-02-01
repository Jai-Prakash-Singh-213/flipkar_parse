# Scrapy settings for project2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'project3'

SPIDER_MODULES = ['project3.spiders', 'code3forlinkparsing.spiders']
NEWSPIDER_MODULE = 'project3.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'project2 (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'project3.proxymiddle.ProxyMiddleware': 100,
}

