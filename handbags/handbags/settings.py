# Scrapy settings for handbags project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'handbags'

SPIDER_MODULES = ['handbags.spiders']
NEWSPIDER_MODULE = 'handbags.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'handbags (+http://www.yourdomain.com)'



DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'handbags.proxymiddle.ProxyMiddleware': 120,
}
