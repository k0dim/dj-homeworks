# Умный дом

Доброго времени суток!
Работы выполнена.

## Документация по проекту

Для запуска проекта необходимо:

Перейти в директорию:

```bash
cd smart_home
```

Активировать виртальное окружение:

```bash
source venv/bin/activate
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
python manage.py makemigrations
```

```base
python manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
