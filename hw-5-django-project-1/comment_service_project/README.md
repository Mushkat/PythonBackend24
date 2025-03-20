Команды для запуска проекта

```
python manage.py makemigrations
python manage.py migrate
```

Очистка базы данных и добавление мок данных.
```
python manage.py flush
python manage.py loaddata mock_data.json
```
Пример запроса и результат с мок данными.

![img.png](img.png)

Докер
Команда для контейнера

```
cd .\comment_service_project\
docker-compose -f storage/docker-compose.yml build
docker-compose -f storage/docker-compose.yml up -d
```
![img_1.png](img_1.png)

Тесты
Запускаются с помощью
```
python manage.py test
```
Результаты тестов
![img_2.png](img_2.png)