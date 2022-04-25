## Movie UGC Service

Сервис отслеживания и аналитики пользовательской активности

### Prerequisites

Для работы понадобится создать .env file в корне проекта.
Пример файла переменных окружения для запуска проекта можно найти в examples/example.env

Для подключения к managed yandex cloud kafka service нужен сертификат.
Сертфикат подключается в контейнер с помощью docker volume.
Чтобы передать сертификат в контейнер с приложением, нужно выставить переменную окружения KAFKA_SSL_CAFILE локально. 

```shell
export KAFKA_SSL_CAFILE=/Users/Downloads/CA.pem
```

### How to run the application

```
docker-compose up -d 
```

### ClickHouse migrations

Сервис etl-migrations, запущенный в docker-compose файле, автоматически выполнит все скрипты,
находящиеся в директории "migrations".

### Running the tests

```
pytest -v ugc/tests/
```

### Storage benchmark

1. MongoDB. 
- массив данных состоит из 148000 документов
- Выборка одного документа происходит на MacBook M1 - за 166 ms, на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 0,9 ms, 1,15 ms, 1,02 ms;
- Поиск документов с условием field="A" на MacBook M1 - за 133 ms, на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 73,1 ms, 63,37 ms, 51,25 ms.

### Swagger api specifications

Описание API доступно по URI /api/openapi


https://github.com/urbanchef/ugc_sprint_1
