import scrapy


class CompanySpider(scrapy.Spider):
    name = "quotes"
    base_url = 'http://www.saramin.co.kr/zf_user/recruit/company-info-view?idx=%d'

    def start_requests(self):
        for i in range(1, 100):
            yield scrapy.Request(self.base_url % i)

    def parse(self, response):
        dic = {}
        for info in response.css('.table_col_type1').css('tbody').css('tr'):
            key = info.css('th::text').extract_first().strip()
            if key == "홈페이지":
                dic[key] = info.css('td a.link_site::attr("href")').extract_first()
            else:
                dic[key] = info.css('td::text').extract_first().strip()
        yield dic
