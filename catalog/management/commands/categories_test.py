from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Очистка старых данных
        Category.objects.all().delete()

        # Загрузка данных
        catalog_test = [
            {
                'name': 'Планшеты',
                'description': 'Китай'
            },
            {
                'name': 'Телефоны',
                'description': 'Apple'
            },
            {
                'name': 'Ноутбуки',
                'description': 'ASUS'
            },
            {
                'name': 'Настольные компьютеры',
                'description': 'Собрать'
            }
        ]

        categorys_d = []
        for item in catalog_test:
            categorys_d.append(Category(**item))

        Category.objects.bulk_create(categorys_d)
