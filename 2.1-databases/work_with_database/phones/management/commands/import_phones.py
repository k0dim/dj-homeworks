import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            if len([q for q in Phone.objects.filter(id=phone['id'])]) == 0:
                phonedb = Phone(
                    id = phone['id'],
                    name = phone['name'],
                    slug = slugify(phone['name']),
                    image = phone['image'],
                    price = phone['price'],
                    release_date = phone['release_date'],
                    lte_exists = phone['lte_exists'],
                )
                phonedb.save()
        try:
            return print('Success')
        except:
            return print('Error')
