import csv
import datetime as dt
from collections import defaultdict

from .settings import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:

    def __init__(self):
        """Инициализация пайплайна."""
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """Подсчёт статусов."""
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        """Обновление счётчика."""
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Запись результатов в файл."""
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = self.results_dir / file_name
        data_to_write = [
            ['Статус', 'Количество'],
            *sorted(self.status_counter.items()),
            ['Всего', sum(self.status_counter.values())]
        ]
        with open(file_path, 'w', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, dialect=csv.unix_dialect)
            csv_writer.writerows(data_to_write)
