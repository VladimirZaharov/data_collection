import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    vacancy_name = scrapy.Field()
    salary_from = scrapy.Field()
    salary_to = scrapy.Field()
    vacancy_link = scrapy.Field()
    vacancy_site = scrapy.Field()

