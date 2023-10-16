# Дипломный проект. Продуктовый помощник.
- foodgramsanchess.hopto.org - ссылка на ресурс
#### Запуск проекта локально
```
docker compose -f docker-compose.production.yml up -d --build
docker compose -f docker-compose.production.yml exec python manage.py makemigrations
docker compose -f docker-compose.production.yml exec python manage.py migrate
docker compose -f docker-compose.production.yml exec python manage.py loaddata fixtures/db.json
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
