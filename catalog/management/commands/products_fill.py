from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    """Класс который, удаляет товары из базы данных, потом его заполняет"""

    def handle(self, *args, **options):

        Product.objects.all().delete()

        product_list = [
            {'name': '4-х поршневой суппорт JBT CB4P',
             'description': 'Применяется с дисками: 303мм, толщина 25мм, колесный диск 16.'
                            '330мм с алюминевой ступицей, толщина 32мм, колесный диск 17.'
                            '355мм с алюминевой ступицей, толщина 32мм, колесный диск 18.',
             "image": "products/CB4P.png",
             'category': 'Cуппорты',
             'price': 25000, 'creation_at': '2021-01-01', 'modified_at': '2021-01-01'},

            {'name': '4-х поршневой суппорт JBT FB4P1',
             'description': 'Применяется с дисками: 380мм с алюминиевой ступицей, толщина 32мм, колесный диск 19" и более',
             "image": "products/FB4P1.png",
             'category': 'Cуппорты',
             'price': 25000, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},

            {'name': '4-х поршневой суппорт JBT CM4P',
             'description': 'Применяется с дисками: 282-330мм, толщина 24-26мм, колесный диск 15"-17"',
             "image": "products/CM4P.png",
             'category': 'Cуппорты',
             'price': 25000, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},

            {'name': '6-ти поршневой суппорт JBT CB6P',
             'description': 'Применяется с дисками: 355мм с алюминиевой ступицей, толщина 32мм, колесный диск 18", 19" и '
                            'более.' '330мм с алюминиевой ступицей, толщина 32мм, колесный диск 17", 18',
             "image": "products/CB6P.png",
             'category': 'Cуппорты',
             'price': 36000, 'creation_at': '2022-01-01', 'modified_at': '2022-01-01'},

            {'name': 'Кованый 8-ми поршневой суппорт JBT FM8P',
             'description': 'Применяется с дисками: 355мм с алюминиевой ступицей, толщина 32мм, колесный диск 18", 19" и более.',
             "image": "products/FM8P.png",
             'category': 'Cуппорты',
             'price': 45000, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},

            {'name': 'Кованый 8-ми поршневой суппорт JBT FB8P',
             'description': 'Применяется с дисками:'
                            '405мм с алюминиевой ступицей, толщина 34-36мм, колесный диск 20", 22.'
                            '380мм с алюминиевой ступицей, толщина 34мм, колесный диск 19", 20", 22.',
             "image": "products/FB8P.png",
             'category': 'Cуппорты',
             'price': 60000, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},

            {'name': 'Кованый 12-ти поршневой суппорт JBT FB12P',
             'description': 'Применяется с дисками: 405мм с алюминиевой ступицей, толщина 34-36мм, колесный диск 20", 22" и более.'
                            '380мм с алюминиевой ступицей, толщина 34мм, колесный диск 19", 20", 22" и более',
             "image": "products/FB12P.png",
             'category': 'Cуппорты',
             'price': 70000, 'creation_at': '2022-02-01', 'modified_at': '2022-02-01'},
        ]

        products_objects = []
        for product_item in product_list:
            products_objects.append(Product(**product_item))

        Product.objects.bulk_create(products_objects)
