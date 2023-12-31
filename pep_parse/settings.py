from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

ALLOWED_DOMAIN = 'peps.python.org'

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
