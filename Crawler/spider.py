import scrapy


class CompanySpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.saramin.co.kr/zf_user/recruit/company-info/idx/1',
    ]

    def parse(self, response):
        dic = {}
        for info in response.css('.table_col_type1').css('tbody').css('tr'):
            key = info.css('th::text').extract_first().strip()
            if key == "홈페이지":
                dic[key] = link = info.css('td a.link_site::attr("href")').extract_first()
            else:
                dic[key] = info.css('td::text').extract_first().strip()
        yield dic
