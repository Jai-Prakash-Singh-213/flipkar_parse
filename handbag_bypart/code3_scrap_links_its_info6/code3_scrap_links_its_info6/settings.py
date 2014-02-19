# Scrapy settings for code3_scrap_links_its_info project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'code3_scrap_links_its_info6'

SPIDER_MODULES = ['code3_scrap_links_its_info6.spiders']
NEWSPIDER_MODULE = 'code3_scrap_links_its_info6.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'code3_scrap_links_its_info (+http://www.yourdomain.com)'


#TELNETCONSOLE_HOST = '127.0.0.1' # defaults to 0.0.0.0 set so
#TELNETCONSOLE_PORT = '6066'      # only we can see it.
#TELNETCONSOLE_ENABLED = False


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'code3_scrap_links_its_info6.proxymiddle.ProxyMiddleware': 100,
}
