import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAIN


class PepSpider(scrapy.Spider):
    """Парсер."""
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Начальный парсинг."""
        all_peps = response.css('#numerical-index a[href^="pep-"]::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Извлечение информации."""
        header = response.css('article h1::text').get()
        number, name = header.split(' – ', 1)
        yield PepParseItem(
            {
                'number': int(number.split()[-1]),
                'name': name,
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text').get(),
            }
        )
