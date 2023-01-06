import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import csv file phones.csv to database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            data = list(csv.DictReader(file, delimiter=';'))

        for row in data:
            phone = Phone(
                name=row['name'],
                image=row['image'],
                price=row['price'],
                release_date=row['release_date'],
                lte_exists=row['lte_exists'],
            )
            phone.save()
