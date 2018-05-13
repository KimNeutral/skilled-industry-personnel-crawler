import scrapy

table = {
    '기업명': 'name',
    '사업내용': 'desc',
    '기업형태': 'type',
    '설립일': 'established_at',
    '사원수': 'employee_number',
    '매출액': 'revenue',
    '자본금': 'capital',
    '영업이익': 'income',
    '대표전화': 'tel',
    'FAX': 'fax',
    '홈페이지': 'website',
    '기업주소': 'address',
}


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
    original_url = scrapy.Field();
    pass


def table_head_to_class_field(table_head):
    if table_head in table:
        return table[table_head]
    return None
