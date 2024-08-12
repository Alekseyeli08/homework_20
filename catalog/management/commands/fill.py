import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_categories() -> list:
        """
        Получение данных из фикстуры с категориями
        :return: список с категориями
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_products() -> list:
        """
        Получение данных из фикстуры с продуктами
        :return: список с продуктами
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding="utf-8") as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == "catalog.product"]
        return products

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Category.truncate_table_restart_id()
        Product.objects.all().delete()
        product_list = []
        category_list = []

        for category in Command.json_categories():
            category_list.append(
                {"id": category['pk'], "name": category['fields']['name'],
                 "description": category['fields']['description']}
            )
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category.objects.create(**category_item)
            )

        for product in Command.json_products():
            product_list.append(
                {"id": product['pk'], "name": product['fields']['name'],
                 "description": product['fields']['description'],
                 "price": product['fields']['price'],
                 "category": Category.objects.get(pk=product['fields']['category']),
                 "image": product['fields']['image'], "created_at": product['fields']['created_at'],
                 "updated_at": product['fields']['updated_at']}
            )
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(**product_item)
            )

        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)