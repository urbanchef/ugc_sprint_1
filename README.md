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
- Тестовый датасет состоит из 148655 строк данных.
- Выборка одного документа происходит:
  - на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 1,68 ms, 1,47 ms, 1,49 ms;
- Поиск документов с условием field="A":
  - на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 0,13 ms, 0,13 ms, 0,11 ms.

2. ClickHouse. 
- Тестовый датасет состоит из 148655 строк данных.
- Выборка одного документа происходит:
  - на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 12,86 ms, 12,33 ms, 14,18 ms;
- Поиск документов с условием field="A":
  - на Ubuntu (Ryzen 5 5600H) по результатам 3-х испытаний - за 21,34 ms, 24,07 ms, 25,98 ms.

Вывод: выбор падает на mondodb по результатам тестов. 

### Swagger api specifications

Описание API доступно по URI /api/openapi


https://github.com/urbanchef/ugc_sprint_1
