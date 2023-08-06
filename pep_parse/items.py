import scrapy


class PepParseItem(scrapy.Item):
    """Описание данных."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
