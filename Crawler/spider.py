import scrapy
from .items import Company, table_head_to_class_field


class CompanySpider(scrapy.Spider):
    name = "quotes"
    base_url = 'http://www.saramin.co.kr/zf_user/recruit/company-info-view?idx=%d'

    def start_requests(self):
        for i in range(1, 10):
            yield scrapy.Request(self.base_url % i)

    def parse(self, response):
        item = Company()
        for info in response.css('.table_col_type1').css('tbody').css('tr'):
            key = table_head_to_class_field(info.css('th::text').extract_first().strip())
            value = info.css('td::text').extract_first().strip()
            if key == "website":
                item[key] = info.css('td a.link_site::attr("href")').extract_first()
            elif key is not None and value is not None:
                item[key] = value
        yield item
