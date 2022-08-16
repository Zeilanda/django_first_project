import json

from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as json_content:
            books = json.load(json_content)

        for book in books:
            Book.objects.create(name=book['fields']['name'],
                                author=book['fields']['author'],
                                pub_date=book['fields']['pub_date'])
                # TODO: Добавьте сохранение модели
                # pass

