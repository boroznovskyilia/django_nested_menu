# Текст задания


Задача :

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1) Меню реализовано через template tag

2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.

3) Хранится в БД.

4) Редактируется в стандартной админке Django

5) Активный пункт меню определяется исходя из URL текущей страницы

6) Меню на одной странице может быть несколько. Они определяются по названию.

7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.

8) На отрисовку каждого меню требуется ровно 1 запрос к БД

 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

 {% draw_menu 'main_menu' %}

 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


## Запуск приложения
1) скачать репозиторй:
    git clone https://github.com/boroznovskyilia/django_nested_menu.git
2) создать venv
    cd django_nested_menu
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
3) создать .env файл в корне проекта и присать следующее(заменить на свое)
    DB_NAME=your_app_name
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_HOST=your_host
    DB_PORT=your_port

4) python manage.py migrate

5) python manage.py createsuperuser
    
    p.s(admin name = admin, admin password = admin)

6) python manage.py runserver

### Детали реализации и руковдстов пользователя

    Меню создается как и в задании при помощи template tags, меню создается в admin панели
    для демонстрации всех меню первого уровня(у которых нет родителей) и их подменю есть url http://localhost:8000/menus

    далее можно переходить по различным меню, так же в зависимости от этого будет изменять ulr, и так же по url можно попасть на страницу с определенным меню

    Так же выполнен пункт который реализует загрузку меню одним запросом в бд:
        - выгружаются меню с их сложенными меню
        - и далее формируется сгруппипрованный по уровням сложенности словарь
        - далее проходим по этом словарю как по деерву используя поиск в глубину и формируем итоговый список меню в       порядке отображения пользователю и передаем на ftont(в наш html)