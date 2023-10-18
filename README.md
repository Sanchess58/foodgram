# Дипломный проект. Продуктовый помощник. Студент 60 когорты Яндекс.Практикум Сотников А.М.
- foodgramsanchess.hopto.org - ссылка на ресурс
### Используемый стек 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=c6d2f5&color=474389)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=c6d2f5&color=474389)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=c6d2f5&color=474389)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=c6d2f5&color=474389)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=c6d2f5&color=474389)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=c6d2f5&color=474389)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=c6d2f5&color=474389)](https://www.docker.com/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=c6d2f5&color=474389)](https://cloud.yandex.ru/)
#### Запуск проекта локально
```
docker compose -f docker-compose.production.yml up -d --build
docker compose -f docker-compose.production.yml exec python manage.py makemigrations
docker compose -f docker-compose.production.yml exec python manage.py migrate
docker compose -f docker-compose.production.yml exec python manage.py loaddata fixtures/db.json
```
#### Пример файла .env
```
SECRET_KEY=Секретный ключ Django приложения
DEBUG=True or False

DATABASE_NAME=Имя БД
DATABASE_USER=Имя юзера
DATABASE_PASSWORD=пароль
DATABASE_HOST=Хост БД
DATABASE_PORT=Порт
ALLOWED_HOSTS=Разрешенные url
CSRF_TRUSTED_ORIGINS=url для защиты от межподдоменных атак
```
### Возможности приложения
#### На данном сайте вы можете 
- Зарегистрироваться/Авторизироваться/Сменить пароль
- Выставить рецепт с фотографией, ингредиентами и тегами
- Подписаться на автора 
- Добавить рецепт в избранное
- Добавить рецепт в список покупок
- Скачать список покупок
- Перейти в интересующий вас рецепт и посмотреть более подробную информацию о нем

### О проекте
#### «Продуктовый помощник»: приложение, на котором пользователи
- публикуют рецепты кулинарных изделий.
- подписываются на публикации других авторов.
- добавляют рецепты в избранное. 
- добавляют рецепты в список покупок, для дальнейшего скачивания списка продуктов.
### Примеры запросов
- ```GET api/tags/``` - Получение, списка тегов.
- ```GET api/tags/{id}``` - Получение определенного тега.
- ```GET api/ingredients/``` - Получение, списка ингредиентов.
- ```GET api/ingredients/{id}``` - Получение определенного ингредиента.
- ```GET, POST api/recipes/``` - Получение списка с рецептами и публикация рецептов.
- ```GET, PUT, PATCH, DELETE api/recipes/{id}``` - Получение, изменение, удаление определенного рецепта.
- ```GET, DELETE api/recipes/{id}/shopping_cart/``` - Добавление определенного рецепта в список покупок и его удаление.
- ```GET api/recipes/download_shopping_cart/``` - Скачать файл со списком покупок в формате .txt.
- ```GET, DELETE api/recipes/{id}/favorite/``` - Добавление определенного рецепта в список избранного и его удаление.

- ```GET, POST api/users/``` - Получение информации о пользователе и регистрация новых пользователей.
- ```GET api/users/{id}/``` - Получение информации о пользователе.
- ```GET api/users/me/``` - Получение и изменение данных своей учётной записи.
- ```PATCH api/users/set_password/``` - Изменение собственного пароль.
- ```GET, DELETE api/users/{id}/subscribe/``` - Подписаться на пользователя или отписаться от него.
- ```GET api/users/subscribe/subscriptions/``` - Просмотр пользователей на которых подписан текущий пользователь.

- ```POST api/auth/token/login/``` - Получение токена.
- ```POST api/auth/token/logout/``` - Удаление токена.
