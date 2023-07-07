## 20.1 Работа с ORM в Django. Домашнее задание

### Реализовано в проекте:

#### 1. Подключена СУБД PostgreSQL для работы в проекте. Настройки подключения вынесены в переменные окружения, смотрите config.settings.py
    - pip install psycopg2


#### 2. В приложении каталога создано две модели с полями. Cоздана миграции для новых моделей:
    - Product (Наименование, Описание, Изображение, Категория, Цена за покупку, Дата создания, Дата последнего изменения)
    - Category (Наименование, Описание)
    - python manage.py makemigrations


#### 3. Внесены изменения в модель категорий, добавлено поле created_at. Осуществлен откат миграции
    - creation_at = models.DateField(verbose_name='Дата создания')
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py migrate catalog 0001
![migration](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-04%20(1).png?raw=true)



#### 4. Для моделей категории и продукта настроено отображение в административной панели.
#### Для категорий выведен id и наименование в список отображения, а для продуктов выведен в список id, название, 
#### цену и категорию. Отображение можно фильтровать по категории, а также осуществлять поиск по названию и полю описания.
    - python manage.py createsuperuser (Username-admin, password -12345)
    - localhost:8000/admin


#### 6. Через инструмент shell заполнен список категорий, применены фильтры.
    - python manage.py shell
    - Category.objects.create(name='Оборудование', description='Автотовары')
![shell](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-06%20(1).png?raw=true)



    - category_list = Сategory.objects.filter(name='Детейлинг')
    - category_list.count(), category_list.exists()

![catlist](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-06%20(8).png?raw=true)



    - category_list = Сategory.objects.get(pk=1)

![catlist_pk1](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-06%20(9).png?raw=true)


    - category_list.__dict__
    - category_list.delete()

![catlist_del](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-06%20(10).png?raw=true)
![catlist_del](https://github.com/Miklefil/dz_20_1/blob/master/screenshots/2023-07-06%20(11).png?raw=true)

#### Сформирована фикстура для заполнения и выгрузка json из базы данных.
    - python -Xutf8 manage.py loaddata Catalog_product.json
    - python -Xutf8 manage.py dumpdata catalog -o Catalog_product.json


#### Написана кастомная команда, которая умеет заполнять данные в базу данных
    - python manage.py catalog_fill.py
    - python manage.py product_fill.py



