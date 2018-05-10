# import dmoz spider class
import scrapy;
from Crawler import spider
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

# scrapy api
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(get_project_settings())

process.crawl(spider.CompanySpider, idx=2)
process.start() # the script will block here until the crawling is finished
