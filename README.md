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

### Running the tests

```
pytest -v ugc/tests/
```


### Swagger api specifications

Описание API доступно по URI /api/openapi


https://github.com/urbanchef/ugc_sprint_1
