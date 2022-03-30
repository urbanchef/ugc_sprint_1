import os
from logging import config as logging_config

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'UGC API Service')
PROJECT_DESCRIPTION = os.getenv('PROJECT_DESCRIPTION', 'Сервис треккинга пользовательской активности')

KAFKA_HOST = os.getenv('KAFKA_HOST', '127.0.0.1')
KAFKA_PORT = int(os.getenv('KAFKA_PORT', 9092))