import csv
import datetime as dt
from collections import defaultdict

from .settings import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        """Подсчёт статусов."""
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        """Обновление счётчика."""
        self.status_counter[item['status']] += 1
        self.status_counter['Total'] += 1
        return item

    def close_spider(self, spider):
        """Создание директории."""
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            total = self.status_counter.pop('Total')
            writer.writerows(sorted(self.status_counter.items()))
            writer.writerow(['Всего', total])
