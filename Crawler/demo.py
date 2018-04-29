# import dmoz spider class
import scrapy;
from Crawler import spider

# scrapy api
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(spider.QuotesSpider())
process.start() # the script will block here until the crawling is finished