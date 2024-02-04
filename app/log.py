import logging
import colorlog

# Создаем логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Создаем обработчик для вывода сообщений логгирования в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создаем форматтер с цветным выводом
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Назначаем форматтер обработчику
console_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(console_handler)
