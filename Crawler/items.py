import scrapy


class Company(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()
    type = scrapy.Field()
    established_at = scrapy.Field()
    employee_number = scrapy.Field()
    revenue = scrapy.Field()
    capital = scrapy.Field()
    income = scrapy.Field()
    tel = scrapy.Field()
    fax = scrapy.Field()
    website = scrapy.Field()
    address = scrapy.Field()
    pass
