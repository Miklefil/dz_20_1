## 22.2 Аутентификация. Домашнее задание

### Реализовано в проекте:

#### 1. Создано новое приложение для работы с пользователем. Создана форма авторизации на сайте через электронную почту
    Приложение: class User(AbstractUser)
    Поля: email, phone, avatar, country, token, created_at

#### 2. Функционал аутентификации, а именно:
    - регистрацию пользователя по почте и паролю;
    - верификацию почты пользователя через отправленное письмо;
    - авторизацию пользователя;
    - восстановление пользователя на автоматически сгенерированный пароль (UserForgotPasswordView, UserPasswordResetConfirmView)
    - восстановление пользователя на автоматически сгенерированный пароль в профиле (generate_new_password)


____________________________________________________________________________________________________________________

## 22.1 Формы. Домашнее задание

### Реализовано в проекте:

#### 1. Для модели продуктов (Product) реализован CRUD, задействован модуль Django.forms
    - ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView

#### Сделана валидация для пользователей при создании нового товара (models product).
#### Могут создавать новые продукты; не могут загружать запрещенные продукты на платформу.
#### Запрещенные слова при создании товара (казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар)
    - def clean_name(запрещенные слова при создании товара поле name)
    - def clean_description(запрещенные слова при создании товара поле description)

#### 2. Добавлена новая модель «Версия» (Version), со следующими поля:
    - продукт (product)
    - номер версии (version_number)
    - название версии (version_name)
    - признак текущей версии (is_active)

#### При наличии активной версии выводится список продуктов информации об активной версии
    - class ProductsListView, модуль переопределения get_queryset

#### 3. Для формы работы с продуктом добавлена реализация работы с формсетами для версий продукта. 
    - class ProductsUpdateView, 
        - def get_context_data
        - def form_valid

#### Все созданные формы стилизованы методом __init__
    - class FormStyleMixin
        - class ProductForm(FormStyleMixin)
        - class BlogForm(FormStyleMixin)
        - class VersionForm(FormStyleMixin)
__________________________________________________________________________________________________________________

## 21.1 fbv и cbv. Домашнее задание

### Реализовано в проекте:

#### 1. Имеющиеся контроллеры Products были переведены с FBV на CBV.
    - ProductsListView
    - ProductsDetailView

#### 2. Реализована новая модель CRUD для блоговой записи (class Blog) со следующими полями:
    - заголовок (name);
    - slug (slug);
    - содержимое (content);
    - изображение (image);
    - дата создания (creation_at);
    - признак публикациим (publication);
    - количество просмотров (number_views).

#### 3. Реализован:
    - счетчик просмотров;
    - вывод список статей имеющую положительный признак публикации;
    - динамический slug name для заголовка новых записей;
    - редактирование, удаление, и деактивация записей с перенаправлением пользователя на просмотр этой статьи.

__________________________________________________________________________________________________________________


## 20.2 Шаблонизация. Домашнее задание

### Реализовано в проекте:

#### 1. Создано четыре контроллера:
    - 1. index. Вывод 4 товара на главной странице. 
    - 2. products. Вывод всего товара на отдельной странице
    - 3. products_card. Вывод карточки товара
    - 4. contacts. Контакты с обратной связью

#### 2. Созданы шаблоны, реализованы подшаблоны и базовые шаблоны.
    - base.html. Базовый шаблон. Вынесено в подшаблон навбар, футер меню.
    - inc.catalog_footer.html. Отображение футер меню
    - inc.catalog_menu.html. Отображение навбара.
    - inc.catalog_card.html. Итерация по карточкам товара. 
    - index.html. Реализовано подключение базового шаблона и подшаблон
    - products.html. Отображение всего товара. 
    - product_card.html. Отображение карточки товара
    - contacts.html. Отображение контактов

#### 3. Создан шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:
    - Создан файл templatetags/catalog_tags.py с реализацией тега и фильтра
        в файле inc.catalog_card.html прописано:

        {% load catalog_tags %}
        <img src="{{ object.image|mediapath }}" />

    - шаблонный тег:
        <img src="{% mediapath object.image %}" />

_____________________________________________________________________________________________________________________


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



