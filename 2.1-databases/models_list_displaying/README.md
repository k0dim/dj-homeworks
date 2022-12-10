# Делаем онлайн-библиотеку


## Документация по проекту

Для запуска проекта необходимо:

Активировать виртуальное окружение
```bash
sourse venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Команда для запуска приложения

```bash
python manage.py runserver
```

- Для загрузки начальных данных модели Book необходимо выполнить команду:

```bash
python manage.py loaddata fixtures/books.json
```
