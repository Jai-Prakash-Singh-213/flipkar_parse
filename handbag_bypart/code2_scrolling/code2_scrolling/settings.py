# Scrapy settings for code2_scrolling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'code2_scrolling'

SPIDER_MODULES = ['code2_scrolling.spiders']
NEWSPIDER_MODULE = 'code2_scrolling.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'code2_scrolling (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'code2_scrolling.proxymiddle.ProxyMiddleware': 100,
}
